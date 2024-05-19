from flask import Flask, render_template
from waitress import serve
from dotenv import load_dotenv

load_dotenv(override=True)

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
@app.route("/index")

def index():
    return render_template("index.html")


@app.route("/contacts/")

def contacts():
    return render_template("contacts.html")


@app.route("/mosaic/")

def mosaic():
    return render_template("mosaic.html")

<<<<<<< HEAD
=======

>>>>>>> 0cb564ecf3975c5ed6baac3c90f01f4fdd97a3fe
@app.route("/napkins/")

def napkins():
    return render_template("napkins.html")

<<<<<<< HEAD

@app.route("/kitchen/")

def kitchen():
    return render_template("kitchen.html")

@app.route("/toipaper/")

def toipaper():
    return render_template("toipaper.html")


=======
>>>>>>> 0cb564ecf3975c5ed6baac3c90f01f4fdd97a3fe
if __name__ == "__main__":
    serve(app.run()) # type: ignore
