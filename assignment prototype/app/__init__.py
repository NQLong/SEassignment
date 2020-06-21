from flask import Flask
from flask_session import Session
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session, relationship

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

Base = declarative_base() 
engine = create_engine('postgres://super:12340@localhost/apptest')
db = scoped_session(sessionmaker(bind=engine))
ins = inspect(engine)

from app import view