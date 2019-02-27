from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import urllib

app = Flask(__name__)
app.config.from_object(Config)


params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=SEW-DESK;DATABASE=Firescrum;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
 

SQLALCHEMY_TRACK_MODIFICATIONS = False

from app import routes