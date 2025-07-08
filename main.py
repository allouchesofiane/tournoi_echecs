
from controllers.player_controller import save_players, load_players
from controllers.tournament_controller import TournamentController
from models.players import Player
from views.view_main import PlayerView


def main():
    player_view = PlayerView()
    players = load_players()
    tournament_controller = TournamentController()

    while True:
        print("\n=== Menu Principal ===")
        print("1. Ajouter un joueur")
        print("2. Afficher les joueurs")
        print("3. Gérer les tournois")
        print("4. Quitter")
        choice = input("Votre choix : ")

        if choice == "1":
            player_info = player_view.get_player_info()
            new_player = Player(**player_info)
            players.append(new_player)
            save_players(players)
            player_view.confirm_player_added(new_player)

        elif choice == "2":
            player_view.show_all_players(players)

        elif choice == "3":
            tournament_controller.create_tournament()

        elif choice == "4":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez entrer 1, 2, 3 ou 4.")


if __name__ == "__main__":
    main()
