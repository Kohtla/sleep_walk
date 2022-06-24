from .gui import GUI
from .state import State
from .db import SQLDatabase
from .settings import dev


def main():
    print('Start game')
    # create and migrate database
    db = SQLDatabase()
    # run main loop and
    state = State(db)
    ui = GUI(state, dev)
    ui.run()

    print('Exit game')


if __name__ == "__main__":
    main()
