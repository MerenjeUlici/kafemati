from flask import Flask, render_template

from random import randint

app = Flask(__name__)

@app.route("/")
def index():

    rq = randint(0,10000)
    return render_template('index.html', rq=rq)

@app.route("/our_story")
def our_story():

    rq = randint(0,10000)
    return render_template('our_story.html', rq=rq)

@app.route("/kafemati")
def kafemati():

    rq = randint(0,10000)
    return render_template('kafemati.html', rq=rq)
