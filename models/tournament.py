import json
from pathlib import Path

data_file = Path("data_base/tournaments.json")
data_file.parent.mkdir(parents=True, exist_ok=True)
data_file.touch(exist_ok=True)


class Tournament:
    def __init__(self, name, location, date, rounds=4, time_control="Blitz", description="", players=None, rounds_list=None):
        self.name = name
        self.location = location
        self.date = date
        self.rounds = rounds
        self.time_control = time_control
        self.description = description
        self.players = players if players else []
        self.rounds_list = rounds_list if rounds_list else []

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "rounds": self.rounds,
            "time_control": self.time_control,
            "description": self.description,
            "players": self.players,
            "rounds_list": self.rounds_list
        }

    @staticmethod
    def save(tournament_data):
        try:
            with open(data_file, "r", encoding="utf-8") as f:
                tournaments = json.load(f)
        except json.JSONDecodeError:
            tournaments = []

        tournaments.append(tournament_data)

        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(tournaments, f, indent=4, ensure_ascii=False)

    @staticmethod
    def load_all():
        try:
            with open(data_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []