import string
from flask import Flask, session, render_template,request,redirect,url_for
from flask_session import Session
from models import *
import requests

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/ulogin')
def ulogin():
    return render_template("ulogin.html")

@app.route("/ordering")
def makeorder():
    pass

@app.route("/employee")
def elogin():
    return render_template("elogin.html")


@app.route("/esignup", methods = ["POST", "GET"])
def esignup():
    if request.method == "POST":
        ename = request.form.get("name")
        epass = request.form.get("password")
        etype = request.form.get("etype")
        eVid = int(request.form.get("vid"))
        employ = Staff(ename,epass,etype,eVid)
        db.add(employ)
        db.commit()
        return render_template("/elogin.html")
    else:
        return render_template("/esignup.html")   

@app.route("/vsignup", methods = ["POST", "GET"])
def vsignup():
    if request.method == "POST":
        vname = request.form.get("name")
        vend = Vendor(vname)
        db.add(vend)
        db.commit()
    return render_template("/vsignup.html")

@app.route("/additem",methods = ["POST", "GET"])
def isignup():
    if request.method == "POST":
        iname = request.form.get("name")
        iprice =int(request.form.get("price"))
        ivid = int(request.form.get("vid"))
        item = Item(iname, iprice,ivid)
        db.add(item)
        db.commit()
    return render_template("/isignup.html")

@app.route("/osignup",methods = ["POST", "GET"])
def osignup():
    if request.method == "POST":
        pass
    return render_template("/isignup.html")

@app.route("/csignup", methods = ["POST","GET"])
def csignup():
    if request.method == "POST":
        cname = request.form.get("name")
        cpass = request.form.get("password")
        cbilling = request.form.get("billing")
        Cmer = Customer(cname, cpass, cbilling)
        db.add(Cmer)
        db.commit()
    return render_template("/csignup.html")
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug = True)