from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


login_manager = LoginManager()
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'User'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password_hash = db.Column(db.String(80))
    role = db.Column(db.String(80))
    timeSheets = db.relationship('TimeSheet', backref='user', lazy=True)
    projects = db.relationship('Project', backref='user', lazy=True)

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    def get_id(self):
        return self.user_id


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(user_id=user_id).first() or None


class Task(db.Model):
    __tablename__ = 'Task'
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    description = db.Column(db.Text)
    project_id = db.Column(db.Integer, db.ForeignKey('Project.project_id'))
    timeSheets = db.relationship('TimeSheet', backref='task', lazy=True)


class TimeSheet(db.Model):
    __tablename__ = 'TimeSheet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    comment = db.Column(db.Text)
    date_submitted = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    task_id = db.Column(db.Integer, db.ForeignKey('Task.task_id'))


class Project(db.Model):
    __tablename__ = 'Project'
    project_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(80))
    start_date = db.Column(db.Date)
    expected_end_date = db.Column(db.Date)
    project_description = db.Column(db.Text)
    project_manager = db.Column(db.String(80))
    tasks = db.relationship('Task', backref='project', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
