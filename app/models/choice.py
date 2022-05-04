from peewee import ForeignKeyField
from .base_model import BaseModel
from .line import Line


class Choice(BaseModel):
    line = ForeignKeyField(Line, null=True)
    choice = ForeignKeyField(Line, null=True)