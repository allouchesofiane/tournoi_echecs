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
            print(f"- {player.first_name} {player.last_name} | Né(e) le {player.date_of_birth} | ID : {player.national_id}")
        print()
