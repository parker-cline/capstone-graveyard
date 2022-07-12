
from . import db
from flask import current_app as app

class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(100), nullable=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"<Idea {self.title}>"


sammy = Idea(title="Sammy", description="Sammy is a cool guy.")
parker = Idea(title="Parker", description="Parker is a strange guy.")

db.create_all()

db.session.add(sammy)
db.session.add(parker)
db.session.commit()
