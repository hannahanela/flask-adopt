"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_URL = "https://www.shutterstock.com/image-vector/dog-outline-icon-pet-vector-illustration-1497500723"

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


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
        default=DEFAULT_IMG_URL
    )

    # select from ['baby', 'young', 'adult', 'senior']
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
