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
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump([p.to_dict() for p in players], f, indent=4, ensure_ascii=False)


def load_players():
    if not os.path.exists(DATA_PATH):
        return []

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

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
