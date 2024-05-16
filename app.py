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


if __name__ == "__main__":
    serve(app.run()) # type: ignore
