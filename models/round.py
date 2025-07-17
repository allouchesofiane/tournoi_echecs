"""Modèle représentant un tour de tournoi."""

from datetime import datetime


class Round:
    """Représente un tour complet avec une liste de matchs et des timestamps."""

    def __init__(self, name=None, matchs=None, start_time=None, end_time=None):
        """
        Initialise un tour.
        """
        self.name = name if name else "Tour"
        self.matchs = matchs if matchs else []
        self.start_time = start_time if start_time else datetime.now().isoformat()
        self.end_time = end_time

    def add_match(self, match):
        """
        Ajoute un match au tour.
        """
        self.matchs.append(match)

    def start_round(self):
        """Marque le début du tour avec l'heure actuelle."""
        self.start_time = datetime.now().isoformat()

    def end_round(self):
        """Marque le tour comme terminé en enregistrant l'heure de fin."""
        self.end_time = datetime.now().isoformat()

    def is_finished(self):
        """
        Vérifie si le tour est terminé.
        """
        return self.end_time is not None

    def to_dict(self):
        """
        Convertit l'objet Round en dictionnaire pour la sérialisation JSON.
        """
        return {
            "name": self.name,
            "matchs": [match.to_tuple() for match in self.matchs],
            "start_time": self.start_time,
            "end_time": self.end_time
        }

    def __str__(self):
        """Représentation textuelle du tour."""
        status = "Terminé" if self.is_finished() else "En cours"
        return f"{self.name} - {status} ({len(self.matchs)} matchs)"
