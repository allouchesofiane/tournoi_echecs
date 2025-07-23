# Gestionnaire de Tournois d'Échecs 

Application Python en ligne de commande pour gérer des tournois d'échecs. 
Développée en suivant l'architecture MVC (Modèle-Vue-Contrôleur) et les principes de la programmation orientée objet.

##  Table des matières

- [Fonctionnalités](#-fonctionnalités)
- [Architecture du projet](#-architecture-du-projet)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Structure des données](#-structure-des-données)
- [Développement](#-développement)

##  Fonctionnalités

### Gestion des joueurs
-  Ajout de nouveaux joueurs
-  Affichage de tous les joueurs (tri alphabétique)
-  Recherche de joueurs par ID
-  Persistance des données en JSON

### Gestion des tournois
-  Création de tournois avec paramètres personnalisables
-  Sélection des joueurs participants
-  Génération automatique des appariements
-  Évitement des matchs en double
-  Gestion des tours successifs
-  Calcul automatique des classements

### Rapports détaillés
-  Liste complète des joueurs
-  Liste de tous les tournois
-  Détails complets d'un tournoi
-  Classement 

##  Architecture du projet

```
TOURNOI_ECHECS/
│
├── main.py                      # Point d'entrée principal
├── requirements.txt             # Dépendances Python
├── .flake8                      # Configuration flake8
├── .gitignore                  # Fichiers ignorés par Git
├── README.md                   # Ce fichier
│
├── models/                     # Modèles 
│   ├── __init__.py
│   ├── player.py              # Modèle Joueur
│   ├── tournament.py          # Modèle Tournoi
│   ├── match.py               # Modèle Match
│   └── round.py               # Modèle Tour
│
├── views/                      # interface utilisateur
│   ├── __init__.py
│   ├── main_view.py           # Vue du menu principal
│   ├── player_view.py         # Vue pour les joueurs
│   ├── tournament_view.py     # Vue pour les tournois
│   ├── round_view.py          # Vue pour les tours et matchs
│   └── report_view.py         # Vue pour les rapports
│
├── controllers/                # Contrôleur 
│   ├── __init__.py
│   ├── main_controller.py     # Contrôleur principal
│   ├── player_controller.py   # Contrôleur des joueurs
│   ├── tournament_controller.py # Contrôleur des tournois
│   └── report_controller.py   # Contrôleur des rapports
│
├── utils/                      # Utilitaires et helpers
│   ├── __init__.py
│   └── db_manager.py          # Gestion des fichiers JSON
│
├── data/                       # Données persistantes
│   ├── players.json           # Base de données des joueurs
│   └── tournaments.json       # Base de données des tournois
│
└── flake8_rapport/            # Rapport de conformité PEP8
    └── index.html
```

## Installation

### Prérequis
- Python 3.13 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone https://github.com/allouchesofiane/tournoi_echecs.git
cd tournoi_echecs
```

2. **Créer un environnement virtuel**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

## 💻 Utilisation

### Lancer l'application
```bash
python main.py
```

### Navigation dans les menus

#### Menu principal
```
1. Gestion des joueurs    → Ajouter, afficher, rechercher
2. Gestion des tournois   → Créer, gérer les tours, classements
3. Rapports              → Diverses vues
4. Quitter               → Fermer l'application
```

#### Workflow typique d'un tournoi

1. **Créer des joueurs** (minimum 2, idéalement nombre pair)
2. **Créer un tournoi** et sélectionner les participants
3. **Démarrer le premier tour** (appariement aléatoire)
4. **Saisir les résultats** des matchs
5. **Créer les tours suivants** (appariement par score)
6. **Consulter le classement final**

##  Structure des données

### Format Player (joueur)
```json
{
    "last_name": "dubois",
    "first_name": "bertrand",
    "date_of_birth": "03/03/2000",
    "national_id": "VB12547"
}
```

### Format Tournament (tournoi)
```json
{
    "name": "tournoi pour les amateurs",
    "location": "boulogne",
    "date": "05/11/2026",
    "rounds": 4,
    "time_control": "Blitz",
    "description": "un tournoi pour les amateurs",
    "players": [
        "DE12456",
        "FR25418",
        "GT12548",
        "SZ14527",
        "HY25413",
        "VB12547"
    ],
    "rounds_list": []
}
```

## Développement

### Standards de code
- **PEP 8** : Respect des conventions Python
- **Ligne maximale** : 119 caractères
- **Docstrings** : Pour toutes les classes et méthodes

### Architecture MVC
- **Modèles** : Aucune dépendance vers les vues
- **Vues** : Aucune logique métier
- **Contrôleurs** : Orchestration uniquement

## Qualité du code 

### Vérifier la conformité PEP8
```bash
# Générer le rapport HTML
flake8 . --format=html --htmldir=flake8_rapport

# Vérification dans le terminal
flake8 .
```

## Notes importantes

### Améliorations futures possibles
- Interface graphique 
- Base de données SQL

## 📄 Licence

Ce projet est développé dans le cadre d'une formation.
