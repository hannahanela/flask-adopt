"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField(
        "Pet name",
        validators=[
            InputRequired(),
            Length(max=50, message='Name must be less than %(max)d characters.')
        ],
    )

    species = SelectField(
        "Pet species",
        choices=[
            ('cat', 'Cat'),
            ('dog', 'Dog'),
            ('porcupine', 'Porcupine'),
        ],
        validators=[
            InputRequired(),
        ],
    )

    photo_url = StringField(
        "Photo of pet",
        validators=[
            Optional(),
            URL(),
        ],
    )

    age = SelectField(
        "Pet Age",
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior'),
        ],
        validators=[
            InputRequired(),
        ],
    )
    
    notes = TextAreaField(
        "Notes",
        validators=[
            Optional(),
        ],
    )


class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField(
        "Photo of pet",
        validators=[
            Optional(),
            URL(),
        ],
    )

    notes = TextAreaField(
        "Notes",
        validators=[
            Optional(),
        ],
    )

    available = BooleanField(
        "Availability",
        validators=[
            Optional(),
        ],
    )
