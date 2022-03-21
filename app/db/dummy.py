from datetime import datetime
from .database import Database
from app.models import Person, level


class DummyDatabase(Database):
    def __init__(self):
        self.persons = {}
        self.create_person('Jinja')

    def get_person(self, pk):
        return self.persons[pk]

    def get_latest_person(self):
        # just grabs first person from the database
        return [p for p in self.persons.values()][0]

    def list_persons(self):
        return [p for p in self.persons.values()]

    def create_person(self, name):
        person = Person(name=name, cash=0, date_created=datetime.now, score=0)
        self.persons[name] = person
        return person

    def update_person(self, person):
        self.persons[person.name] = person
        return person
