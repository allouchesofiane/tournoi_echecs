"""Modèle représentant un tournoi d'échecs."""


class Tournament:
    """Représente un tournoi d'échecs avec ses paramètres et son état."""

    def __init__(self, name, location, date, rounds=4, time_control="Blitz",
                 description="", players=None, rounds_list=None):
        """
        Initialise un nouveau tournoi.
        """
        self.name = name
        self.location = location
        self.date = date
        self.rounds = int(rounds)
        self.time_control = time_control
        self.description = description
        self.players = players if players else []
        self.rounds_list = rounds_list if rounds_list else []
        self.current_round = len(self.rounds_list)

    def add_player(self, player_id):
        """
        Ajoute un joueur au tournoi.
        """
        if player_id not in self.players:
            self.players.append(player_id)

    def add_round(self, round_dict):
        """
        Ajoute un tour au tournoi.
        """
        self.rounds_list.append(round_dict)
        self.current_round = len(self.rounds_list)

    def is_finished(self):
        """
        Vérifie si le tournoi est terminé.
        bool: True si tous les tours ont été joués
        """
        return len(self.rounds_list) >= self.rounds

    def to_dict(self):
        """
        Convertit l'objet Tournament en dictionnaire pour la sérialisation JSON.
        """
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

    def __str__(self):
        """Représentation textuelle du tournoi."""
        status = "Terminé" if self.is_finished() else f"Tour {self.current_round}/{self.rounds}"
        return f"{self.name} - {self.location} ({self.date}) - {status}"
