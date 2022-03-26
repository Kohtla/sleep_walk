from peewee import AutoField, TextField, CharField, ForeignKeyField
from .base_model import BaseModel
from .level import Level


class Line(BaseModel):
    id = AutoField()
    level = ForeignKeyField(Level, backref='lines')
    character = CharField()
    text = TextField()
    language = CharField()
    next_line = ForeignKeyField('self', backref='previous_line', null=True)
