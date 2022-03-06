from datetime import datetime
from peewee import CharField, ForeignKeyField, IntegerField, BooleanField, DateTimeField
from .level import Level
from .base_model import BaseModel


class Person(BaseModel):
    name = CharField()
    level = ForeignKeyField(Level)
    cash = IntegerField()
    score = IntegerField()
    is_main = BooleanField()
    date_created = DateTimeField()
    date_updated = DateTimeField(default=datetime.now())
