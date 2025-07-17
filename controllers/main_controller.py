"""Contrôleur principal qui gère le menu principal de l'application."""

from views.main_view import MainView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController


class MainController:
    """Contrôleur principal qui orchestre l'application."""

    def __init__(self):
        """Initialise le contrôleur principal et ses dépendances."""
        self.view = MainView()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()
        self.report_controller = ReportController()

    def run(self):
        """Lance la boucle principale de l'application."""
        # Affichage du message de bienvenue
        self.view.display_welcome()
        # Boucle principale
        while True:
            self.view.display_main_menu()
            choice = int(input("Votre choix : "))
            if choice == 1:
                # Gestion des joueurs
                self.player_controller.run()
            elif choice == 2:
                # Gestion des tournois
                self.tournament_controller.run()
            elif choice == 3:
                # Rapports
                self.report_controller.run()
            elif choice == 4:
                # Quitter
                self.view.display_goodbye()
                break
            else:
                # Choix invalide
                print("choix invalide")
