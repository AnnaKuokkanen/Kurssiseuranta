from CourseEditor import db
from CourseEditor.models import Base
from CourseEditor.usercourse.models import UserCourse
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id', ondelete='cascade'), nullable=False)

    courses = db.relationship('Course', secondary='account_course', cascade='all, delete-orphan', backref='account', single_parent=True, lazy=True)

    def __init__(self, firstname, lastname, username, password, role_id):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.role_id = role_id

    def get_id(self):
        return self.id
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        roles = []
        roles.append(Role.search_role(self.role_id))
        return roles[0]

    @staticmethod
    def remove_row(user_id, course_id):
        stmt = text("DELETE FROM account_course WHERE user_id = :user AND course_id = :course").params(user=user_id, course=course_id)
        db.engine.execute(stmt)
    
    @staticmethod
    def remove_user(user_id):
        stmt = text("DELETE FROM account_course WHERE user_id = :user").params(user=user_id)
        db.engine.execute(stmt)
    
    @staticmethod
    def list_all_users():
        stmt = text("SELECT id, firstname, lastname, role_id FROM account")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "firstname":row[1], "lastname":row[2], "role_id":row[3]})

        return response

    @staticmethod
    def count_statistics(user_id):
        response = []

        stmt = text("SELECT COUNT(DISTINCT course_id) FROM account_course")
        res = db.engine.execute(stmt)

        for row in res:
            response.append(row[0])
        
        stmt = text("SELECT COUNT(*) FROM account WHERE role_id = :role").params(role=1)
        res = db.engine.execute(stmt)

        for row in res:
            response.append(row[0])
        
        stmt = text("SELECT COUNT(*) FROM account WHERE role_id = :role").params(role=2)
        res = db.engine.execute(stmt)

        for row in res:
            response.append(row[0])

        stmt = text("SELECT COUNT(DISTINCT user_id) FROM account_course")
        res = db.engine.execute(stmt)

        for row in res:
            response.append(row[0])

        # Searching biggest from number of students per course
        stmt = text("SELECT MAX(students) "
                    "FROM (SELECT COUNT(account_course.user_id) AS students FROM account_course "
                    "GROUP BY account_course.course_id) AS students")
        res = db.engine.execute(stmt)

        for row in res:
            if row[0] is None:
                response.append(0)
            else:
                response.append(row[0])

        # Counting particular user's completed courses
        stmt = text("SELECT COUNT(Course.id) FROM Course "
                    "LEFT JOIN account_course ON Course.id = account_course.course_id "
                    "WHERE account_course.user_id = :user AND account_course.completed = :completed").params(user=user_id, completed=True)
        res = db.engine.execute(stmt)

        for row in res:
            response.append(row[0])
        
        # Counting how many different teachers particular user has
        stmt = text("SELECT COUNT(Course.teacher_id) FROM Course "
                    "LEFT JOIN account_course ON Course.id = account_course.course_id "
                    "WHERE account_course.user_id = :user").params(user=user_id)
        res = db.engine.execute(stmt)

        for row in res:
            response.append(row[0])

        return response

class Role(db.Model):

    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(5), nullable=False)

    users = db.relationship("User", cascade='all, delete-orphan', backref='role', single_parent=True, lazy=True)

    def __init__(self, id, role):
        self.id = id
        self.role = role

    @staticmethod
    def search_role(role_id):
        stmt = text("SELECT Role.role FROM Role WHERE Role.id = :role").params(role=role_id)  
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[0])

        return response
    