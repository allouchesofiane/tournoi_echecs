import os
from controllers.main_controller import MainController


def create_directories():
    """
    Crée les répertoires nécessaires au fonctionnement de l'application.
    """
    directories = ['data', 'flake8_rapport']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def main():
    """
    Point d'entrée principal de l'application.
    Initialise les répertoires nécessaires et lance le contrôleur principal.
    """
    create_directories()
    app = MainController()
    app.run()


if __name__ == "__main__":
    main()
