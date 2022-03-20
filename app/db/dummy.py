from datetime import datetime
from .database import Database
from app.models import Person, level


class DummyDatabase(Database):
    def __init__(self):
        self.persons = {}

    def get_person(self, pk):
        return self.persons[pk]

    def get_latest_person(self):
        # just grabs first person from the database
        return self.persons.values()[0]

    def create_person(self, name):
        person = Person()
        person.name = name
        person.cash = 0
        person.date_created = datetime.now()
        person.score = 0
        self.persons[name] = person
        return person

    def update_person(self, person):
        self.persons[person.name] = person
        return person
