from app import app
from models import db, Pet

db.drop_all()
db.create_all()

p1 = Pet(
    name='Gus',
    species='domestic shorthair',
    photo_url='',
    age='adult',
    notes='A very grumpy boy.',
    available=True,
)

p2 = Pet(
    name='Arlo',
    species='Canis familiaris',
    age='young',
    available=False,
)

db.session.add_all([p1, p2])
db.session.commit()
