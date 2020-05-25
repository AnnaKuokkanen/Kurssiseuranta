from CourseEditor import db
from CourseEditor.usercourse import models

class Course(db.Model):

    __tablename__ = "course"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(144), nullable=False)
    time = db.Column(db.String(144), nullable=False)

    #accounts = db.relationship("User", secondary=account_course, backref='course')


    def __init__(self, name, content, time):
        self.name = name
        self.content = content
        self.time = time
