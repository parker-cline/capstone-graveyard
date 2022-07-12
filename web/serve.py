from flask import render_template, redirect, url_for, flash, request, jsonify
from .models import Idea
from flask import current_app as app


@app.route("/", methods=("GET", "POST"))
def index():
    ideas_list = Idea.query.all()
    return render_template("index.html", ideas=ideas_list)
