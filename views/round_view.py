"""Vue pour la gestion des tours et matchs."""
from datetime import datetime


class RoundView:
    """Gère l'affichage relatif aux tours et matchs."""

    def display_round_creation(self, round_name, matches):
        """
        Affiche les informations lors de la création d'un tour.
        """
        print(f"CRÉATION DU {round_name.upper()}")
        print(f"\nNombre de matchs: {len(matches)}")
        print(f"Heure de début: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print("-" * 40)
        print("\nAppariements:")
        print("-" * 40)

        for idx, match in enumerate(matches, 1):
            if match.player_2 is None:
                print(f"Match {idx}: {match.player_1} est exempté (1 point)")
            else:
                print(f"Match {idx}: {match.player_1} vs {match.player_2}")

    def display_current_standings(self, standings):
        """
        Affiche le classement actuel.
        """
        print("\nClassement actuel:")
        print("-" * 40)

        print(f"{'Rang '} {'Joueur '} {'Points '}")
        print("-" * 40)

        for rank, (player_id, score) in enumerate(standings, 1):
            print(f"{rank} {player_id} {score:}")

    def get_match_result(self, match):
        """
        Demande le résultat d'un match.
        """
        if match.player_2 is None:
            print(f"{match.player_1} est exempté. Aucun score à saisir.")
            return 1.0, 0.0
        print(f"\n{match}")
        print("\nRésultat du match:")
        print("1. Victoire de", match.player_1)
        print("2. Victoire de", match.player_2)
        print("3. Match nul")

        choice = input("Votre choix (1/2/3) : ")

        if choice == "1":
            return 1.0, 0.0
        elif choice == "2":
            return 0.0, 1.0
        elif choice == "3":
            return 0.5, 0.5
        else:
            print("Choix invalide.")
            return None

    def display_score_entry_header(self, round_name):
        """
        Affiche l'en-tête pour la saisie des scores.
        """
        print(f"SAISIE DES RÉSULTATS - {round_name.upper()}")
        print("\nEntrez les résultats de chaque match:")
        print("-" * 40)

    def display_round_completed(self, round_name):
        """
        Confirme que le tour est terminé.
        """
        print(f"{round_name} terminé et enregistré avec succès!")
        print(f" Heure de fin: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    def display_rounds_list(self, tournament_name, rounds_list):
        """
        Affiche la liste des tours d'un tournoi.
        """
        print(f"TOURS DU TOURNOI - {tournament_name.upper()}")

        if not rounds_list:
            print("Aucun tour n'a été joué dans ce tournoi.")
            return

        for round_data in rounds_list:
            print(f"\n{round_data['name']}")
            print("-" * 40)

            start_time = round_data.get('start_time', 'N/A')
            end_time = round_data.get('end_time', 'En cours')

            print(f"Début: {start_time}")
            print(f"Fin: {end_time}")

            if round_data.get('matchs'):
                print("\nMatchs:")
                for match in round_data['matchs']:
                    try:
                        p1, s1 = match[0]
                        p2, s2 = match[1]

                        # Déterminer le résultat
                        if s1 > s2:
                            result = f" Victoire de {p1}"
                        elif s2 > s1:
                            result = f" Victoire de {p2}"
                        else:
                            result = "= Match nul"

                        if p2 == "EXEMPT":
                            print(f"• {p1} est exempté (1 point)")
                        else:
                            print(f"• {p1} ({s1}) vs {p2} ({s2}) - {result}")
                    except Exception:
                        print("• Erreur d'affichage du match")
            else:
                print("\nAucun match dans ce tour.")

    def display_no_tournament_started(self):
        """Affiche un message quand aucun tournoi n'a commencé."""
        print("Ce tournoi n'a pas encore commencé. Créez d'abord le premier tour.")

    def display_tournament_finished(self):
        """Affiche un message quand le tournoi est terminé."""
        print("Ce tournoi est terminé. Tous les tours ont été joués.",)

    def display_pairing_conflict(self, player1, player2):
        """
        Affiche un avertissement pour un match déjà joué.
        """
        print(f"Attention: {player1} et {player2} se sont déjà rencontrés dans ce tournoi.")

    def display_invalid_scores(self):
        """Affiche un message d'erreur pour des scores invalides."""
        print("Scores invalides. Utilisez: 1-0 (victoire J1), 0-1 (victoire J2) ou 0.5-0.5 (nul)")

    def display_no_valid_pairings(self):
        """Affiche un message quand aucun appariement n'est possible."""
        print("Tous les joueurs se sont déjà rencontrés.")

    def confirm_round_start(self):
        """
        Demande confirmation avant de démarrer un tour.
        """
        response = input("\nVoulez-vous démarrer ce tour? (O/N)").upper()
        return response == 'O'
