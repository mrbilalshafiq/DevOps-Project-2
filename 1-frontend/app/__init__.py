from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='../templates')
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db:3306/db'
app.config['SECRET_KEY'] = "YOUR_KEY"

from app import routes
