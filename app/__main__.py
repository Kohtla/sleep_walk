from .game import Game
from .ui import UI
from .database import Database


def main():
    print('Start game')
    # create and migrate database
    db = Database()
    db.migrate()
    # run main loop and
    game = Game(UI())
    game.loop()

    print('Exit game')


if __name__ == "__main__":
    main()
