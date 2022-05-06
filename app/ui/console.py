
from app.init_story import init_story

class Console:
    
    def main_menu(self, game):         
        print('SLEEP WALK v 0.1')
        print('1 - NEW GAME')
        print('2 - CONTINUE')
        print('3 - LOAD GAME')
        print('4 - EXIT')
        print('5 - init story')
        choice = input()
        match choice:
            case '1':
                game.open_create_person_menu()
            case '2':
                game.start(game.get_latest_person())
            case '3':
                game.open_load_menu()
            case '4':
                game.exit()
            case '5':
                init_story()
    
    def pause_menu(self, game):
        print('Pause')
        print('1 - RESUME')
        print('2 - MAIN MENU')
        print('3 - EXIT')
        choice = input()
        match choice:
            case '1':
                game.unpause()
            case '2':
                game.open_main_menu()
            case '3':
                game.exit()

    def create_person_menu(self, game):
        print('Creating new person...')
        name = input('Name:')
        game.create_person(name)
        print()
    
    def load_person_menu(self, game):
        print('Choose person to play...')
        n = 1
        persons = {}
        for p in game.list_persons():
            print('%i - %s - %i' % (n, p.name, p.cash))
            persons[str(n)] = p
            n += 1
        choice = input('Load #:')
        game.start(persons[choice])
    
    def show_titles(self, game):
        print('This is the end, my friend')
        print('')
        print('Designed and developed by Kohtla')
        print('')
        print('1 - return to main menu')
        choice = input()
        match choice:
            case '1':
                game.close_titles()
    
    def show_level(self, game):
        print('------------------------------')
        print('It is level %s for %s' %
              (game.level.name, game.person.name))
        print('%s: %s' % (game.line.character, game.line.text))
        i = 1
        choices = {}
        for choice in game.get_choices():
            print('%i - %s' % (i, choice.text))
            choices[str(i)] = choice
            i += 1
        if not choices:
            print('next - NEXT LINE')
        print('0 - PAUSE')
        print('------------------------------')
        choice = input()
        if choice == '0':
            game.pause()
        elif choice == 'next':
            game.next_level()
        else:
            game.make_choice(choices[choice])
    
    