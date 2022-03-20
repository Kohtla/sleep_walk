from app.db.database import Database
from app.models.person import Person


class Game:
    is_running = True
    db = Database()
    person = None

    is_pause_menu = False
    is_main_menu = True
    is_create_person_menu = False

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
    
    # start new game
    def start_new_game(self):
        self.is_create_person_menu = True
        self.is_main_menu = False
        self.is_pause_menu = False
        
    def pause(self):
        self.is_pause_menu = True

    def unpause(self):
        self.is_pause_menu = False

    # data manipulating commands
    def get_person(self, pk):
        return self.db.get_person(pk)
    
    def get_latest_person(self):
        return self.db.get_latest_person()
    
    def create_person(self, name):
        self.person = self.db.create_person(name)
        self.is_create_person_menu = False
