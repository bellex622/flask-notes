"""Models for Notes app."""
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)


class User(db.Model):
    """Create properties and method for cupcake"""

    __tablename__ = "users"

    username = db.Column(
        db.String(20),
        primary_key=True,
        nullable=False
    )

    password = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    first_name = db.Column(
        db.String(30),
        nullable=False
    )

    last_name = db.Column(
        db.String(30),
        nullable=False
    )

    def serialize(self):
        """Serialize to dictionary."""

        return {

        }

    @classmethod
    def register(cls, username, password, first_name, last_name, email):
        """Register user w/hashed password & return user."""
        hashed = bcrypt.generate_password_hash(password).decode('utf8')

        return cls(username=username,
                   password=hashed,
                   first_name=first_name,
                   last_name=last_name,
                   email=email)

    @classmethod
    def authenticate(cls, username, password):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        user = cls.query.filter_by(username=username).one_or_none()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False
