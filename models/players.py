class Player :
    """Classe representant un seul joueur d'echecs."""

    def __init__(self, last_name, first_name, date_of_birth, national_id):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.national_id = national_id
    
    def __str__(self):
        return f" le nom du joueur est {self.last_name} {self.first_name} et sa date de naissance est {self.date_of_birth} et son edentifiant est {self.national_id}"
        
    def to_dict(self):
        return {
            "last_name" : self.last_name,
            "first_name" : self.first_name,
            "date_of_birth" : self.date_of_birth,
            "national_id" : self.national_id
            }