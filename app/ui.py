from app.init_story import init_story


class UI:
    game = None

    def pass_game_object(self, game_object):
        self.game = game_object

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
        print('------------------------------')
        print('It is level %s for %s' %
              (self.game.level.name, self.game.person.name))
        print('%s: %s' % (self.game.line.character, self.game.line.text))
        i = 1
        choices = {}
        for choice in self.game.get_choices():
            print('%i - %s' % (i, choice.text))
            choices[str(i)] = choice
            i += 1
        if not choices:
            print('next - NEXT LINE')
        print('0 - PAUSE')
        print('------------------------------')
        choice = input()
        if choice == '0':
            self.game.pause()
        elif choice == 'next':
            self.game.next_level()
        else:
            self.game.make_choice(choices[choice])

    def _main_menu(self):
        print('SLEEP WALK v 0.1')
        print('1 - NEW GAME')
        print('2 - CONTINUE')
        print('3 - LOAD GAME')
        print('4 - EXIT')
        print('5 - init story')
        choice = input()
        match choice:
            case '1':
                self.game.open_create_person_menu()
            case '2':
                self.game.start(self.game.get_latest_person())
            case '3':
                self.game.open_load_menu()
            case '4':
                self.game.exit()
            case '5':
                init_story()

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
            case '3':
                self.game.exit()

    def _create_person_menu(self):
        print('Creating new person...')
        name = input('Name:')
        self.game.create_person(name)
        print()

    def _load_person_menu(self):
        print('Choose person to play...')
        n = 1
        persons = {}
        for p in self.game.list_persons():
            print('%i - %s - %i' % (n, p.name, p.cash))
            persons[str(n)] = p
            n += 1
        choice = input('Load #:')
        self.game.start(persons[choice])

    def _show_titles(self):
        print('This is the end, my friend')
        print('')
        print('Designed and developed by Kohtla')
        print('')
        print('1 - return to main menu')
        choice = input()
        match choice:
            case '1':
                self.game.close_titles()
