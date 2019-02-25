from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

from app import routes



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://SEW-TABUTER/SQLEXPRESS/blueprism6.3'
db = SQLAlchemy(app)

SQLALCHEMY_TRACK_MODIFICATIONS = False