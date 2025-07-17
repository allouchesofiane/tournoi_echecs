"""Vue pour le menu principal de l'application."""


class MainView():
    """Gère l'affichage du menu principal."""

    def display_welcome(self):
        """Affiche le message de bienvenue."""
        print()
        print("-------------GESTIONNAIRE DE TOURNOIS D'ÉCHECS----------------")
        print()
        print("--------------Application de gestion de tournois-------------")
        print()

    def display_main_menu(self):
        """Affiche le menu principal de l'application."""
        print("--------------------MENU PRINCIPAL---------------------------")
        print()
        print("1- Gestion des joueurs")
        print("2- Gestion des tournois")
        print("3- Rapports")
        print("4- Quitter")

    def display_goodbye(self):
        """Affiche le message de fin."""
        print(" Au revoir")
