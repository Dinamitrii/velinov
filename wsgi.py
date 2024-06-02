from waitress import serve
from dotenv import load_dotenv
from app import app

load_dotenv(override=True)


if __name__ == "__main__":
    serve(app.run(host="0.0.0.0", port=8000))
