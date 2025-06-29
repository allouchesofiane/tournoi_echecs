
class Player :
    """Classe representant un seul joueur d'echecs.
        Attributs :
            last_name (str) : Nom de famille du joueur.
            first_name (str) : Prénom du joueur.
            date_of_birth (str) : Date de naissance du joueur.
            national_id (str) : Identifiant national unique attribué par la fédération d'échecs.
    """
    def __init__(self, last_name, first_name, date_of_birth, national_id):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.national_id = national_id

    """Representation lisible de l'objet lors d'une impression avec la methode print"""
    def __str__(self):
        return f" le nom du joueur est {self.last_name} {self.first_name} et sa date de naissance est {self.date_of_birth} et son edentifiant est {self.national_id}"
    
    """Convertir l'objet player en dictionnaire """   
    def to_dict(self):
        """Return un dictionnaire contenant les donnees d'un joueur"""
        return {
            "last_name" : self.last_name,
            "first_name" : self.first_name,
            "date_of_birth" : self.date_of_birth,
            "national_id" : self.national_id
            }

