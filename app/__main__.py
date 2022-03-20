from app.db.dummy import DummyDatabase
from .game import Game
from .ui import UI
from .db.sqlite import SQLDatabase


def main():
    print('Start game')
    # create and migrate database
    db = DummyDatabase()
    # run main loop and
    game = Game(UI(), db)
    game.loop()

    print('Exit game')


if __name__ == "__main__":
    main()
