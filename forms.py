from typing import Optional
from flask_wtf import FlaskForm
from wtforms import StringField, TextField
from wtforms.fields.core import BooleanField, IntegerField
from wtforms.validators import AnyOf, NumberRange, Optional, URL


class AddPet(FlaskForm):

    name = StringField('Pet Name')

    species = StringField(
        'Species', validators=[AnyOf(values=['dog', 'cat', 'porcupine'], message='Enter Valid Species')])

    age = IntegerField('Age', validators=[NumberRange(
        min=0, max=30, message='Age must be between 0-30')])

    photo_url = StringField('Photo URL', validators=[URL(), Optional()])

    notes = TextField('Notes')


class EditPet(FlaskForm):

    photo_url = StringField('Photo URL', validators=[URL(), Optional()])

    notes = StringField('Notes')

    available = BooleanField('Available?')
