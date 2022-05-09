from app.ui import Console
from app.ui import GUI


class Controller:
    game = None
    ui = None
    def pass_game_object(self, game_object):
        self.game = game_object
    
    def __init__(self, ui):
        self.ui = ui

    def show(self):      
        if self.game.is_main_menu:
            self._main_menu()
        elif self.game.is_pause_menu:
            self._pause_menu()
        elif self.game.is_create_person_menu:
            self._create_person_menu()
        elif self.game.is_load_person_menu:
            self._load_person_menu()
        elif self.game.is_titles:
            self._show_titles()
        else:
            self._level()

    def _level(self):
        self.ui.show_level(self.game)

    def _main_menu(self):
        self.ui.main_menu(self.game)        

    def _pause_menu(self):
        self.ui.pause_menu(self.game)

    def _create_person_menu(self):
        self.ui.create_person_menu(self.game)

    def _load_person_menu(self):
        self.ui.load_person_menu(self.game)

    def _show_titles(self):
        self.ui.show_titles(self.game)
