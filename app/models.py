from datetime import datetime
from app import db


class Accounts(db.model):
	AccID = db.Column(db.Integer, primary_key=True)
	fname = db.Column(db.String(20), index=True, unique=True)
	lname = db.Column(db.String(20), index=True, unique=True)
	username = db.Column(db.String(20), index=True, unique=True)
	password = db.Column(db.String(20), index=True, unique=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	def __repr__(self):
		return '<Accounts {}>'.format(self.username)