from app.db.database import Database
from app.models.person import Person


class Game:
    is_running = True
    db = Database()
    person = None

    is_pause_menu = False
    is_main_menu = True
    is_create_person_menu = False
    is_load_person_menu = False

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

    def start(self, person):
        self.person = person
        self.is_load_person_menu = False
        self.is_main_menu = False

    def pause(self):
        self.is_pause_menu = True

    def unpause(self):
        self.is_pause_menu = False

    def open_main_menu(self):
        self.is_pause_menu = False
        self.is_main_menu = True

    def open_load_menu(self):
        self.is_main_menu = False
        self.is_load_person_menu = True

    # data manipulating commands
    def get_person(self, pk):
        return self.db.get_person(pk)

    def get_latest_person(self):
        return self.db.get_latest_person()

    def list_persons(self):
        return self.db.list_persons()

    def create_person(self, name):
        self.person = self.db.create_person(name)
        self.is_create_person_menu = False
