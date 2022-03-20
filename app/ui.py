class UI:
    game = None
    level = 1    

    def pass_game_object(self, game_object):
        self.game = game_object

    def show(self):
        if self.game.is_main_menu:
            self._main_menu()
        elif self.game.is_pause_menu:
            self._pause_menu()
        elif self.game.is_create_person_menu:
            self._create_person_menu()
        else:
            self._level()

    def _level(self):
        print('------------------------------')
        print('It is level %i for %s' % (self.level, self.game.person.name))
        print('1 - NEXT LEVEL')
        print('2 - PAUSE')
        print('------------------------------')
        choice = input()
        match choice:
            case '1':
                self.next_level()                
            case '2':                
                self.game.pause()
            case _:
                pass

    def _main_menu(self):
        print('SLEEP WALK v 0.1')
        print('1 - NEW GAME')
        print('2 - CONTINUE')
        print('3 - LOAD GAME')
        print('4 - EXIT')
        choice = input()
        match choice:
            case '1':
                self.game.start_new_game()
            case '2':
                print('not implemented')
            case '3':
                print('not implemented')
            case '4':
                self.game.exit()

    def _pause_menu(self):
        print('Pause')
        print('1 - RESUME')
        print('2 - MAIN MENU')
        print('3 - EXIT')
        choice = input()
        match choice:
            case '1':
                self.game.unpause()
            case '2':
                self.game.open_main_menu()
            case '2':
                self.game.exit()

    def next_level(self):
        self.level += 1

    def _create_person_menu(self):
        print('Creating new person...')
        name = input('Name:')
        self.game.create_person(name)
        print()


