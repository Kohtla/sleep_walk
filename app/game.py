from app.db.database import Database
from app.models.person import Person


class Game:
    is_running = True
    db = Database()
    person = None
    level = None
    line = None

    is_pause_menu = False
    is_main_menu = True
    is_create_person_menu = False
    is_load_person_menu = False
    is_titles = False

    def __init__(self, ui, db):
        self.ui = ui
        self.db = db
        self.ui.pass_game_object(self)

    # main game loop
    def loop(self):
        while self.is_running:
            self.ui.show()

    # game control functions
    def exit(self):
        self.is_running = False

    def start(self, person):
        self.person = person
        if not person.level:
            person.level = self.db.get_first_level()
            person.save()
        self.level = person.level
        self.start_level()
        self.is_load_person_menu = False
        self.is_main_menu = False
    
    def start_level(self):
        self.line = self.db.get_first_line(self.level)
    
    def next_line(self):
        if self.line.next_line:
            self.line = self.line.next_line
        else:
            self.next_level()
    
    def next_level(self):
        if self.level.next_level:
            self.level = self.level.next_level
            self.person.level = self.level
            self.start_level()
            self.update_person(self.person)
        else:
            self.end_game()

    def end_game(self):
        self.open_titles()

    # ui state functions
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
    
    def open_create_person_menu(self):
        self.is_create_person_menu = True
        self.is_main_menu = False
        self.is_pause_menu = False
    
    def open_titles(self):
        self.is_titles = True
    
    def close_titles(self):
        self.is_titles = False
        self.is_main_menu = True

    # data manipulating commands
    def get_person(self, pk):
        return self.db.get_person(pk)

    def get_latest_person(self):
        return self.db.get_latest_person()

    def list_persons(self):
        return self.db.list_persons()

    def create_person(self, name):
        person = self.db.create_person(name)
        self.start(person)
        self.is_create_person_menu = False
    
    def update_person(self, person):
        self.person = self.db.update_person(person)
