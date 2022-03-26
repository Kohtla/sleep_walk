from datetime import datetime
from peewee import CharField, ForeignKeyField, IntegerField, DateTimeField
from .level import Level
from .base_model import BaseModel


class Person(BaseModel):
    name = CharField(primary_key=True)
    level = ForeignKeyField(Level, null=True)
    cash = IntegerField()
    score = IntegerField()
    date_created = DateTimeField()
    date_updated = DateTimeField(default=datetime.now())
