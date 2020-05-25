from CourseEditor import db
from CourseEditor.users import models
from CourseEditor.courses import models

UserCourse = db.Table('account_course',
                        db.Column('user_id', db.Integer, db.ForeignKey('account.id'), primary_key=True), 
                        db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True))
