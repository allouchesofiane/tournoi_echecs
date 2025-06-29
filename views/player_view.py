class PlayerView :
    print("Ajout d'un nouveau joueur")

    def prompt_new_player(self):
        #demander les informations à l'utilisateur 
        last_name = input("Votre nom: ")
        first_name = input("Votre prénom: ")
        date_of_birth = input("Votre date de naissance: ")
        national_id = input("Votre identifiant national: ")
        return last_name, first_name, date_of_birth, national_id