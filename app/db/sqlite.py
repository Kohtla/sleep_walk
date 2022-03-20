from peewee import SqliteDatabase
from app.db.database import Database
from app.models import Person, Level


class SQLDatabase(Database):
    def __init__(self):
        self.db = SqliteDatabase('sw.db')

    def migrate(self):
        self.db.connect()
        self.db.create_tables([Person, Level])
        self.db.close()
