# Gestionnaire de Tournoi d'Échecs

Ce projet est une application en ligne de commande permettant de gérer des tournois d'échecs. Il a été développé dans le cadre d'un parcours de formation développeur Python.

## 🔧 Fonctionnalités

- Ajout et affichage de joueurs avec persistance en JSON
- Création de tournois avec :
  - nom, lieu, date, nombre de tours, description, type de cadence
  - sélection manuelle des joueurs
- Gestion du 1er tour d’un tournoi :
  - Génération aléatoire de paires
  - Saisie des scores et sauvegarde du round
- Création automatique des tours suivants :
  - Tri des joueurs par scores
  - Exclusion des paires déjà jouées
- Affichage de tous les rounds et des matchs associés
- Affichage du classement final d’un tournoi
- Architecture MVC respectée
- Conformité PEP8 avec rapport flake8-html

## 📂 Structure du projet

tournoi_echecs/
│
├── controllers/
│   └── player_controller.py
│   └── tournament_controller.py
│
├── models/
│   └── players.py
│   └── tournament.py
│
├── views/
│   └── view_main.py
│
├── data_base/
│   └── players.json
│   └── tournaments.json
│
├── flake8_rapport/  # Rapport HTML flake8
│
├── main.py
├── requirements.txt
└── README.md

## 💾 Sauvegarde des données

Les données sont enregistrées localement dans des fichiers `.json` :
- `players.json` pour les joueurs
- `tournaments.json` pour les tournois

Aucune base de données externe n’est utilisée. L’application fonctionne hors ligne.

## 🌟 Qualité du code

- Respect du pattern MVC (Modèle - Vue - Contrôleur)
- Code validé avec `flake8` et rapport généré avec `flake8-html`
- Convention PEP8 respectée

## 🔄 Installation de l'environnement virtuel

1. Créer un environnement virtuel Python :
```bash
python -m venv env
```

2. Activer l'environnement :
- Windows :
```bash
env\Scripts\activate
```
- macOS/Linux :
```bash
source env/bin/activate
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## 🚀 Lancer l'application

Dans le terminal, à la racine du projet :
```bash
python main.py
```

## 🔢 Générer un rapport flake8-html

Assurez-vous que `flake8` et `flake8-html` sont installés. Puis :
```bash
flake8 . --format=html --htmldir=flake8_rapport --max-line-length=119
```
Le rapport HTML sera créé dans le dossier `flake8_rapport/index.html`.

**Important :** le rapport ne doit afficher aucune erreur pour valider la conformité au PEP8.
