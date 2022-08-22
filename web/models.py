
from . import db
from flask import current_app as app

class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    tags = db.Column(db.PickleType, nullable=True)
    
    def __repr__(self):
        return f"<Idea {self.title}>"

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telegram = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
