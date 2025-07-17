"""Contrôleur pour la gestion des joueurs."""

from views.player_view import PlayerView
from models.player import Player
from utils.db_manager import DatabaseManager

DATA_PATH = "data/players.json"


class PlayerController:
    """Contrôleur qui gère les opérations sur les joueurs."""

    def __init__(self):
        """Initialise le contrôleur des joueurs."""
        self.view = PlayerView()
        self.db_manager = DatabaseManager()

    def run(self):
        """Gère le menu des joueurs."""
        while True:
            self.view.display_player_menu()
            choice = int(input("Votre choix : "))
            if choice == 1:
                # Ajouter un joueur
                self.add_player()
            elif choice == 2:
                # Afficher tous les joueurs
                self.list_players()
            elif choice == 3:
                # Rechercher un joueur
                self.search_player()
            elif choice == 4:
                # Retour au menu principal
                break
            else:
                print("choix invalide")

    def add_player(self):
        """Ajoute un nouveau joueur avec validation complète."""
        last_name, first_name, date_of_birth, national_id = self.view.prompt_new_player()
        # Création du joueur
        player = Player(last_name, first_name, date_of_birth, national_id.upper())
        # Vérification des doublons
        players = self.load_players()
        # Ajout et sauvegarde
        players.append(player)
        self.save_players(players)
        self.view.display_player_added(player)

    def list_players(self):
        """Affiche la liste de tous les joueurs."""
        players = self.load_players()
        self.view.display_players_list(players)

    def search_player(self):
        """Recherche un joueur par nom, prénom ou ID."""
        players = self.load_players()
        if not players:
            print("Aucun joueur dans la base de données.")
            return

        query = self.view.get_search_query().lower()
        if not query:
            return

        # Recherche dans tous les champs
        results = []
        for player in players:
            if query in player.national_id.lower():
                results.append(player)
        self.view.display_search_results(results)

    def save_players(self, players):
        """
        Sauvegarde la liste des joueurs dans un fichier JSON.
        """
        self.db_manager.save_data(DATA_PATH, [p.to_dict() for p in players])

    def load_players(self):
        """
        Charge les joueurs depuis le fichier JSON.
        """
        data = self.db_manager.load_data(DATA_PATH)
        players = []
        for p in data:
            player = Player(
                last_name=p["last_name"],
                first_name=p["first_name"],
                date_of_birth=p["date_of_birth"],
                national_id=p["national_id"]
            )
            players.append(player)
        return players

# Fonctions utilitaires pour être utilisées par d'autres contrôleurs


def load_players():
    """Fonction utilitaire pour charger les joueurs."""
    controller = PlayerController()
    return controller.load_players()


def save_players(players):
    """Fonction utilitaire pour sauvegarder les joueurs."""
    controller = PlayerController()
    controller.save_players(players)
