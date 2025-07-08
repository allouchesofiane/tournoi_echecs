import json
from operator import attrgetter
from models.players import Player
from views.view_main import DisplayPlayersView


class PlayerController:
    def __init__(self):
        self.view = DisplayPlayersView()

    def add_player(self):
        new_player = self.view.prompt_player_info()
        players = self.load_players()
        players.append(new_player.to_dict())
        self.save_players(players)
        print("\nJoueur ajouté avec succès !\n")

    def display_sorted_players(self):
        players_data = self.load_players()
        players = [Player(**player_info) for player_info in players_data]

        while True:
            print("1 - Afficher les joueurs par ordre alphabétique")
            print("2 - Afficher les joueurs par classement")
            print("3 - Retour au menu principal")
            choice = input("--> ")

            if choice == "1":
                players.sort(key=attrgetter("last_name"))
                self.view.display_players(players)
            elif choice == "2":
                players.sort(key=attrgetter("ranking"))
                self.view.display_players(players)
            elif choice == "3":
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    @staticmethod
    def load_players():
        try:
            with open("data_base/players.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def save_players(players):
        with open("data_base/players.json", "w", encoding="utf-8") as file:
            json.dump(players, file, indent=4, ensure_ascii=False)
