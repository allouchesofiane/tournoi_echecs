"""Modèle représentant un joueur d'échecs."""


class Player:
    """Représente un joueur d'échecs avec ses informations personnelles."""

    def __init__(self, last_name, first_name, date_of_birth, national_id):
        """
        Initialise un nouveau joueur avec les données fournies.
        """
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.national_id = national_id

    def to_dict(self):
        """
        Convertit l'objet Player en dictionnaire pour la sérialisation JSON.
        """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "national_id": self.national_id
        }

    def get_full_name(self):
        """Retourne le nom complet du joueur."""
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """Représentation textuelle du joueur."""
        return f"{self.get_full_name()} ({self.national_id})"
