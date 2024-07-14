from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    avatar = db.Column(db.String(100), nullable=False)
    guide = db.Column(db.String(100), nullable=False)
    participants = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    dates = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Event {self.guide}>'
