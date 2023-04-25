from flask import Flask
from os import path

def fourthStreet():
    fourthStreet = Flask(__name__)
    from .models.auth import auth
    # from .models.marketplace import marketplace
    # fourthStreet.register_blueprint(marketplace, url_prefix = "/")
    fourthStreet.register_blueprint(auth, url_prefix = "/")
    return fourthStreet
