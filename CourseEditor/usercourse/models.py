from CourseEditor import db
#from sqlalchemy import Table, Integer, ForeignKey, Column

class UserCourse(db.Model):
    __tablename__ = "account_course"
    user_id = db.Column(db.Integer, db.ForeignKey('account.id', ondelete='cascade'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete='cascade'), primary_key=True)
    completed = db.Column(db.Boolean, nullable=False)
    planned = db.Column(db.Boolean, nullable=False)

    def __init__(self, completed, planned):
        self.completed = False
        self.planned = False

#UserCourse = db.Table('account_course',
                        #db.Column('user_id', db.Integer, db.ForeignKey('account.id', ondelete='cascade'), primary_key=True), 
                        #db.Column('course_id', db.Integer, db.ForeignKey('course.id', ondelete='cascade'), primary_key=True))

