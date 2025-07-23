"""Vue pour la gestion des joueurs."""


class PlayerView:
    """Gère l'affichage relatif aux joueurs."""

    def display_player_menu(self):
        """Affiche le menu de gestion des joueurs."""
        print()
        print("GESTION DES JOUEURS")
        print("*" * 75)
        print("1- Ajouter un nouveau joueur")
        print("2- Afficher tous les joueurs")
        print("3- Rechercher un joueur")
        print("4- Retour au menu principal")

    def prompt_new_player(self):
        """
        Demande les informations pour créer un nouveau joueur.

        Returns:
            tuple: (last_name, first_name, date_of_birth, national_id)
        """
        print()
        print("CRÉATION D'UN NOUVEAU JOUEUR")
        print("Veuillez entrer les informations du joueur:\n")
        last_name = input("Nom de famille: ").strip()
        first_name = input("Prénom: ").strip()
        date_of_birth = input("Date de naissance (JJ/MM/AAAA): ").strip()
        national_id = input("Identifiant national d'échecs (ex: AB12345): ").strip()
        return last_name, first_name, date_of_birth, national_id

    def display_player_added(self, player):
        """
        Confirme l'ajout d'un joueur.
        """
        print(f"Joueur ajouté avec succès: {player.get_full_name()} (ID: {player.national_id})")

    def display_players_list(self, players):
        """
        Affiche la liste des joueurs.
        """
        print("Liste des joueurs")

        if not players:
            print("Aucun joueur enregistré.")
            return

        # Tri par ordre alphabétique (nom puis prénom)
        sorted_players = sorted(players, key=lambda p: (p.last_name.lower(), p.first_name.lower()))

        # Affichage des joueurs
        for idx, player in enumerate(sorted_players, 1):
            print(f"{idx} - {player.last_name} {player.first_name} "
                  f"{player.date_of_birth} {player.national_id}")

        print(f"\nTotal: {len(players)} joueur(s)")

    def get_search_query(self):
        """
        Demande l'id pour la recherche.
        """
        return input("Rechercher ID : ")

    def display_search_results(self, results):
        """
        Affiche Liste des joueurs trouvés.
        """
        if results:
            self.display_players_list(results)
        else:
            print("Aucun joueur trouvé.")
