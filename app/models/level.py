from peewee import IntegerField, TextField, CharField, CharField
from .base_model import BaseModel


class Level(BaseModel):
    id = IntegerField(primary_key=True)
    text = TextField()
    name = CharField()
    language = CharField()
