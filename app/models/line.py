from enum import unique
from xmlrpc.client import Boolean
from peewee import AutoField, TextField, CharField, ForeignKeyField, BooleanField
from .base_model import BaseModel
from .level import Level


class Line(BaseModel):
    uuid = CharField(primary_key=True) 
    level = ForeignKeyField(Level, backref='lines')
    character = CharField()
    text = TextField()
    language = CharField()
    prev_line = ForeignKeyField('self', null=True)
    next_line = ForeignKeyField('self', null=True)

    is_first = BooleanField(default=False)
    action = CharField(null=True)
