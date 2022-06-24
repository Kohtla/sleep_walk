from .application import Application
from .game import Game
from .db import SQLDatabase
from .settings import dev

def main():
    print('Start game')
    # create and migrate database
    db = SQLDatabase()
    # run main loop and
    game = Game(db)
    ui = Application(game, dev)
    ui.run()

    print('Exit game')


if __name__ == "__main__":
    main()
