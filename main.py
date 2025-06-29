
from controllers.player_controller import PlayerController


def main():
    controller = PlayerController()
    controller.add_player()
    print(controller)
   
if __name__ == "__main__":
    main()