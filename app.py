from flask import Flask, render_template, url_for
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


@app.route("/napkins/")
def napkins():
    return render_template("napkins.html")


# The code below lets the Flask server respond to browser requests for a favicon
@app.route("/favicon.ico")
def favicon():
    return url_for('static', filename='images/favicon/favicon.ico')


@app.route("/rollstp/")
def kitchen_rolls_tp():
    return render_template('rollstp.html')


if __name__ == "__main__":
    serve(app.run(host="0.0.0.0", port=8000))
