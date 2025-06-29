
from views.player_view import PlayerView
from models.players import Player
import json
import os

"""Chemin vers le fichier json"""
DATA_PATH = "data_base/players.json" 


class PlayerController :

    """Constructeur"""
    def __init__(self):
        self.view =PlayerView()

    """Ajout d'un joueur"""
    def add_player(self):
        last_name, first_name, birth_date, national_id = self.view.prompt_new_player()
        player = Player(last_name, first_name, birth_date, national_id)
        self.save_player(player)
        self.view.confirm_player_added(player)

    """Sauvegarde des joueurs dans un fichier json"""
    def save_player(self,player):

        # Crée le dossier s’il n’existe pas
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
        #On charge les joueurs existants 
        players = self.load_players()
        #On ajoute les nouveaux joueurs
        players.append(player)
        #enregistrer tous les joueurs dans un fichier json
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in players], f, indent=4)

    def load_players(self) :

        #On retourne une liste vide si dossier inexistant
        if not os.path.exists(DATA_PATH):
            return []
        #On ouvre le fichier en lecture 
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
            players = []
            #On parcourt chaque dictionnaire
            for p in data:
                player = Player(
                    last_name=p["last_name"],
                    first_name=p["first_name"],
                    date_of_birth=p["date_of_birth"],
                    national_id=p["national_id"]
                 )
                #On ajoute ajoute chaque objet dans la liste players et return la liste d'objet
                players.append(player)
            return players