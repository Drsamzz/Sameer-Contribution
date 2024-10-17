from .users import create_user
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'boy', 'email@email.com','bobboy', 'bobpass')
