from flask import render_template, redirect, url_for, flash, request, jsonify
from .models import Idea
from flask import current_app as app
from .forms import IdeaSubmitForm
from . import db 

@app.route("/", methods=["GET", "POST"])
def index():
    ideas_list = Idea.query.all()
    form = IdeaSubmitForm()
    if form.validate_on_submit():
        new_idea = Idea(title=form.title.data, description=form.description.data)
        db.session.add(new_idea)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("index.html", ideas=ideas_list, form=form)

import random
@app.route("/cards", methods=["GET", "POST"])
def cards():
    random_idea = random.choice(Idea.query.all())
    return render_template("cards.html", idea=random_idea)