class UI:
    game = None
    level = 1
    is_pause_menu = False
    is_main_menu = True

    def pass_game_object(self, game_object):
        self.game = game_object

    def show(self):
        if self.is_main_menu:
            self._show_main_menu()
        elif self.is_pause_menu:
            self._show_pause_menu()
        else:
            self._show_level()

    def _show_level(self):
        print('------------------------------')
        print('It is level %i' % (self.level))
        print('1 - NEXT LEVEL')
        print('2 - PAUSE')
        print('------------------------------')
        choice = input()
        match choice:
            case '1':
                self.next_level()                
            case '2':                
                self.is_pause_menu = True
                self.is_main_menu = False
            case _:
                pass

    def _show_main_menu(self):
        print('SLEEP WALK v 0.1')
        print('1 - START')
        print('2 - EXIT')
        choice = input()
        match choice:
            case '1':
                self.is_main_menu = False
                self.is_pause_menu = False
            case '2':
                self.game.exit()

    def _show_pause_menu(self):
        print('Pause')
        print('1 - RESUME')
        print('2 - EXIT')
        choice = input()
        match choice:
            case '1':
                self.is_main_menu = False
                self.is_pause_menu = False
            case '2':
                self.game.exit()

    def next_level(self):
        self.level += 1
