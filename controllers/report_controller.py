"""Contrôleur pour la gestion des rapports."""

from views.report_view import ReportView
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from controllers.player_controller import load_players
from controllers.tournament_controller import TournamentController


class ReportController:
    """Contrôleur qui gère la génération et l'affichage des rapports."""

    def __init__(self):
        """Initialise le contrôleur des rapports."""
        self.view = ReportView()
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
        self.tournament_controller = TournamentController()

    def run(self):
        """Gère le menu des rapports."""
        while True:
            self.view.display_report_menu()
            choice = int(input("Votre choix : "))
            if choice == 1:
                self.show_all_players_alphabetical()
            elif choice == 2:
                self.show_all_tournaments()
            elif choice == 3:
                self.show_tournament_details()
            elif choice == 4:
                self.show_tournament_ranking()
            elif choice == 5:
                break
            else:
                print("choix invalide")

    def show_all_players_alphabetical(self):
        """
        Rapport 1: Liste de tous les joueurs par ordre alphabétique.
        """
        players = load_players()
        self.view.display_players_report(players)

    def show_all_tournaments(self):
        """
        Rapport 2: Liste de tous les tournois avec statistiques.
        """
        tournaments = self.tournament_controller.load_tournaments()
        self.view.display_tournaments_report(tournaments)

    def show_tournament_details(self):
        """
        Rapport 3: Détails complets d'un tournoi spécifique.
        """
        tournaments = self.tournament_controller.load_tournaments()
        tournament = self.tournament_view.select_tournament(tournaments)
        if not tournament:
            return
        # Charger les joueurs pour avoir leurs noms
        all_players = load_players()
        players_dict = {p.national_id: p for p in all_players}
        self.view.display_tournament_detail_report(tournament, players_dict)

    def show_tournament_ranking(self):
        """
        Rapport 4: Classement d'un tournoi spécifique.
        """
        tournaments = self.tournament_controller.load_tournaments()
        tournament = self.tournament_view.select_tournament(tournaments)

        if not tournament:
            return
        if not tournament.rounds_list:
            print("Aucun tour n'a été joué dans ce tournoi.")
            return
        # Calcul des scores
        scores = {pid: 0.0 for pid in tournament.players}
        for round_data in tournament.rounds_list:
            for match in round_data["matchs"]:
                pid1, score1 = match[0]
                pid2, score2 = match[1]
                scores[pid1] += score1
                scores[pid2] += score2
        # Récupération des noms des joueurs
        all_players = load_players()
        players_dict = {p.national_id: p for p in all_players}
        # Préparation du classement
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        rankings = []

        for pid, score in sorted_scores:
            player = players_dict.get(pid)
            if player:
                name = player.get_full_name()
            else:
                name = f"Joueur inconnu ({pid})"
            rankings.append((name, score))

        self.view.display_ranking_report(tournament.name, rankings)
