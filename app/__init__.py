from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import urllib

app = Flask(__name__)
app.config.from_object(Config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://SEW-DESK/Firescrum'
db = SQLAlchemy(app)



from app import routes
