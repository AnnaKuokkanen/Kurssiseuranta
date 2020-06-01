from CourseEditor import db

class Teacher(db.Model):
    __tablename__ = "teacher"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(144), nullable=False)
    lastname = db.Column(db.String(144), nullable=False)

    courses = db.relationship("Course", cascade='all, delete-orphan', backref='course', single_parent=True, lazy=True)

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname 