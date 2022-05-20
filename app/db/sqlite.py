from datetime import datetime
from peewee import SqliteDatabase
from app.db.database import Database
from app.models import Person, Level, Line, Choice


class SQLDatabase(Database):
    def __init__(self):
        self.db = SqliteDatabase('sw.db')
        self.migrate()

    def migrate(self):
        self.db.connect()
        self.db.create_tables([Person, Level, Line, Choice])
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
        person = Person(name=name, cash=0,
                        date_created=datetime.now(), score=0)
        person.save()
        return person

    def update_person(self, person):
        person.save()
        return person

    # level
    def create_level(self, level):
        level.save()
        return level

    def get_level(self, pk):
        pass

    def get_first_level(self):
        return Level.get(Level.prev_level.is_null(True))

    # line
    def create_line(self, line):
        try:
            line.save(force_insert=True)
            return line
        except Exception:
            return None

    def get_line(self, pk):
        return Line.get(Line.uuid == pk)

    def get_lines(self, pks):
        return Line.select().where(Line.uuid.in_(pks))

    def get_first_line(self, level):
        return Line.get((Line.level == level) & Line.is_first)

    def add_choices(self, line, choices):
        for choice in choices:
            Choice(line=line, choice=choice).save()

    def get_choices(self, line):
        return Line.select().join(Choice).where(Choice.line == line)
