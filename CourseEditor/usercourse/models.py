from CourseEditor import db
from CourseEditor.users import models
from CourseEditor.courses import models

user_course = db.Table('course_user',
                    db.Column('user_id', db.Integer, db.ForeignKey('account.id'), primary_key=True), 
                    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True))