from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
##app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///courses.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from CourseEditor import views

from CourseEditor.courses import models
from CourseEditor.courses import views

from CourseEditor.plans import views

from CourseEditor.users import models
from CourseEditor.users import views

db.create_all()