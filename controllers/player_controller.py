
from views.player_view import PlayerView
from models.players import Player


class PlayerController :

    def __init__(self):
        self.view =PlayerView()

    def add_player(self):
        last_name, first_name, birth_date, national_id = self.view.prompt_new_player()
        player = Player(last_name, first_name, birth_date, national_id)
      
    
    