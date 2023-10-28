from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '346ee29615dfb34e9ba2cca22c377f00'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import routes

with app.app_context():
    database.create_all()

