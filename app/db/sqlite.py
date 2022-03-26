from datetime import datetime
from peewee import SqliteDatabase
from app.db.database import Database
from app.models import Person, Level


class SQLDatabase(Database):
    def __init__(self):
        self.db = SqliteDatabase('sw.db')
        self.migrate()

    def migrate(self):
        self.db.connect()
        self.db.create_tables([Person, Level])
        self.db.close()
    # person
    def get_person(self, pk):
        Person.get(Person.username == pk)
        return Person

    def get_latest_person(self):        
        return Person.select().order_by(Person.date_updated.desc()).get()

    def list_persons(self):
        return Person.select()

    def create_person(self, name):
        person = Person(name=name, cash=0, date_created=datetime.now(), score=0)
        person.save()
        return person

    def update_person(self, person):
        person.save()
        return person
    
    # level