from datetime import datetime
from enum import unique
from peewee import AutoField, CharField, ForeignKeyField, IntegerField, DateTimeField
from .level import Level
from .base_model import BaseModel


class Person(BaseModel):
    id = AutoField()
    name = CharField(unique=True)
    level = ForeignKeyField(Level, null=True)
    cash = IntegerField()
    score = IntegerField()
    date_created = DateTimeField()
    date_updated = DateTimeField(default=datetime.now())
