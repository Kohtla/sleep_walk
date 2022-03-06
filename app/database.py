from peewee import SqliteDatabase, Model

from app.models import Person, Level


class Database:
    def __init__(self):
        self.db = SqliteDatabase('sw.db')

    def migrate(self):
        self.db.connect()
        self.db.create_tables([Person, Level])
        self.db.close()


class BaseModel():
    class Meta:
        database = Database().db
