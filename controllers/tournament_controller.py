import json
import os
import random
from models.tournament import Tournament, Match, Tour
from views.view_main import DisplayTournamentView
from models.players import Player

DATABASE_PATH = "data_base/tournaments.json"


class TournamentController:
    def __init__(self):
        self.view = DisplayTournamentView()

    def __call__(self):
        while True:
            print("\n=== Menu Tournoi ===")
            print("1. Créer un nouveau tournoi")
            print("2. Afficher les tournois existants")
            print("3. Créer le 1er tour d’un tournoi")
            print("4. Afficher les tours et matchs d’un tournoi")
            print("5. Créer le tour suivant d’un tournoi")
            print("6. Afficher le classement final d’un tournoi")
            print("7. Retour au menu principal")

            choice = input("Votre choix : ")

            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.list_tournaments()
            elif choice == "3":
                self.start_first_round_menu()
            elif choice == "4":
                self.show_rounds_and_matches()
            elif choice == "5":
                self.create_next_round_menu()
            elif choice == "6":
                self.show_final_ranking()
            elif choice == "7":
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 6.")

    def load_tournaments(self):
        if not os.path.exists(DATABASE_PATH):
            return []

        try:
            with open(DATABASE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Tournament(**t) for t in data]
        except json.JSONDecodeError:
            return []

    def create_tournament(self):

        print("\n=== Création d'un nouveau tournoi ===")
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        date = input("Date : ")
        rounds = input("Nombre de tours (défaut 4) : ") or 4
        time_control = input("Contrôle du temps(Blitz/ Bullet/ Coup rapide) : ") or "Blitz"
        description = input("Description : ")

    # Charger les joueurs disponibles
        try:
            with open("data_base/players.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                players = [Player(**p) for p in data]
        except (FileNotFoundError, json.JSONDecodeError):
            players = []

        # Afficher les joueurs avec un index
        print("\n=== Joueurs disponibles ===")
        if not players:
            print("Aucun joueur disponible. Ajoutez des joueurs avant de créer un tournoi.")
            return

        for idx, player in enumerate(players, 1):
            print(f"{idx}. {player.first_name} {player.last_name} ({player.national_id})")

        # Sélection des joueurs
        print("\nEntrez les numéros des joueurs à ajouter au tournoi (ex: 1,3,5). Minimum 2 joueurs.")
        selected = input("Sélection : ")
        selected_indices = [int(i.strip()) - 1 for i in selected.split(",") if i.strip().isdigit()]

        if len(selected_indices) < 2:
            print(" Vous devez sélectionner au moins 2 joueurs pour créer un tournoi.")
            return

        selected_players = [players[i] for i in selected_indices if 0 <= i < len(players)]
        player_ids = [p.national_id for p in selected_players]

        # Création du tournoi avec les joueurs sélectionnés
        new_tournament = Tournament(
            name=name,
            location=location,
            date=date,
            rounds=int(rounds),
            time_control=time_control,
            description=description,
            players=player_ids
        )

        self.save_tournament(new_tournament.to_dict())
        print("\n Tournoi ajouté avec succès avec les joueurs sélectionnés.")

    def list_tournaments(self):
        tournaments = self.load_tournaments()
        self.view.show_all_tournaments(tournaments)

    def start_first_round(self, tournament: Tournament):
        print("\n=== Démarrage du premier tour ===")

        # Récupérer les joueurs à partir de leurs identifiants
        try:
            with open("data_base/players.json", "r", encoding="utf-8") as f:
                all_players = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Impossible de charger les joueurs.")
            return

        # Associer les objets Player aux identifiants dans le tournoi
        player_objs = [
            Player(**p) for p in all_players if p["national_id"] in tournament.players
        ]

        if len(player_objs) < 2:
            print("Pas assez de joueurs pour lancer le tournoi.")
            return

        # Mélange aléatoire
        random.shuffle(player_objs)

        # Création des matchs
        matchs = []
        for i in range(0, len(player_objs), 2):
            if i + 1 < len(player_objs):
                match = Match(player_objs[i].national_id, player_objs[i+1].national_id)
                matchs.append(match)

        # Création du tour
        round_name = "Tour 1"
        first_round = Tour(name=round_name)
        for match in matchs:
            first_round.add_match(match)

        # Ajout du tour au tournoi
        tournament.rounds_list.append(first_round.to_dict())

        # Sauvegarde dans le fichier JSON
        self.update_tournament(tournament)

        print(f"\n{round_name} démarré avec {len(matchs)} matchs.")

    def update_tournament(self, tournament):
        """Remplace le tournoi existant par sa version mise à jour dans le fichier JSON"""
        try:
            with open(DATABASE_PATH, "r", encoding="utf-8") as f:
                tournaments = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            tournaments = []

        updated = []
        for t in tournaments:
            if t["name"] == tournament.name and t["date"] == tournament.date:
                updated.append(tournament.to_dict())
            else:
                updated.append(t)

        with open(DATABASE_PATH, "w", encoding="utf-8") as f:
            json.dump(updated, f, indent=4, ensure_ascii=False)

    def start_first_round_menu(self):
        tournaments = self.load_tournaments()
        if not tournaments:
            print("Aucun tournoi disponible.")
            return

        print("\n=== Sélectionner un tournoi à démarrer ===")
        for idx, t in enumerate(tournaments, 1):
            print(f"{idx}. {t.name} ({t.date})")

        choice = input("Entrez le numéro du tournoi à démarrer : ")
        if not choice.isdigit() or not (1 <= int(choice) <= len(tournaments)):
            print("Choix invalide.")
            return

        tournament = tournaments[int(choice) - 1]
        # Créer un tour
        print("\n--- Démarrage du premier tour ---")

        players = tournament.players
        if len(players) % 2 != 0:
            print("Nombre impair de joueurs. Impossible de créer des paires.")
            return

        # Générer des paires aléatoires
        random.shuffle(players)

        matchs = []
        for i in range(0, len(players), 2):
            match = Match(players[i], players[i+1])
            matchs.append(match)

        tour = Tour(name="Tour 1", matchs=matchs)

        print("\nMatchs du Tour 1 :")
        for m in matchs:
            print(m)

        print("\n=== Saisie des scores ===")
        for m in matchs:
            try:
                score_1 = float(input(f"Score pour {m.player_1} : "))
                score_2 = float(input(f"Score pour {m.player_2} : "))
            except ValueError:
                print("Entrée invalide. Les scores doivent être numériques.")
                return
            m.score_1 = score_1
            m.score_2 = score_2

        tour.close_tour()

        # Ajouter le tour au tournoi
        tournament.rounds_list.append(tour.to_dict())

        # Sauvegarder le tournoi mis à jour
        updated_data = [t.to_dict() if t.name != tournament.name else tournament.to_dict() for t in tournaments]
        with open(DATABASE_PATH, "w", encoding="utf-8") as f:
            json.dump(updated_data, f, indent=4, ensure_ascii=False)

        print("\nTour 1 terminé et enregistré.")

    def show_rounds_and_matches(self):
        tournaments = self.load_tournaments()
        if not tournaments:
            print("Aucun tournoi disponible.")
            return

        print("\n=== Sélectionner un tournoi ===")
        for idx, t in enumerate(tournaments, 1):
            print(f"{idx}. {t.name} ({t.date})")

        choice = input("Entrez le numéro du tournoi à afficher : ")
        if not choice.isdigit() or not (1 <= int(choice) <= len(tournaments)):
            print("Choix invalide.")
            return

        tournament = tournaments[int(choice) - 1]

        if not tournament.rounds_list:  # ou tournament.rounds_list selon ta version
            print("Aucun tour n’a été enregistré pour ce tournoi.")
            return

        print(f"\n=== Tours du tournoi {tournament.name} ===")
        for round_data in tournament.rounds_list:  # ou .rounds_list
            print(
                f"\n{round_data['name']} - Début : {round_data['start_time']} | "
                f"Fin : {round_data['end_time'] or 'en cours'}"
            )

            if not round_data.get("matchs"):
                print("Aucun match trouvé.")
                continue

            for match in round_data["matchs"]:
                try:
                    p1, s1 = match[0]
                    p2, s2 = match[1]
                    print(f"  ➤ {p1} ({s1}) vs {p2} ({s2})")
                except Exception as e:
                    print(f"  ⚠ Erreur lors de l'affichage du match : {e}")

    def create_first_round(self, tournament):
        """Créer automatiquement le premier tour du tournoi"""
        player_ids = tournament.players  # liste des national_id

        # Charger tous les joueurs depuis le fichier
        try:
            with open("data_base/players.json", "r", encoding="utf-8") as f:
                all_players_data = json.load(f)
                all_players = [Player(**p) for p in all_players_data]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Erreur de chargement des joueurs.")
            return

        # Filtrer les joueurs du tournoi
        selected_players = [p for p in all_players if p.national_id in player_ids]

        # Mélanger les joueurs aléatoirement
        from random import shuffle
        shuffle(selected_players)

        # Générer les matchs (paire de joueurs)
        matches = []
        for i in range(0, len(selected_players), 2):
            if i + 1 < len(selected_players):
                match = Match(selected_players[i].national_id, selected_players[i+1].national_id)
                matches.append(match)

        # Créer un objet Tour avec les matchs
        round_1 = Tour(name="Tour 1", matchs=matches)

        # Ajouter le tour au tournoi et sauvegarder
        tournament.rounds_list.append(round_1.to_dict())

        self.save_tournament(tournament.to_dict())
        print("\nPremier tour du tournoi généré automatiquement.")

    def save_tournament(self, tournament_data):
        try:
            with open(DATABASE_PATH, "r", encoding="utf-8") as f:
                tournaments = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            tournaments = []

        # Remplacer le tournoi ayant le même nom
        tournaments = [t for t in tournaments if t["name"] != tournament_data["name"]]
        tournaments.append(tournament_data)

        with open(DATABASE_PATH, "w", encoding="utf-8") as f:
            json.dump(tournaments, f, indent=4, ensure_ascii=False)

    def create_next_round(self, tournament: Tournament):
        """Crée le prochain tour en fonction des scores précédents et en évitant les re-matches."""
        print("\n=== Création du tour suivant ===")

        # Récupérer les joueurs du tournoi avec leurs scores
        player_scores = {player_id: 0.0 for player_id in tournament.players}

        # Parcourir tous les tours pour calculer les scores et l'historique des matchs
        previous_matches = set()
        for round_data in tournament.rounds_list:
            for match in round_data["matchs"]:
                p1, s1 = match[0]
                p2, s2 = match[1]
                previous_matches.add(frozenset([p1, p2]))
                player_scores[p1] += s1
                player_scores[p2] += s2

        # Trier les joueurs par score décroissant
        sorted_players = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)
        player_ids_sorted = [pid for pid, score in sorted_players]

        # Générer des paires en évitant les re-matches
        matches = []
        used_players = set()
        i = 0
        while i < len(player_ids_sorted):
            p1 = player_ids_sorted[i]
            if p1 in used_players:
                i += 1
                continue

            for j in range(i+1, len(player_ids_sorted)):
                p2 = player_ids_sorted[j]
                if p2 not in used_players and frozenset([p1, p2]) not in previous_matches:
                    matches.append(Match(p1, p2))
                    used_players.update([p1, p2])
                    break
            else:
                # Aucun adversaire disponible (impair ou tout le monde a déjà joué contre lui)
                i += 1

        # Création du nouveau tour
        round_number = len(tournament.rounds_list) + 1
        new_round = Tour(name=f"Tour {round_number}", matchs=matches)

        # Affichage des matchs
        print(f"\nMatchs du {new_round.name} :")
        for match in matches:
            print(match)

        print("\n=== Saisie des scores ===")
        for match in matches:
            try:
                score_1 = float(input(f"Score pour {match.player_1} : "))
                score_2 = float(input(f"Score pour {match.player_2} : "))
            except ValueError:
                print("Entrée invalide. Les scores doivent être numériques.")
                return
            match.score_1 = score_1
            match.score_2 = score_2

        new_round.close_tour()

        # Ajouter le tour au tournoi et sauvegarder
        tournament.rounds_list.append(new_round.to_dict())
        self.update_tournament(tournament)

        print(f"\n{new_round.name} terminé et enregistré.")

    def create_next_round_menu(self):
        tournaments = self.load_tournaments()
        if not tournaments:
            print("Aucun tournoi disponible.")
            return

        print("\n=== Sélectionner un tournoi pour le prochain tour ===")
        for idx, t in enumerate(tournaments, 1):
            print(f"{idx}. {t.name} ({t.date})")

        choice = input("Entrez le numéro du tournoi : ")
        if not choice.isdigit() or not (1 <= int(choice) <= len(tournaments)):
            print("Choix invalide.")
            return

        tournament = tournaments[int(choice) - 1]
        self.create_next_round(tournament)

    def show_final_ranking(self):
        tournaments = self.load_tournaments()
        if not tournaments:
            print("Aucun tournoi disponible.")
            return

        print("\n=== Sélectionner un tournoi ===")
        for idx, t in enumerate(tournaments, 1):
            print(f"{idx}. {t.name} ({t.date})")

        choice = input("Entrez le numéro du tournoi : ")
        if not choice.isdigit() or not (1 <= int(choice) <= len(tournaments)):
            print("Choix invalide.")
            return

        tournament = tournaments[int(choice) - 1]

        # Calcul des scores
        scores = {pid: 0.0 for pid in tournament.players}
        for round_data in tournament.rounds_list:
            for match in round_data["matchs"]:
                pid1, score1 = match[0]
                pid2, score2 = match[1]
                scores[pid1] += score1
                scores[pid2] += score2

        # Récupération des infos des joueurs
        try:
            with open("data_base/players.json", "r", encoding="utf-8") as f:
                all_players = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Impossible de charger les joueurs.")
            return

        players_dict = {p["national_id"]: p for p in all_players}

        # Tri du classement
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        print(f"\n=== Classement final du tournoi {tournament.name} ===")
        for rank, (pid, score) in enumerate(sorted_scores, start=1):
            player = players_dict.get(pid, {})
            name = f"{player.get('first_name', 'Inconnu')} {player.get('last_name', '')}"
            print(f"{rank}. {name} - {score} points")
