from peewee import AutoField, TextField, CharField, ForeignKeyField
from .base_model import BaseModel


class Level(BaseModel):
    id = AutoField()
    next_level = ForeignKeyField('self', backref='previous_level', null=True)
    text = TextField()
    name = CharField()
    language = CharField()
