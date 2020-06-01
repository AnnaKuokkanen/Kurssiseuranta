from CourseEditor import db
from sqlalchemy.sql import text

class Course(db.Model):

    __tablename__ = "course"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(144), nullable=False)
    time = db.Column(db.String(144), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)

    accounts = db.relationship('User', secondary='account_course', backref='course', lazy=True)

    def __init__(self, name, content, time):
        self.name = name
        self.content = content
        self.time = time

    @staticmethod 
    def list_course_and_teacher(user_id):
        stmt = text("SELECT Course.name, Course.content, Course.time, Teacher.firstname, Teacher.lastname FROM Course, Teacher "
                    "LEFT JOIN account_course ON user_id = :user AND course_id = Course.id "
                    "WHERE Course.teacher_id = Teacher.id").params(user=user_id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "content":row[1], "time":row[2], "firstname":row[3],"lastname":row[4]})

        return response