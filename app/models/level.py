from peewee import Model, IntegerField, TextField, CharField, CharField


class Level(Model):
    id = IntegerField(primary_key=True)
    text = TextField()
    name = CharField()
    language = CharField()
