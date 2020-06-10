import os
import string
from flask import Flask, session, render_template,request,redirect,url_for
from flask_session import Session
from models import *
import requests



app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)