from flask import render_template, flash, redirect, url_for, request,session
from app import app
from app.forms import LoginForm, RegistrationForm, ProjectForm
import json
from app import db
from app.models import Accounts, Projects, Stories, Tasks, Userprojects
from datetime import datetime

current_user=""
ListOPRojects=[{"name":"FireScrum","description":"IT's WHAT YOU're USING!"},{"name":"D&D Web App","description":"We're working on stuff here"}]

@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if request.method == 'POST':
        return redirect(url_for('projectList'))
    else:
        return render_template("index.html",title="FireScrum",form=form,current_user=current_user)

@app.route('/signUp')
def signUpPage():
    form = RegistrationForm()
    return render_template("signUp.html",form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        current_user=request.form["username"]
        #if current_user.is_authenticated():
        #    g.user = current_user.username
        return redirect(url_for('projectList', current_user= current_user))
    else:
        return render_template('signIn.html', title='Sign In', form=form,current_user=current_user)

@app.route('/about')
def about():
    return render_template("aboutfirescrum.html")

@app.route('/<current_user>/projects')
def projectList(current_user):
    projList=ListOPRojects
    return render_template("projects.html",projectList=projList, current_user=current_user)

@app.route('/<current_user>/projects/<projectName>')
def projectSplash(current_user,projectName):
    return render_template("projectDash.html", current_user=current_user)

@app.route('/<current_user>/createProject', methods=['GET', 'POST'])
def createProj(current_user):
    form = ProjectForm()
    if request.method == 'POST':
        projectName=request.form["titleOfProject"]
        description=request.form["description"]
        newProj={"name":projectName,"description":description}
        ListOPRojects.append(newProj)
        return redirect(url_for('projectList', current_user= current_user))
    return render_template("createProject.html",form=form)

@app.route('/DBTEST')
def dbTest():
    p = Projects(name='Firescrum', ProjectID=1, description='scrum stuff', start_date = datetime.datetime.now() )
    db.session.add(p)
    db.session.commit()
    ListOProjects = Projects.query.all()
    for p in ListOProjects:
        print(p.name, p.ProjectID)
    projList = ListOProjects
    return render_template("projects.html",projectList=projList, current_user=current_user)

@app.route('/logOut')
def logOut():
    current_user=""
    return  redirect(url_for('home'))

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.errorhandler(500)
def not_found(error):
    return render_template('error.html'), 500
