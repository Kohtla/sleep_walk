
from app.db import SQLDatabase
from app.models import Level, Line

import os


def init_story():    
    db = SQLDatabase()
    Line.delete()
    Level.delete()
    
    level = db.create_level(Level(name='Welcome',
                                  text='Welcome boi',
                                  language='rus'))
    
    db.create_line(Line(character='Kohtla',
                        text='This is the first line of that story',
                        level=level,
                        language='rus'))
