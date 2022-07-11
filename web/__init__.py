from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html', ideas=["Do the thing.", "Do the other thing."])