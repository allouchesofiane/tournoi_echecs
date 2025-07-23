"""Vue pour l'affichage des rapports."""


class ReportView:
    """Gère l'affichage des rapports."""

    def display_report_menu(self):
        """Affiche le menu des rapports."""
        print("MENU RAPPORTS")
        print("1- Liste de tous les joueurs (ordre alphabétique)")
        print("2- Liste de tous les tournois")
        print("3- Détails d'un tournoi spécifique")
        print("4- Classement d'un tournoi")
        print("5- Retour au menu principal")

    def display_players_report(self, players):
        """
        Affiche la liste de joueurs.
        """
        print("RAPPORT - LISTE DES JOUEURS")
        print("(Tri par ordre alphabétique)\n")

        if not players:
            print("Aucun joueur enregistré dans la base de données.")
            return
        # Tri alphabétique
        sorted_players = sorted(players, key=lambda p: (p.last_name.lower(), p.first_name.lower()))
        # En-tête
        print(f"{'N° '} {'Nom complet '} {'Date de naissance '} {'ID National '}")
        print("=" * 75)
        # Affichage
        for idx, player in enumerate(sorted_players, 1):
            full_name = f"{player.last_name.upper()}, {player.first_name}"
            print(f"{idx} {full_name} {player.date_of_birth} {player.national_id}")
        print(f"- Total des joueurs: {len(players)}")

    def display_tournaments_report(self, tournaments):
        """
        Affiche la liste des tournois.
        """
        print("RAPPORT - LISTE DES TOURNOIS")
        if not tournaments:
            print("Aucun tournoi enregistré dans la base de données.")
            return
        # Statistiques
        total = len(tournaments)
        print(f"- Total des tournois: {total}")
        print("*" * 75)
        # Liste détaillée
        for idx, tournament in enumerate(tournaments, 1):
            print(f"\n{idx}. {tournament.name}")
            print(f"Lieu: {tournament.location}")
            print(f"Date: {tournament.date}")
            print(f"Type: {tournament.time_control}")
            print(f"Joueurs: {len(tournament.players)}")
            status = "Terminé" if tournament.is_finished() else "En cours"
            print(f"Statut: {status}")

    def display_tournament_detail_report(self, tournament, players_dict):
        """
        Affiche le rapport détaillé d'un tournoi.
        """
        print(f"RAPPORT DÉTAILLÉ - {tournament.name.upper()}")

        # Informations générales
        print("\n INFORMATIONS GÉNÉRALES")
        print("-" * 40)
        print(f"Lieu: {tournament.location}")
        print(f"Date: {tournament.date}")
        print(f"Contrôle du temps: {tournament.time_control}")
        print(f"Nombre de tours: {tournament.rounds}")
        print(f"Tours joués: {len(tournament.rounds_list)}")

        if tournament.description:
            print(f"\nDescription: {tournament.description}")
        else:
            print("pase de description")
        # Liste des joueurs inscrits
        print("\n\n JOUEURS INSCRITS")
        print("-" * 40)

        tournament_players = []
        for pid in tournament.players:
            if pid in players_dict:
                tournament_players.append(players_dict[pid])

        # Tri alphabétique
        tournament_players.sort(key=lambda p: (p.last_name.lower(), p.first_name.lower()))

        for idx, player in enumerate(tournament_players, 1):
            print(f"{idx}. {player.get_full_name()} ({player.national_id})")

        # Détail des tours
        if tournament.rounds_list:
            print("\n\n DÉTAIL DES TOURS")
            print("-" * 40)

            for round_data in tournament.rounds_list:
                print(f"\n{round_data['name']}")
                print(f"Début: {round_data.get('start_time', 'N/A')}")
                print(f"Fin: {round_data.get('end_time', 'N/A')}")

                if round_data.get('matchs'):
                    print("\nMatchs:")
                    for match in round_data['matchs']:
                        p1, s1 = match[0]
                        p2, s2 = match[1]

                        # Récupérer les noms des joueurs
                        name1 = players_dict[p1].get_full_name() if p1 in players_dict else p1
                        name2 = players_dict[p2].get_full_name() if p2 in players_dict else p2

                        print(f"• {name1} ({s1}) vs {name2} ({s2})")

    def display_ranking_report(self, tournament_name, rankings):
        """
        Affiche le classement d'un tournoi.
        Args:
            tournament_name (str): Nom du tournoi
            rankings (list): Liste des tuples (nom_joueur, score)
        """
        print(f"CLASSEMENT - {tournament_name.upper()}")

        if not rankings:
            print("Aucun match n'a été joué dans ce tournoi.")
            return

        print(f"\n{'Rang '} {'Joueur '} {'Points '}")
        print("=" * 60)

        for rank, (player_name, score) in enumerate(rankings, 1):
            print(f"{rank} {player_name} {score}")

        print("-" * 40)
        print(f"\nTotal des participants: {len(rankings)}")
