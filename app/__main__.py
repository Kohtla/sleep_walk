from app.ui import GUI
from .game import Game
from .controller import Controller
from .db import SQLDatabase


def main():
    print('Start game')
    # create and migrate database
    db = SQLDatabase()
    # run main loop and
    game = Game(db)    
    ui = GUI(game)
    ui.run()

    print('Exit game')


if __name__ == "__main__":
    main()
