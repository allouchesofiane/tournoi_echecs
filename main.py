import os
from controllers.player_controller import load_players, save_players
from controllers.tournament_controller import TournamentController
from models.players import Player
from views.view_main import PlayerView

# Chemin du fichier contenant les joueurs
DATA_FILE = "data_base/players.json"
# Crée le dossier 'data_base' s’il n’existe pas, pour stocker les fichiers JSON
os.makedirs("data_base", exist_ok=True)


def main():
    """
    Point d'entrée principal de l'application.

    Ce menu permet :
    - d’ajouter un joueur (avec sauvegarde en JSON),
    - d’afficher tous les joueurs enregistrés,
    - d’accéder au menu de gestion des tournois,
    - ou de quitter l’application.

    L'application suit une architecture MVC :
    - les modèles contiennent les entités (Player, Tournament, etc.),
    - les vues gèrent les interactions utilisateur,
    - les contrôleurs gérent la logique métier.
    """
    # Initialisation de la vue du joueur
    player_view = PlayerView()
    # Chargement des joueurs existants depuis le fichier JSON
    players = load_players()
    # Création du contrôleur de tournoi
    tournament_controller = TournamentController()
    # Boucle principale du menu
    while True:
        print("\n=== Menu Principal ===")
        print("1. Ajouter un joueur")
        print("2. Afficher les joueurs")
        print("3. Gérer les tournois")
        print("4. Quitter")

        choice = input("Votre choix : ")
        # Ajouter un joueur
        if choice == "1":
            player_info = player_view.get_player_info()
            new_player = Player(**player_info)
            players.append(new_player)
            save_players(players)
            player_view.confirm_player_added(new_player)
        # Afficher tous les joueurs
        elif choice == "2":
            player_view.show_all_players(players)
        # Accès au menu tournoi
        elif choice == "3":
            tournament_controller()  # appel du __call__ de TournamentController
        # sort de l'application et break la boucle
        elif choice == "4":
            print("Au revoir !")
            break
        # le cas ou le choix n'est pas 1,2,3 ou 4
        else:
            print("Choix invalide. Veuillez entrer 1, 2, 3 ou 4.")


# Lancement du programme si ce fichier est exécuté directement
if __name__ == "__main__":
    main()
