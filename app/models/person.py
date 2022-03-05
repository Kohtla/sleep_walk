from datetime import datetime
from peewee import Model, CharField, ForeignKeyField, IntegerField, BooleanField, DateTimeField
from .level import Level


class Person(Model):
    name = CharField()
    level = ForeignKeyField(Level)
    cash = IntegerField()
    score = IntegerField()
    is_main = BooleanField()
    date_created = DateTimeField()
    date_updated = DateTimeField(default=datetime.now())
