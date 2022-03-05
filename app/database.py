from peewee import SqliteDatabase

from app.models import Person, Level


class Database:
    def __init__(self):
        self.db = SqliteDatabase('sw.db')
    
    def migrate(self):
        with self.db.connect():
            self.db.create_tables([Person, Level])
