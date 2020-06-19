from CourseEditor import db
from sqlalchemy import Table, Integer, ForeignKey, Column

class UserCourse(db.Model):
    __tablename__ = "account_course"
    user_id = db.Column(db.Integer, db.ForeignKey('account.id', ondelete='cascade'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete='cascade'), primary_key=True)
    completed = db.Column(db.Boolean, nullable=False)
    planned = db.Column(db.Boolean, nullable=False)

    def __init__(self, user_id, course_id, completed, planned):
        self.user_id = user_id
        self.course_id = course_id
        self.completed = completed
        self.planned = planned
