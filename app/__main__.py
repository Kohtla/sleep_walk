from .game import Game
from .ui import UI


def main():
    print('Start game')
    # create and migrate database
    # run main loop and
    game = Game(UI())
    game.loop()

    print('Exit game')


if __name__ == "__main__":
    main()
