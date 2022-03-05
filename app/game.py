class Game:
    is_running = True

    def __init__(self, ui):
        self.ui = ui
        self.ui.pass_game_object(self)

    def loop(self):
        while self.is_running:
            self.ui.show()

    def exit(self):
        self.is_running = False
