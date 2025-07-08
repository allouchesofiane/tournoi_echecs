import json
import os

from models.tournament import Tournament
from views.view_main import DisplayTournamentView

DATABASE_PATH = "data_base/tournaments.json"


class TournamentController:
    def __init__(self):
        self.view = DisplayTournamentView()

    def __call__(self):
        tournaments = self.load_tournaments()
        self.view.show_all_tournaments(tournaments)

    def load_tournaments(self):
        if not os.path.exists(DATABASE_PATH):
            return []

        with open(DATABASE_PATH, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return [Tournament(**t) for t in data]
            except json.JSONDecodeError:
                return []


    def create_tournament(self):
        print("Fonctionnalité de création de tournoi à venir.")

    def list_tournaments(self):
        print("Fonctionnalité de liste des tournois à venir.")
