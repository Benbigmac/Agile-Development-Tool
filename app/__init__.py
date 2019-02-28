from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import urllib

app = Flask(__name__)
app.config.from_object(Config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://SEW-DESK/Firescrum'
db = SQLAlchemy(app)

SQLALCHEMY_TRACK_MODIFICATIONS = False

migrate = Migrate(app,db)

from app import routes #, models <- to be implmented
