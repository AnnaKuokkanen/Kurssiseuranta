from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///courses.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from CourseEditor import views

from CourseEditor.users import models

db.create_all()