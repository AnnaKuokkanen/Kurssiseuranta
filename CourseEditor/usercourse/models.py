from CourseEditor import db
from sqlalchemy import Table, Integer, ForeignKey, Column

UserCourse = db.Table('account_course',
                        db.Column('user_id', db.Integer, db.ForeignKey('account.id', ondelete='cascade'), primary_key=True), 
                        db.Column('course_id', db.Integer, db.ForeignKey('course.id', ondelete='cascade'), primary_key=True))

