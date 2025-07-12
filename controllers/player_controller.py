import json
import os
from views.view_main import PlayerView
from models.players import Player

DATA_PATH = "data_base/players.json"


class PlayerController:
    def __init__(self):
        self.view = PlayerView()

    def add_player(self):
        last_name, first_name, date_of_birth, national_id = self.view.prompt_new_player()
        player = Player(last_name, first_name, date_of_birth, national_id)
        players = load_players()
        players.append(player)
        save_players(players)
        self.view.confirm_player_added(player)

    def list_players(self):
        players = load_players()
        self.view.show_all_players(players)


def save_players(players):
    """
    Sauvegarde la liste des joueurs dans un fichier JSON.

    Paramètre :
    - players (list): Liste d'objets Player à sauvegarder.
    """
    # Crée le dossier 'data_base' s'il n'existe pas déjà
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    # Ouvre le fichier en mode écriture avec encodage UTF-8
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        # Transforme chaque objet Player en dictionnaire (grâce à to_dict),
        # puis enregistre la liste obtenue dans le fichier JSON, formatée proprement
        json.dump([p.to_dict() for p in players], f, indent=4, ensure_ascii=False)


def load_players():
    """
    Charge les joueurs depuis un fichier JSON et les transforme en objets Player.

    Retourne :
        list: Liste d'objets Player si le fichier est valide, sinon une liste vide.
    """
    # Vérifie si le fichier de données existe, sinon retourne une liste vide
    if not os.path.exists(DATA_PATH):
        return []
    # Ouvre le fichier JSON en lecture avec l'encodage UTF-8
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        try:
            # Charge les données JSON dans une variable Python
            data = json.load(f)
        # Si le contenu JSON est invalide, retourne une liste vide
        except json.JSONDecodeError:
            return []
        # Liste pour stocker les objets Player
        players = []
        # Parcourt chaque dictionnaire représentant un joueur
        for p in data:
            # Pour chaque dictionnaire représentant un joueur, créer un objet Player correspondant
            player = Player(
                last_name=p["last_name"],
                first_name=p["first_name"],
                date_of_birth=p["date_of_birth"],
                national_id=p["national_id"]
            )
            # On ajoute chaque joueur dans la liste player
            players.append(player)
        # On retourne la liste
        return players
