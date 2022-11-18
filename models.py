"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_URL = "https://etc.usf.edu/clipart/70400/70421/70421_262_rg-240_o_sm.gif"


class Pet(db.Model):
    """Pet for adoption."""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(
        db.String(50),
        nullable=False,
    )

    species = db.Column(
        db.String(50),
        nullable=False,
    )

    photo_url = db.Column(
        db.String,
        nullable=False,
        default=DEFAULT_IMG_URL,
    )

    # select from ['baby', 'young', 'adult', 'senior']
    # wtform options / validation handle this
    age = db.Column(
        db.String,
        nullable=False,
    )

    notes = db.Column(
        db.Text,
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
    )


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
