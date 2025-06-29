
class PlayerView :
    """On demande nécessaires à l'utilisateur et on confirme l'ajout de l'objet """

    print("Ajout d'un nouveau joueur")
    #demander les informations à l'utilisateur
    def prompt_new_player(self):
         
        last_name = input("Votre nom: ")
        first_name = input("Votre prénom: ")
        date_of_birth = input("Votre date de naissance: ")
        national_id = input("Votre identifiant national: ")
        return last_name, first_name, date_of_birth, national_id
    #On confirme l'ajout de l'objet
    def confirm_player_added(self, player) : 
        print(f"player ajouté {player}")