"""Modèle représentant un match entre deux joueurs."""


class Match:
    """Représente un match entre deux joueurs avec leurs scores."""

    def __init__(self, player_1, player_2, score_1=0.0, score_2=0.0):
        """
        Initialise un match avec deux joueurs et leurs scores.
        """
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = float(score_1)
        self.score_2 = float(score_2)

    def set_result(self, score_1, score_2):
        """
        Définit le résultat du match.
        """
        valid_scores = [(1.0, 0.0), (0.0, 1.0), (0.5, 0.5)]
        if (float(score_1), float(score_2)) not in valid_scores:
            raise ValueError("Scores invalides. Utilisez: 1-0, 0-1 ou 0.5-0.5")

        self.score_1 = float(score_1)
        self.score_2 = float(score_2)

    def to_tuple(self):
        """
        Convertit l'objet Match en tuple pour la sérialisation JSON.
        """
        if self.player_2 is None:
            return ([self.player_1, self.score_1], ["EXEMPT", self.score_2])
        return ([self.player_1, self.score_1], [self.player_2, self.score_2])

    def get_winner(self):
        """
        Retourne l'identifiant du gagnant ou None si match nul.
        """
        if self.score_1 > self.score_2:
            return self.player_1
        elif self.score_2 > self.score_1:
            return self.player_2
        return None  # Match nul

    def is_played(self):
        """Vérifie si le match a été joué."""
        return self.score_1 != 0.0 or self.score_2 != 0.0

    def __str__(self):
        """Représentation textuelle du match."""
        if self.player_2 is None:
            return f"{self.player_1} est exempté (1 point)"
        if self.is_played():
            return f"{self.player_1} ({self.score_1}) vs {self.player_2} ({self.score_2})"
        return f"{self.player_1} vs {self.player_2}"
