from datetime import datetime
from app import db


class Accounts(db.Model):
    AccID = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    fname = db.Column(db.String(20), index=True)
    lname = db.Column(db.String(20), index=True)
    username = db.Column(db.String(20), index=True, unique=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(50), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return unicode(self.AccID)
        
    def __repr__(self):
        return '<Accounts {}>'.format(self.username)


class Projects(db.Model):
    name = db.Column(db.String(50))
    ProjectID = db.Column(db.Integer, primary_key=True,
                          index=True, unique=True)
    description = db.Column(db.String(50))
    start_date = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return '<Projects {}>'.format(self.ProjectID)


class Stories(db.Model):
    ProjectID = db.Column(db.Integer, db.ForeignKey('Projects.id'))
    description = db.Column(db.String(50))
    StoryID = db.Column(db.Integer, primary_key=True, index=True, unique=True)

    def __repr__(self):
        return '<Stories {}>'.format(self.StoryID)


class Tasks(db.Model):
    TaskID = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    StoryID = db.Column(db.Integer, db.ForeignKey('Stories.StoryID'))
    description = db.Column(db.String(50))
    effort = db.Column(db.Integer)

    def __repr__(self):
        return '<Tasks {}>'.format(self.TaskID)


class Userprojects(db.Model):
    ident = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    ProjectID = db.Column(db.Integer, db.ForeignKey('Projects.ProjectID'))
    AccID = db.Column(db.Integer, db.ForeignKey('Accounts.AccID'))
