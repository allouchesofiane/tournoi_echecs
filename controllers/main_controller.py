# main_controller.py
from views.view_main import MainDisplay, ClearScreen, InputView, MessageView
# (on ajoutera les imports pour les sous-contrôleurs plus tard)

class MainController:
    """Contrôleur principal qui gère le menu principal de l'application."""

    def __init__(self):
        self.display = MainDisplay()
        self.clear = ClearScreen()
        self.input_view = InputView()
        self.message = MessageView()

    def __call__(self):
        while True:
            self.clear()  # Nettoie l'écran à chaque boucle
            self.display.display_title()  # Affiche le menu principal

            choice = self.input_view.get_input("Votre choix")

            if choice == "1":
                self.message.show_message("→ Accès au menu joueur (à implémenter)")
                # Ici, on appellera le PlayerController plus tard
                input("Appuyez sur Entrée pour revenir au menu.")
            elif choice == "2":
                self.message.show_message("→ Accès au menu tournoi (à implémenter)")
                # Ici, on appellera le TournamentController plus tard
                input("Appuyez sur Entrée pour revenir au menu.")
            elif choice == "3":
                self.message.show_message("→ À bientôt 👋")
                break
            else:
                self.message.show_message("⚠️ Choix invalide. Veuillez réessayer.")
                input("Appuyez sur Entrée pour continuer.")
