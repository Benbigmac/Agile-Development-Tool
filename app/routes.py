from flask import render_template, flash, redirect, url_for, request,session
from app import app
from app.forms import LoginForm, RegistrationForm, ProjectForm
import json, sys

current_user=""
dataString='C:/Users/benma/Desktop/cs442/code/v2/group7/app/data/'
#dataString='C:/Users/swald/group7/app/data/'
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
    filein = open((dataString+'projects.json'), 'r')
    print (filein.read(), file=sys.stdout)
    filein.seek(0,0)
    projList = json.loads(filein.read())
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

    filein = open('C:/Users/swald/group7/app/data/projects.json', 'r')
    print (filein.read(), file=sys.stdout)
    filein.seek(0,0)
    projList = json.loads(filein.read())
    # print(projList)
    # db.session.add(p)
    # db.session.commit()
    # ListOProjects = Projects.query.all()
    # for p in ListOProjects:
    #     print(p.name, p.ProjectID)
    # projList = ListOProjects
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
