class Player:
    # Représente un joueur d'échecs avec ses informations personnelles.
    def __init__(self, last_name, first_name, date_of_birth, national_id):
        """
        Initialise un nouveau joueur avec les données fournies.
        Args:
            last_name (str): Nom de famille.
            first_name (str): Prénom.
            date_of_birth (str): Date de naissance (ex: "01/01/2000").
            national_id (str): Identifiant national ou unique du joueur.
        """
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.national_id = national_id

    def to_dict(self):
        # Convertit l'objet joueur en dictionnaire
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "national_id": self.national_id
        }

    def __str__(self):
        # Représentation lisible du joueur, utilisée quand on fait `print(joueur)`.
        return f"{self.last_name} {self.first_name} ({self.date_of_birth}) - ID: {self.national_id}"
