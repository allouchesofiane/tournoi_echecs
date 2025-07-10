
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

## 🗂️ Structure du projet

tournoi_echecs/
│
├── controllers/
│ └── player_controller.py
│ └── tournament_controller.py
│
├── models/
│ └── players.py
│ └── tournament.py
│
├── views/
│ └── view_main.py
│
├── data_base/
│ └── players.json
│ └── tournaments.json
│
├── main.py
├── requirements.txt
└── README.md


## 💾 Sauvegarde des données

Les données sont enregistrées localement dans des fichiers `.json` :
- `players.json` pour les joueurs
- `tournaments.json` pour les tournois

Aucune base de données externe n’est utilisée. L’application fonctionne hors ligne.

## Qualité du code

- Respect du pattern MVC (Modèle - Vue - Contrôleur)
- Code validé avec `flake8` et rapport généré avec `flake8-html`
- Convention PEP8 respectée

## Lancer l'application
python main.py
