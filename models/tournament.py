import json
from pathlib import Path
from datetime import datetime

# Crée un objet Path qui représente le chemin vers le fichier "tournaments.json"
data_file = Path("data_base/tournaments.json")
# Crée le dossier "data_base" s’il n’existe pas encore.
# .parent récupère le dossier contenant le fichier, donc ici "data_base"
# mkdir(parents=True) crée tous les dossiers manquants dans le chemin
# exist_ok=True évite une erreur si le dossier existe déjà
data_file.parent.mkdir(parents=True, exist_ok=True)
# Crée le fichier "tournaments.json" s’il n’existe pas encore
data_file.touch(exist_ok=True)


class Tournament:
    """
    Représente un tournoi d’échecs avec ses paramètres et son état.
    """
    def __init__(self, name, location, date, rounds=4, time_control="Blitz",
                 description="", players=None, rounds_list=None):
        self.name = name
        self.location = location
        self.date = date
        self.rounds = rounds
        self.time_control = time_control
        self.description = description
        self.players = players if players else []
        self.rounds_list = rounds_list if rounds_list else []

    def to_dict(self):
        # Convertit l'objet joueur en dictionnaire
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
        # Enregistre un tournoi dans le fichier JSON contenant la liste des tournois existants.
        try:
            # Ouverture du fichier en lecture pour charger les tournois existants
            with open(data_file, "r", encoding="utf-8") as f:
                tournaments = json.load(f)
        except json.JSONDecodeError:
            # Si le fichier est vide ou mal formé, on initialise une liste vide
            tournaments = []
        # Ajout du nouveau tournoi à la liste
        tournaments.append(tournament_data)

        # Écriture de la liste mise à jour dans le fichier
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(tournaments, f, indent=4, ensure_ascii=False)

    @staticmethod
    def load_all():
        # Charge et retourne la liste de tous les tournois enregistrés dans le fichier JSON.
        try:
            # Lecture du fichier contenant les tournois
            with open(data_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Si le fichier n'existe pas ou contient des données invalides, on retourne une liste vide
            return []


class Match:
    """Représente un match entre deux joueurs avec un score chacun."""
    # Attribut de classe pour numéroter les matchs automatiquement
    MATCH_NUMBER = 1

    def __init__(self, player_1, player_2, score_1=0.0, score_2=0.0):
        # Initialise un match avec deux joueurs et leurs scores.
        self.name = f"Match {Match.MATCH_NUMBER}"  # Génère un nom de match unique
        Match.MATCH_NUMBER += 1  # Incrémente le compteur pour les prochains matchs
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def to_tuple(self):
        # Convertit l'objet Match en une représentation sous forme de tuple pour faciliter la sérialisation JSON.
        return ([self.player_1, self.score_1], [self.player_2, self.score_2])

    def __str__(self):
        # Retourne une représentation textuelle du match.
        return f"{self.name} : {self.player_1} vs {self.player_2} | Scores : {self.score_1} - {self.score_2}"


class Tour:
    """Représente un tour complet avec une liste de matchs et des timestamps."""
    def __init__(self, name=None, matchs=None, start_time=None, end_time=None):
        # Initialise un tour
        self.name = name if name else "Tour"
        self.matchs = matchs if matchs else []
        self.start_time = start_time if start_time else datetime.now().isoformat()
        self.end_time = end_time  # à remplir manuellement à la fin du tour

    def add_match(self, match_instance):
        # Ajoute un match à la liste des matchs du tour.
        self.matchs.append(match_instance)

    def close_tour(self):
        # Marque le tour comme terminé en enregistrant l'heure de fin actuelle.
        self.end_time = datetime.now().isoformat()

    def to_dict(self):
        # Convertit l'objet joueur en dictionnaire
        return {
            "name": self.name,
            "matchs": [match.to_tuple() for match in self.matchs],
            "start_time": self.start_time,
            "end_time": self.end_time,
        }

    def __str__(self):
        # Retourne une représentation textuelle du match.
        return f"{self.name} | Début : {self.start_time} | Fin : {self.end_time or 'En cours'}"
