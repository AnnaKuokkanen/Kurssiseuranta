# Flask application
from flask import Flask
app = Flask(__name__)

# Database
from flask_sqlalchemy import SQLAlchemy
import os 

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///courses.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# Log in
from CourseEditor.users.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "users_login_form"
login_manager.login_message = "Kirjaudu sisään, ole hyvä"

# User roles
from functools import wraps

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)


# Application
from CourseEditor import views

from CourseEditor.courses import models, views

from CourseEditor.grades import views

from CourseEditor.plans import views

from CourseEditor.teachers import models

from CourseEditor.users import models, views
from CourseEditor.users.models import Role

from CourseEditor.usercourse import models

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
    r1 = Role(id =1, role = "USER")
    db.session().add(r1)

    r2 = Role(id = 2, role = "ADMIN")
    db.session.add(r2)

    db.session().commit()
except:
    pass