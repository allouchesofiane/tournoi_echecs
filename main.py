
from controllers.player_controller import PlayerController


def main():
    # On crée un contrôleur pour gérer les actions liées aux joueurs
    controller = PlayerController()
    # On déclenche l’ajout d’un nouveau joueur
    controller.add_player()
    
 #point d'entrée de l'application  
if __name__ == "__main__":
    main()