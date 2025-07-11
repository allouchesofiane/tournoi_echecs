import os
import datetime


class ClearScreen:
    """Efface l'écran du terminal (Windows, Mac, Linux)."""
    def __call__(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")


class MainDisplay:
    """Affiche le titre principal de l'application."""
    def display_title(self):
        print("================================================")
        print("========= Application de Tournoi d'Échecs =======")
        print("================================================")
        print("============== Menu Principal ==================")
        print("================================================")
        print("1. Gestion des joueurs")
        print("2. Gestion des tournois")
        print("3. Quitter")
        print("------------------------------------------------")


class InputView:
    """Permet d'afficher une question et de récupérer la saisie."""
    def get_input(self, message):
        return input(f"{message}\n--> ")


class MessageView:
    """Affiche un message simple à l'utilisateur."""
    def show_message(self, message):
        print(f"\n{message}\n")


class DateView:

    """Affiche l'heure de début et de fin d’un tour."""
    def display_tournament_time(self):
        input("Appuyez sur Entrée pour commencer le tour.")
        begin = datetime.datetime.now()
        print(f"Début : {begin}")
        input("Appuyez sur Entrée lorsque le tour est terminé.")
        end = datetime.datetime.now()
        print(f"Fin : {end}")
        return begin, end


class PlayerView:

    def get_player_info(self):
        """Demande à l'utilisateur de saisir les infos d'un joueur"""
        print("=== Création d'un nouveau joueur ===")
        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        date_of_birth = input("Date de naissance (jj/mm/aaaa) : ")
        national_id = input("Identifiant national d'échecs (ex: AB12345) : ")
        return {
            "last_name": last_name,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "national_id": national_id,
        }

    def confirm_player_added(self, player):
        print(f"\n✅ Joueur ajouté : {player.first_name} {player.last_name} (ID : {player.national_id})")

    def show_all_players(self, players):
        print("\n=== Liste des joueurs enregistrés ===")
        for player in players:
            print(f"- {player.first_name} {player.last_name} |"
                  f" Né(e) le {player.date_of_birth} | ID : {player.national_id}")


class DisplayTournamentView:

    def get_tournament_info(self):
        print("\n=== Création d'un nouveau tournoi ===")
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        date = input("Date (jj/mm/aaaa) : ")

        matchs = input("Nombre de matchs (défaut 4) : ")
        matchs = int(matchs) if matchs.isdigit() else 4

        print("Contrôle du temps :")
        print("1. Bullet")
        print("2. Blitz")
        print("3. Coup rapide")
        time_control_choice = input("Choix (1/2/3) : ")
        time_control = {
            "1": "Bullet",
            "2": "Blitz",
            "3": "Coup rapide"
        }.get(time_control_choice, "Blitz")

        description = input("Description (optionnel) : ")

        return {
            "name": name,
            "location": location,
            "date": date,
            "matchs": matchs,
            "time_control": time_control,
            "description": description
        }

    def confirm_tournament_created(self, tournament):
        print(f"\n✅ Le tournoi '{tournament.name}' a bien été créé et sauvegardé.")

    def show_all_tournaments(self, tournaments):
        print("\n=== Liste des tournois ===\n")
        if not tournaments:
            print("Aucun tournoi enregistré.")
            return

        for idx, tournament in enumerate(tournaments, 1):
            if isinstance(tournament, dict):
                name = tournament.get("name", "Inconnu")
                location = tournament.get("location", "Inconnu")
                date = tournament.get("date", "Inconnue")
                time_control = tournament.get("time_control", "Non défini")
            else:
                name = tournament.name
                location = tournament.location
                date = tournament.date
                time_control = tournament.time_control

            print(f"{idx}. {name} - {location} - {date} - {time_control}")
