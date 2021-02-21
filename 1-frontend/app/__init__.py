from flask import Flask
from os import getenv

app = Flask(__name__,template_folder='../templates')
app.config['SECRET_KEY'] = "getenv('SECRET')"

from app import routes
