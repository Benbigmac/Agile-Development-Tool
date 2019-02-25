from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, RegistrationForm

loggedIn=False
@app.route('/')
def home():
    form = RegistrationForm()
    return render_template("index.html",title="FireScrum",form=form)

@app.route('/signUp')
def index():
    form = RegistrationForm()
    return render_template("signUp.html",form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        loggedIn=True
        return redirect(url_for('projectList'))
    else:
        return render_template('signIn.html', title='Sign In', form=form)

@app.route('/about')
def about():
    return render_template("aboutfirescrum.html")



@app.route('/projects')
def projectList():
    projList=[{},{}]
    return render_template("projects.html",projectList=projList)
