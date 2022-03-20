from datetime import datetime
from peewee import CharField, ForeignKeyField, IntegerField, BooleanField, DateTimeField
from .level import Level
from .base_model import BaseModel


class Person(BaseModel):
    name = CharField()
    level = ForeignKeyField(Level)
    cash = IntegerField()
    score = IntegerField()
    date_created = DateTimeField()
    date_updated = DateTimeField(default=datetime.now())

    def __init__(self, name, cash, score, date_created):
        self.name = name
        self.cash = cash
        self.score = score
        self.date_created = date_created

