from app import app
from models import db, User

db.drop_all()
db.create_all()

user1 = User.register(
    username="user1",
    password="password1",
    first_name='firstname1',
    last_name='lastname1',
    email='firstname1@gmail.com'
)

user2 = User.register(
    username="user2",
    password="password2",
    first_name='firstname2',
    last_name='lastname2',
    email='firstname2@gmail.com'
)

db.session.add_all([user1, user2])
db.session.commit()
