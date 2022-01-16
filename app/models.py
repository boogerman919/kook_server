from datetime import datetime
from sqlalchemy.sql.elements import Null
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    rides = db.relationship('Ride', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rides = db.relationship('Ride', backref='board', lazy='dynamic')

    def __repr__(self):
        return '<board {}>'.format(self.id)


class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
    start_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return '<Ride start time: {}>'.format(self.start_time)
