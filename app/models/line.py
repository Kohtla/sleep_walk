from peewee import AutoField, TextField, CharField, ForeignKeyField
from .base_model import BaseModel
from .level import Level


class Line(BaseModel):
    id = AutoField()
    level = ForeignKeyField(Level, backref='lines')
    character = CharField()
    text = TextField()
    language = CharField()
    prev_line = ForeignKeyField('self', null=True)
    next_line = ForeignKeyField('self', null=True)
