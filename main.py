import json
import os
from models.players import Player
from views.view_main import PlayerView
from controllers.tournament_controller import TournamentController

DATA_FILE = "data_base/players.json"
os.makedirs("data_base", exist_ok=True)

def load_players():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
            return [Player(**player_info) for player_info in data]
        except json.JSONDecodeError:
            return []

def save_players(players):
    with open(DATA_FILE, "w") as f:
        json.dump([player.to_dict() for player in players], f, indent=4)

def main():
    view = PlayerView()
    players = load_players()

    while True:
        print("\n=== Menu Principal ===")
        print("1. Ajouter un joueur")
        print("2. Afficher les joueurs")
        print("3. Gérer les tournois")
        print("4. Quitter")        
        choice = input("Votre choix : ")

        if choice == "1":
            player_info = view.get_player_info()
            new_player = Player(**player_info)
            players.append(new_player)
            save_players(players)
            view.confirm_player_added(new_player)

        elif choice == "2":
            view.show_all_players(players)

        elif choice == "3":
            tournament_controller = TournamentController()
            tournament_controller.create_tournament()
        
        elif choice == "4":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3, 4.")

if __name__ == "__main__":
    main()

