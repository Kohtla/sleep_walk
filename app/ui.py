class UI:
    game = None

    def pass_game_object(self, game_object):
        self.game = game_object

    def show(self):
        print('Press 1 to exit')
        choice = input()
        if choice == '1':
            self.game.exit()