import json
import os
from models.tournament import Tournament
from views.view_main import DisplayTournamentView

DATABASE_PATH = "data_base/tournaments.json"


class TournamentController:
    def __init__(self):
        self.view = DisplayTournamentView()

    def __call__(self):
        while True:
            print("\n=== Menu Tournoi ===")
            print("1. Créer un nouveau tournoi")
            print("2. Afficher les tournois existants")
            print("3. Retour au menu principal")
            choice = input("Votre choix : ")

            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.list_tournaments()
            elif choice == "3":
                break
            else:
                print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

    def load_tournaments(self):
        if not os.path.exists(DATABASE_PATH):
            return []

        try:
            with open(DATABASE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Tournament(**t) for t in data]
        except json.JSONDecodeError:
            return []

    def save_tournament(self, tournament_data):
        try:
            with open(DATABASE_PATH, "r", encoding="utf-8") as f:
                tournaments = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            tournaments = []

        tournaments.append(tournament_data)

        with open(DATABASE_PATH, "w", encoding="utf-8") as f:
            json.dump(tournaments, f, indent=4, ensure_ascii=False)

    def create_tournament(self):
        print("\n=== Création d'un nouveau tournoi ===")
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        date = input("Date : ")
        rounds = input("Nombre de tours (défaut 4) : ") or 4
        time_control = input("Contrôle du temps (Blitz / Bullet / Coup rapide) : ") or "Blitz"
        description = input("Description : ")

        new_tournament = Tournament(
            name=name,
            location=location,
            date=date,
            rounds=int(rounds),
            time_control=time_control,
            description=description
        )

        self.save_tournament(new_tournament.to_dict())
        print("\n✅ Tournoi ajouté avec succès.")

    def list_tournaments(self):
        tournaments = self.load_tournaments()
        self.view.show_all_tournaments(tournaments)
