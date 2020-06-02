from CourseEditor import db
from sqlalchemy.sql import text

class Course(db.Model):

    __tablename__ = "course"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(144), nullable=False)
    time = db.Column(db.String(144), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id', ondelete='cascade'), nullable=False)

    accounts = db.relationship('User', secondary='account_course', cascade='all, delete-orphan', backref='course', single_parent=True, lazy=True)

    def __init__(self, name, content, time):
        self.name = name
        self.content = content
        self.time = time

    @staticmethod 
    def list_course_and_teacher(user_id):
        stmt = text("SELECT Course.id, Course.name, Course.content, Course.time, Teacher.firstname, Teacher.lastname FROM Course, Teacher "
                    "LEFT JOIN account_course ON user_id = :user "
                    "WHERE Course.teacher_id = Teacher.id AND course_id = Course.id").params(user=user_id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "content":row[2], "time":row[3], "firstname":row[4],"lastname":row[5]})

        return response

    @staticmethod 
    def find_course_and_teacher(user_id, course_name):
        stmt = text("SELECT Course.id, Course.name, Course.content, Course.time, Teacher.firstname, Teacher.lastname FROM Course, Teacher "
                    "LEFT JOIN account_course ON user_id = :user "
                    "WHERE Course.teacher_id = Teacher.id AND Course.name = :name AND course_id = Course.id").params(user=user_id, name=course_name)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "content":row[2], "time":row[3], "firstname":row[4],"lastname":row[5]})

        return response

    @staticmethod
    def check_if_course_and_teacher_exist(teacher_id, course_name, course_content, course_time):
        stmt = text("SELECT Course.id FROM Course "
                    "WHERE Course.teacher_id = :id AND Course.name = :name AND Course.content = :content AND Course.time = :time").params(id=teacher_id, name=course_name, content=course_content, time=course_time)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0]})
        
        return response