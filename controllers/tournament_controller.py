"""Contrôleur pour la gestion des tournois."""

import random
from models.tournament import Tournament
from models.match import Match
from models.round import Round
from views.tournament_view import TournamentView
from views.round_view import RoundView
from controllers.player_controller import load_players
from utils.db_manager import DatabaseManager

DATABASE_PATH = "data/tournaments.json"


class TournamentController:
    """Contrôleur qui gère les opérations sur les tournois."""

    def __init__(self):
        """Initialise le contrôleur des tournois."""
        self.view = TournamentView()
        self.round_view = RoundView()
        self.db_manager = DatabaseManager()

    def run(self):
        """Gère le menu des tournois."""
        while True:
            self.view.display_tournament_menu()

            choice = int(input("Votre choix : "))

            if choice == 1:
                self.create_tournament()
            elif choice == 2:
                self.list_tournaments()
            elif choice == 3:
                self.start_first_round_menu()
            elif choice == 4:
                self.show_rounds_and_matches()
            elif choice == 5:
                self.create_next_round_menu()
            elif choice == 6:
                self.show_final_ranking()
            elif choice == 7:
                break
            else:
                print("choix invalide")

    def create_tournament(self):
        """Crée un nouveau tournoi avec sélection des joueurs."""
        # Collecte des informations du tournoi
        tournament_info = self.view.prompt_tournament_info()

        # Validation des champs obligatoires
        if not tournament_info["name"] or not tournament_info["location"] or not tournament_info["date"]:
            print("Le nom, le lieu et la date sont obligatoires.")
            return

        # Chargement et sélection des joueurs
        players = load_players()
        selection = self.view.display_player_selection(players)

        if not selection:
            return

        # Traitement de la sélection
        if True:
            selected_indices = [int(i.strip()) - 1 for i in selection.split(",") if i.strip().isdigit()]

        # Validation du nombre de joueurs
        if len(selected_indices) < 2:
            self.view.display_not_enough_players()
            return

        # Récupération des joueurs sélectionnés
        selected_players = [players[i] for i in selected_indices if 0 <= i < len(players)]
        player_ids = [p.national_id for p in selected_players]

        # Avertissement si nombre impair
        if len(player_ids) % 2 != 0:
            self.view.display_odd_number_warning(len(player_ids))

        # Création du tournoi
        new_tournament = Tournament(
            name=tournament_info["name"],
            location=tournament_info["location"],
            date=tournament_info["date"],
            rounds=tournament_info["rounds"],
            time_control=tournament_info["time_control"],
            description=tournament_info["description"],
            players=player_ids
        )

        self.save_tournament(new_tournament)
        self.view.display_tournament_created(new_tournament)

    def list_tournaments(self):
        """Affiche la liste de tous les tournois."""
        tournaments = self.load_tournaments()
        self.view.display_tournaments_list(tournaments)

    def start_first_round_menu(self):
        """Menu pour démarrer le premier tour d'un tournoi."""
        tournaments = self.load_tournaments()
        tournament = self.view.select_tournament(tournaments)

        if not tournament:
            print("aucun tournoi trouvé")
            return

        if tournament.rounds_list:
            print("Ce tournoi a déjà commencé.")
            return

        self.start_first_round(tournament)

    def start_first_round(self, tournament):
        """Démarre le premier tour d'un tournoi."""
        if len(tournament.players) < 2:
            print("Pas assez de joueurs pour lancer le tournoi.")
            return

        if len(tournament.players) % 2 != 0:
            print("Nombre impair de joueurs. Un joueur sera exempt à chaque tour.")

        # Mélange aléatoire pour le premier tour
        players_copy = tournament.players.copy()
        random.shuffle(players_copy)

        # Création des matchs
        matches = []
        for i in range(0, len(players_copy), 2):
            if i + 1 < len(players_copy):
                match = Match(players_copy[i], players_copy[i+1])
                matches.append(match)
            else:
                # Joueur exempté
                exempt_player = players_copy[i]
                match = Match(exempt_player, None, 1.0, 0.0)
                matches.append(match)
        # Création du tour
        round_obj = Round(name="Tour 1", matchs=matches)

        # Affichage et confirmation
        self.round_view.display_round_creation("Tour 1", matches)

        if not self.round_view.confirm_round_start():
            print("Création du tour annulée.")
            return

        # Saisie des scores
        self.round_view.display_score_entry_header("Tour 1")

        for match in matches:
            while True:
                result = self.round_view.get_match_result(match)
                if result:
                    match.set_result(*result)
                    break

        round_obj.end_round()

        # Ajout du tour au tournoi et sauvegarde
        tournament.add_round(round_obj.to_dict())
        self.update_tournament(tournament)

        self.round_view.display_round_completed("Tour 1")

    def show_rounds_and_matches(self):
        """Affiche les tours et matchs d'un tournoi."""
        tournaments = self.load_tournaments()
        tournament = self.view.select_tournament(tournaments)

        if tournament:
            self.round_view.display_rounds_list(tournament.name, tournament.rounds_list)

    def create_next_round_menu(self):
        """Menu pour créer le prochain tour d'un tournoi."""
        tournaments = self.load_tournaments()
        tournament = self.view.select_tournament(tournaments)

        if tournament:
            self.create_next_round(tournament)

    def create_next_round(self, tournament):
        """Crée le prochain tour en respectant le système suisse."""

        if not tournament.rounds_list:
            self.round_view.display_no_tournament_started()
            return

        if tournament.is_finished():
            self.round_view.display_tournament_finished()
            return

        player_scores = self.calculate_scores(tournament)
        sorted_players = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)
        self.round_view.display_current_standings(sorted_players)

        matches = self.generate_swiss_pairs(sorted_players, tournament)
        if not matches:
            self.round_view.display_no_valid_pairings()
            return

        round_number = len(tournament.rounds_list) + 1
        new_round = Round(name=f"Tour {round_number}", matchs=matches)

        self.round_view.display_round_creation(new_round.name, matches)
        if not self.round_view.confirm_round_start():
            print("Création du tour annulée.")
            return

        self.round_view.display_score_entry_header(new_round.name)
        for match in matches:
            if match.player_2 is None:
                continue
            while True:
                result = self.round_view.get_match_result(match)
                if result:
                    try:
                        match.set_result(*result)
                        break
                    except ValueError:
                        self.round_view.display_invalid_scores()

        new_round.end_round()
        tournament.add_round(new_round.to_dict())
        self.update_tournament(tournament)
        self.round_view.display_round_completed(new_round.name)

    def show_final_ranking(self):
        """Affiche le classement final d'un tournoi."""
        tournaments = self.load_tournaments()
        tournament = self.view.select_tournament(tournaments)

        if not tournament:
            return

        if not tournament.rounds_list:
            print("Aucun tour n'a été joué dans ce tournoi.")
            return

        # Calcul des scores finaux
        scores = {pid: 0.0 for pid in tournament.players}
        for round_data in tournament.rounds_list:
            for match in round_data["matchs"]:
                pid1, score1 = match[0]
                scores[pid1] += score1

                pid2, score2 = match[1]
                if pid2 in scores:
                    scores[pid2] += score2

        # Récupération des infos des joueurs
        all_players = load_players()
        players_dict = {p.national_id: p for p in all_players}

        # Tri et préparation du classement
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        rankings = []
        for pid, score in sorted_scores:
            player = players_dict.get(pid)
            if player:
                name = player.get_full_name()
            else:
                name = f"Joueur inconnu ({pid})"
            rankings.append((name, score))

        # Affichage via la vue
        from views.report_view import ReportView
        report_view = ReportView()
        report_view.display_ranking_report(tournament.name, rankings)

    def save_tournament(self, tournament):
        """Sauvegarde un nouveau tournoi."""
        tournaments = self.load_tournaments()
        tournaments.append(tournament)
        self.save_all_tournaments(tournaments)

    def update_tournament(self, tournament):
        """Met à jour un tournoi existant."""
        tournaments = self.load_tournaments()

        # Remplacer le tournoi existant
        for i, t in enumerate(tournaments):
            if t.name == tournament.name and t.date == tournament.date:
                tournaments[i] = tournament
                break

        self.save_all_tournaments(tournaments)

    def save_all_tournaments(self, tournaments):
        """Sauvegarde tous les tournois dans le fichier JSON."""
        self.db_manager.save_data(DATABASE_PATH, [t.to_dict() for t in tournaments])

    def load_tournaments(self):
        """Charge tous les tournois depuis le fichier JSON."""
        data = self.db_manager.load_data(DATABASE_PATH)

        tournaments = []
        for t in data:
            tournament = Tournament(
                name=t["name"],
                location=t["location"],
                date=t["date"],
                rounds=t.get("rounds", 4),
                time_control=t.get("time_control", "Blitz"),
                description=t.get("description", ""),
                players=t.get("players", []),
                rounds_list=t.get("rounds_list", [])
            )
            tournaments.append(tournament)

        return tournaments

    def calculate_scores(self, tournament):
        """Calcule les scores des joueurs pour le tournoi."""
        scores = {pid: 0.0 for pid in tournament.players}
        for round_data in tournament.rounds_list:
            for match in round_data["matchs"]:
                p1, s1 = match[0]
                p2, s2 = match[1]
                scores[p1] += s1
                if p2 in scores:  # ✅ évite les erreurs avec 'EXEMPT' ou None
                    scores[p2] += s2
        return scores

    def generate_swiss_pairs(self, sorted_players, tournament):
        previous_matches = set()
        for round_data in tournament.rounds_list:
            for match in round_data["matchs"]:
                p1, _ = match[0]
                p2, _ = match[1]
                previous_matches.add(frozenset([p1, p2]))

        matches = []
        used = set()

        for i, (p1, _) in enumerate(sorted_players):
            if p1 in used:
                continue
            for j in range(i + 1, len(sorted_players)):
                p2 = sorted_players[j][0]
                if p2 not in used and frozenset([p1, p2]) not in previous_matches:
                    matches.append(Match(p1, p2))
                    used.update([p1, p2])
                    break
                elif frozenset([p1, p2]) in previous_matches:
                    self.round_view.display_pairing_conflict(p1, p2)

        # Ajouter joueur exempt si impair
        remaining = [pid for pid, _ in sorted_players if pid not in used]
        if len(remaining) == 1:
            match = Match(remaining[0], None)
            match.set_result(1.0, 0.0)
            matches.append(match)

        return matches
