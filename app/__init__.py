from flask import Flask
from dotenv import load_dotenv
from os import environ


app = Flask(__name__)

def create_app():
    load_dotenv()

    app.config["DEBUG"] = (environ.get("DEBUG") == "True")
    app.config["ENV"] = environ.get("ENV")

    from .controller import controller

    app.register_blueprint(controller,url_prefix="/")

    return app