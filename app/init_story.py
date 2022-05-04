
from distutils.command.build_scripts import first_line_re
from app.db import SQLDatabase
from app.models import Level, Line, Choice

import os
import json


def init_story():
    db = SQLDatabase()
    Line.delete()
    Level.delete()

    db.create_person('Anna Maria Del Piero')
    data = None
    with open('stories/rus.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    lang = data.get('language')
    bonds = []
    next_lines = []

    for level in data.get('levels'):
        level_object = db.create_level(Level(name=level.get('name'),
                                             text=level.get('text'),
                                             language=lang))
        for line in level.get('lines'):

            line_object = Line(uuid=line.get('id'),
                               character=line.get('character'),
                               text=line.get('text'),
                               level=level_object,
                               language=lang,
                               is_first=bool(line.get('is_first')))
            db.create_line(line_object)
            if line.get('choices'):
                bonds.append((line_object.uuid,line.get('choices')))
            if line.get('next'):
                next_lines.append((line_object.uuid, line.get('next')))

            
    for line_id, choices_ids in bonds:
        line = db.get_line(line_id)
        choices = db.get_lines(choices_ids)
        db.add_choices(line, choices)

    for line_id, next_line_id in next_lines:
        line = db.get_line(line_id)
        next_line = db.get_line(next_line_id)
        line.next_line = next_line
        line.save()
