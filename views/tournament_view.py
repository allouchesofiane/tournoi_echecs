"""Vue pour la gestion des tournois."""


class TournamentView():
    """Gère l'affichage relatif aux tournois."""

    def display_tournament_menu(self):
        """Affiche le menu de gestion des tournois."""
        print("GESTION DES TOURNOIS")
        print("-" * 75)
        print("1- Créer un nouveau tournoi")
        print("2- Afficher tous les tournois")
        print("3- Démarrer le premier tour")
        print("4- Afficher les tours et matchs")
        print("5- Créer le tour suivant")
        print("6- Afficher le classement final")
        print("7- Retour au menu principal")
        print("-" * 75)

    def prompt_tournament_info(self):
        """
        Demande les informations pour créer un nouveau tournoi.
        """
        print("CRÉATION D'UN NOUVEAU TOURNOI")
        print("Veuillez entrer les informations du tournoi:\n")

        name = input("Nom du tournoi: ").strip()
        location = input("Lieu: ").strip()
        date = input("Date (JJ/MM/AAAA): ").strip()

        # Nombre de tours
        rounds_input = input("Nombre de tours (défaut: 4): ").strip()
        rounds = int(rounds_input) if rounds_input.isdigit() else 4

        # Contrôle du temps
        print("\n=== Choisissez le contrôle du temps ===")
        print("1. Bullet")
        print("2. Blitz (par défaut)")
        print("3. Coup rapide")

        # Saisie de l'utilisateur
        time_choice = input("Votre choix (1-3, défaut: 2) : ")

        # Traitement du choix
        time_controls = ["Bullet", "Blitz", "Coup rapide"]

        if time_choice.isdigit() and 1 <= int(time_choice) <= 3:
            time_control = time_controls[int(time_choice) - 1]
        else:
            time_control = "Blitz"

        print(f"Vous avez choisi : {time_control}")

        description = input("\nDescription: ").strip()

        return {
            "name": name,
            "location": location,
            "date": date,
            "rounds": rounds,
            "time_control": time_control,
            "description": description
        }

    def display_tournament_created(self, tournament):
        """
        Confirme la création d'un tournoi.
        """
        print(f"Tournoi '{tournament.name}' créé avec succès!")

    def display_tournaments_list(self, tournaments):
        """
        Affiche la liste des tournois.
        """
        print("LISTE DES TOURNOIS")

        if not tournaments:
            print("Aucun tournoi enregistré.")
            return
        # En-tête du tableau
        print(f"\n{'N°'} {'Nom'} {'Lieu'} {'Date'} {'Tours'} {'Joueurs'} {'Statut'}")
        print("-" * 100)

        # Affichage des tournois
        for idx, tournament in enumerate(tournaments, 1):
            tours_joues = len(tournament.rounds_list)
            nb_joueurs = len(tournament.players)
            statut = "Terminé" if tournament.is_finished() else f"{tours_joues}/{tournament.rounds}"

            print(f"{idx} {tournament.name} {tournament.location} "
                  f"{tournament.date} {tournament.rounds} {nb_joueurs} {statut}")

        print(f"\nTotal: {len(tournaments)} tournoi(s)")

    def select_tournament(self, tournaments):
        """
        Permet de sélectionner un tournoi dans une liste.
        """
        if not tournaments:
            print("Aucun tournoi disponible.")
            return None

        self.display_tournaments_list(tournaments)

        choice = input("\nSélectionnez un tournoi (numéro)")

        if choice.isdigit() and 1 <= int(choice) <= len(tournaments):
            return tournaments[int(choice) - 1]

        print("Choix invalide.")
        return None

    def display_player_selection(self, players):
        """
        Affiche les joueurs disponibles pour la sélection.
        """
        print("SÉLECTION DES JOUEURS")

        if not players:
            print("Aucun joueur disponible. Veuillez d'abord ajouter des joueurs.")
            return None

        print("\nJoueurs disponibles:")
        print("-" * 100)

        for idx, player in enumerate(players, 1):
            print(f"{idx}. {player.get_full_name()} ({player.national_id})")

        print("\nEntrez les numéros des joueurs à inscrire au tournoi")
        print("(ex: 1,3,5,7 pour sélectionner les joueurs 1, 3, 5 et 7)")
        print("Minimum: 2 joueurs")

        selection = input("\nVotre sélection")
        return selection

    def display_not_enough_players(self):
        """Affiche un message d'erreur pour nombre insuffisant de joueurs."""
        print("Vous devez sélectionner au moins 2 joueurs pour créer un tournoi")

    def display_odd_number_warning(self, count):
        """
        Avertit si le nombre de joueurs est impair.
        """
        print(f"Attention: {count} joueurs sélectionnés (nombre impair).Un joueur sera exempt à chaque tour.")

    def display_tournament_details(self, tournament):
        """
        Affiche les détails d'un tournoi.
        """
        print(f"DÉTAILS DU TOURNOI - {tournament.name.upper()}")
        print(f"\nLieu: {tournament.location}")
        print(f"Date: {tournament.date}")
        print(f"Contrôle du temps: {tournament.time_control}")
        print(f"Tours: {len(tournament.rounds_list)}/{tournament.rounds}")
        print(f"Nombre de joueurs: {len(tournament.players)}")

        if tournament.description:
            print(f"\nDescription: {tournament.description}")
        if tournament.is_finished():
            print("Tournoi terminé")
        elif not tournament.rounds_list:
            print("Tournoi non commencé")
        else:
            print(f"Tour actuel: {tournament.current_round}")
