from peewee import AutoField, TextField, CharField, ForeignKeyField
from .base_model import BaseModel


class Level(BaseModel):
    id = AutoField()
    prev_level = ForeignKeyField('self', null=True)
    next_level = ForeignKeyField('self', null=True)
    text = TextField()
    name = CharField()
    language = CharField()
