from CourseEditor import db
#from sqlalchemy.sql import text
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

    # @staticmethod
    # def add_row(user_id, course_id):
        # stmt = text("INSERT INTO account_course VALUES "
        #             "(user_id = :user, " 
        #             "course_id = :course, "
        #             "completed = :completed, "
        #             "planned = :planned)").params(user=user_id, course=course_id, completed=False, planned=False)
        # db.engine.execute(stmt)

# UserCourse = db.Table('account_course',
#                         db.Column('user_id', db.Integer, db.ForeignKey('account.id', ondelete='cascade'), primary_key=True), 
#                         db.Column('course_id', db.Integer, db.ForeignKey('course.id', ondelete='cascade'), primary_key=True))
