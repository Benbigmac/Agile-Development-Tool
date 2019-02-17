from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RegistrationForm


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/signUp')
def index():
    form = RegistrationForm()
    return render_template("signUp.html",form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('signIn.html', title='Sign In', form=form)
