
from app.db import SQLDatabase
from app.models import Level, Line

import os


def init_story():
    db = SQLDatabase()
    Line.delete()
    Level.delete()

    db.create_person('Anna Maria Del Piero')

    level1 = db.create_level(Level(name='Welcome',
                                  text='Welcome boi',
                                  language='rus'))                                  

    line1 = Line(character='Kohtla',
                 text='This is the first line of that story',
                 level=level1,
                 language='rus')    
    db.create_line(line1)

    line2 = Line(character='Kohtla',
                 text='This is the second line',
                 level=level1,
                 language='rus',
                 prev_line=line1)
    line2 = db.create_line(line2)
    line1.next_line = line2
    line1.save()

    line3 = Line(character='Kohtla',
                 text='This is the third line',
                 level=level1,
                 language='rus',
                 prev_line=line2)
    line3 = db.create_line(line3)
    line2.next_line = line3
    line2.save()

    level2 = db.create_level(Level(name='Second level actually',
                                  text='You are fat fuck',
                                  prev_level = level1,
                                  language='rus'))
    level1.next_level = level2
    level1.save()

    line4 = Line(character='Kohtla',
                 text='This is the first and the last line of that level',
                 level=level2,
                 language='rus')    
    db.create_line(line4)

    line5 = Line(character='Kohtla',
                 text='This is the the last line, goodbye!',
                 level=level2,
                 language='rus',
                 prev_line=line4)    
    db.create_line(line5)
    line4.next_line = line5
    line4.save()