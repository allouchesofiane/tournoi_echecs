import json
from pathlib import Path
from datetime import datetime
4
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


class Round:
    """Représente un match entre deux joueurs avec un score chacun."""
    ROUND_NUMBER = 1

    def __init__(self, player_1, player_2, score_1=0.0, score_2=0.0):
        self.name = f"Round {Round.ROUND_NUMBER}"
        Round.ROUND_NUMBER += 1
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def to_tuple(self):
        return ([self.player_1, self.score_1], [self.player_2, self.score_2])

    def __str__(self):
        return f"{self.name} : {self.player_1} vs {self.player_2} | Scores : {self.score_1} - {self.score_2}"


class Tour:
    """Représente un tour complet avec une liste de rounds et des timestamps."""
    def __init__(self, name=None, rounds=None, start_time=None, end_time=None):
        self.name = name if name else "Tour"
        self.rounds = rounds if rounds else []
        self.start_time = start_time if start_time else datetime.now().isoformat()
        self.end_time = end_time  # à remplir manuellement à la fin du tour

    def add_round(self, round_instance):
        self.rounds.append(round_instance)

    def close_tour(self):
        self.end_time = datetime.now().isoformat()

    def to_dict(self):
        return {
            "name": self.name,
            "rounds": [r.to_tuple() for r in self.rounds],
            "start_time": self.start_time,
            "end_time": self.end_time,
        }

    def __str__(self):
        return f"{self.name} | Début : {self.start_time} | Fin : {self.end_time or 'En cours'}"
