"""Flask app for adopt app."""

from flask import Flask, url_for, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = "secret"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.get('/')
def homepage_index():
    """Show list of pets as homepage."""
    pets = Pet.query.all()

    return render_template('pets/list.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Pet add form; handle creating a new pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        photo_url = photo_url if photo_url else None

        pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=photo_url,
            age=form.age.data,
            notes=form.notes.data,
        )

        db.session.add(pet)
        db.session.commit()

        # TODO: add flash message here
        return redirect('/')

    else:
        return render_template('pets/add.html', form=form)