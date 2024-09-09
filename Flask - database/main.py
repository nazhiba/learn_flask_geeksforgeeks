from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py', silent=True)
app.config.from_mapping(SECRET_KEY='dev')

try:
     os.makedirs(app.instance_path)
except OSError:
     pass

app.config["SQLALCHRMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

class Base(DeclarativeBase):
     pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Event(db.Model):
     data = mapped_column(db.String, primary_key=True)
     event = mapped_column(db.String)


