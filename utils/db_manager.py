"""Module de gestion des fichiers JSON pour la persistance des données."""

import json
import os
from pathlib import Path


class DatabaseManager:
    """Gestionnaire de base de données JSON."""

    def __init__(self):
        """initialise un objet DatabaseManager.
            crée un objet Path (de pathlib) qui représente le dossier data.
            On s'assurer que le dossier existe.
    """
        self.data_dir = Path("data")
        self._ensure_data_directory()

    def _ensure_data_directory(self):
        """S'assure que le répertoire de données existe."""
        self.data_dir.mkdir(exist_ok=True)

    def save_data(self, filepath, data):
        """
        Sauvegarde des données dans un fichier JSON.
        """
        try:
            # Sauvegarde avec encodage UTF-8 et indentation
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

        except Exception as e:
            print(f"Erreur lors de la sauvegarde : {e}")

    def load_data(self, filepath):
        """
        Charge des données depuis un fichier JSON.
        """
        if not os.path.exists(filepath):
            return []

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data if data is not None else []

        except json.JSONDecodeError:
            # Si le fichier est corrompu, on retourne une liste vide
            return []
