from app.db.database import Database
from app.models.person import Person


class Game:
    is_running = True
    db = Database()
    person = None

    def __init__(self, ui, db):
        self.ui = ui
        self.db = db
        self.ui.pass_game_object(self)

    # main game loop
    def loop(self):
        while self.is_running:
            self.ui.show()

    # exit game
    def exit(self):
        self.is_running = False
    
    def get_person(self, pk):
        return self.db.get_person(pk)
    
    def get_latest_person(self):
        return self.db.get_latest_person()
    
    def create_person(self, name):
        return self.db.create_person(name)
