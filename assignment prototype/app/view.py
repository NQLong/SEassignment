from app import app, Session, db
from flask import session, render_template, redirect, url_for, request
from sqlalchemy import and_
from app.models import Staff, Orders
class EmployeeView():
    def accountcheck(self):
        if session.get("employee") == None:
            return False
        return True
    def Eredirect(self):
        if session["employee"].Stype == "cook":
            return render_template("CookIndex.html")
    def Elogin(self, Ename, Epass):
        temp = db.query(Staff).filter(Staff.Sname == Ename).first()
        if not temp: return False
        elif temp.SPass == Epass:
            session["employee"] = temp
            return True
        else: 
            return False


class CookController():
    def CookAuthen(self):
        if session.get("employee"):
            if session["employee"].Stype == "cook":
                return True
        return False


Empview = EmployeeView()
Cook = CookController()

@app.route("/employee")
def EmpHome():
    if not Empview.accountcheck():
        return render_template("EmployeeIndex.html")
    elif session["employee"].Stype == "cook":
        return redirect(url_for("CookIndex"))
    


@app.route("/elogin", methods = ["POST","GET"])
def Elogin():
    if request.method == "POST":
        Ename = request.form.get("name")
        Epass = request.form.get("password")
        if Empview.Elogin(Ename,Epass):
            return EmpHome()
    elif not Empview.accountcheck():
        return render_template("EmployeeLogin.html")
    else:
        return redirect(url_for("EmpHome"))


@app.route("/CookIndex")
def CookIndex():
    if Cook.CookAuthen():
        return render_template("CookIndex.html", username = session["employee"].Sname)

@app.route("/Cook/waitingorder")
def Waitingorders():
    if Cook.CookAuthen():
        temp = db.query(Orders).filter(and_(Orders.Vid==session["employee"].Vid, Orders.Ostat == "confirmed")).all()
        print(temp)
        return render_template("Orderlist.html", orderlist = temp)
        