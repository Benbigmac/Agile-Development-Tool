from flask import render_template, flash, redirect, url_for, request,session
from app import app
from app.forms import LoginForm, RegistrationForm
import json

loggedIn=False
@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if request.method == 'POST':
        session['username'] = request.form['username']
        loggedIn=True
        return redirect(url_for('projectList'))
    else:
        return render_template("index.html",title="FireScrum",form=form,username="Ben")

@app.route('/signUp')
def index():
    form = RegistrationForm()
    return render_template("signUp.html",form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        session['username'] = request.form['username']
        loggedIn=True
        return redirect(url_for('projectList'))
    else:
        return render_template('signIn.html', title='Sign In', form=form,username="Ben")

@app.route('/about')
def about():
    return render_template("aboutfirescrum.html")

@app.route('/projects')
def projectList():
    username = request.cookies.get('username')
    projList=[{"name":"FireScrum","description":"IT's WHAT YOU're USING!"},{"name":"D&D Web App","description":"We're working on stuff here"}]
#    projList=json.dumps(projList)
    print (projList)
    return render_template("projects.html",projectList=projList, username="Ben")

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
