from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'random_secret_key'
app.config.from_object('config.Config') 
CORS(app)

db = SQLAlchemy(app)

from app import routes, models