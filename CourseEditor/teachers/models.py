from CourseEditor import db
from CourseEditor.models import Base

class Teacher(Base):
    __tablename__ = "teacher"

    courses = db.relationship("Course", cascade='all, delete-orphan', backref='teacher', single_parent=True, lazy=True)

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname 