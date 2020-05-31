from CourseEditor import db

class Course(db.Model):

    __tablename__ = "course"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(144), nullable=False)
    time = db.Column(db.String(144), nullable=False)
    planned = db.Column(db.Boolean, nullable=False)
    completed = db.Column(db.Boolean, nullable=False)

    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)

    accounts = db.relationship("User", secondary='account_course', backref='course', lazy=True)

    def __init__(self, name, content, time, planned, completed):
        self.name = name
        self.content = content
        self.time = time
        self.planned = planned
        self.completed = completed