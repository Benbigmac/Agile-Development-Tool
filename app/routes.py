from flask import render_template, flash, redirect, url_for, request,session
from app import app
from app.forms import LoginForm, RegistrationForm
import json


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if request.method == 'POST':
        return redirect(url_for('projectList'))
    else:
        return render_template("index.html",title="FireScrum",form=form,username="Ben")

@app.route('/signUp')
def signUpPage():
    form = RegistrationForm()
    return render_template("signUp.html",form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        return redirect(url_for('projectList'))
    else:
        return render_template('signIn.html', title='Sign In', form=form,username="Ben")

@app.route('/about')
def about():
    return render_template("aboutfirescrum.html")

@app.route('/projects')
def projectList():
    projList=[{"name":"FireScrum","description":"IT's WHAT YOU're USING!"},{"name":"D&D Web App","description":"We're working on stuff here"}]
    return render_template("projects.html",projectList=projList, username="Ben")

@app.route('/createProject', methods=['GET', 'POST'])
def createProj():
    if request.method == 'POST':
    #    request.form[""]
        return redirect(url_for('projectList'))
    return render_template("projects.html")

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
