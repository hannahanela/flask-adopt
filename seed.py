from app import app
from models import db, Pet

db.drop_all()
db.create_all()

p1 = Pet(
    name='Gus',
    species='domestic shorthair',
    photo_url='https://www.petfoodindustry.com/ext/resources/Images-by-month-year/21_07/Russian-blue-cat.jpg?t=1627569905&width=700',
    age='adult',
    notes='A very grumpy boy.',
    available=True,
)

p2 = Pet(
    name='Arlo',
    species='Canis familiaris',
    photo_url='https://etc.usf.edu/clipart/70400/70421/70421_262_rg-240_o_sm.gif',
    age='young',
    available=False,
)

db.session.add_all([p1, p2])
db.session.commit()
