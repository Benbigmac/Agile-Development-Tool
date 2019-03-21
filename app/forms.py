
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('UserName')
    password =StringField('Password')
    password2 =StringField('Password')
    email = EmailField("Email",  validators=[])
    nameF = StringField('Name')
    nameL = StringField('Name')
    submit = SubmitField("Create Account")


class ProjectForm(FlaskForm):
    titleOfProject = StringField('Project Name')
    team = StringField('team')
    description = StringField('description')
    taskGoals = StringField('Goals of Project')
    submit = SubmitField('Create Project')


class TaskForm(FlaskForm):
    taskGoal = StringField('State the goal')
    storyPoint = StringField('Story Point')
    assignedTo = StringField('Assigned To')
