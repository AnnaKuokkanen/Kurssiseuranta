from CourseEditor import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(144), nullable=False)
    time = db.Column(db.String(144), nullable=False)

    course_user = db.relationship("Account", backref='course', lazy=True)

    def __init__(self, name, content, time):
        self.name = name
        self.content = content
        self.time = time