
from . import db
from flask import current_app as app

class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"<Idea {self.title}>"

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telegram = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    
class StudentIdea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    idea_id = db.Column(db.Integer, db.ForeignKey("ideas.id"))
    liked = db.Column(db.Boolean)
    students = db.relationship("Student", foreign_keys=student_id)
    ideas = db.relationship("Idea", foreign_keys=idea_id)
    
sammy = Idea(title="Sammy", description="Sammy is a cool guy.")
parker = Idea(title="Parker", description="Parker is a strange guy.")

db.drop_all()
db.create_all()

db.session.add(sammy)
db.session.add(parker)
db.session.commit()
