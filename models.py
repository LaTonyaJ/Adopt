from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Default_img = 'https: // encrypted-tbn0.gstatic.com/images?q = tbn: ANd9GcR5YRqVSAoSLhejfBw4jZsMvYk8NBIAybMPxQ & usqp = CAU'


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Create a Pet"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text, nullable=True, default=Default_img)

    age = db.Column(db.Integer, nullable=False)

    notes = db.Column(db.Text, nullable=True)

    available = db.Column(db.Boolean, nullable=False, default=True)
