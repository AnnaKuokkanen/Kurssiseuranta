# Flask-sovellus
from flask import Flask
app = Flask(__name__)

# Tietokanta
from flask_sqlalchemy import SQLAlchemy
import os 

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///courses.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# Oma sovellus
from CourseEditor import views

from CourseEditor.courses import models
from CourseEditor.courses import views

from CourseEditor.plans import views

from CourseEditor.users import models
from CourseEditor.users import views

from CourseEditor.usercourse import models

# Kirjautuminen 
from CourseEditor.users.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "users_login_form"
login_manager.login_message = "Kirjaudu sisään, ole hyvä"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
except:
    pass