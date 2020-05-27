
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, session, render_template,request,redirect,url_for
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

class Controller():

    def add(self):
        session["jobs"].append(self.message)
    def remove(self):
        session["jobs"].remove(self.message)
    def check(self):
        temp = request.form.get("remove")
        if temp != None:
            self.message = temp
            return "remove"
        else:
            temp = request.form.get("add")
            if temp:
                self.message = temp
                return "add"

        return None

@app.route("/", methods=["GET","POST"])
def index():
    a = Controller()
    if session.get("jobs") ==None:
        session["jobs"]=[]
    if request.method == "POST":
       message = a.check()
       if message:
            if message == "add":
               a.add()
            elif message == "remove":
                a.remove()
       return redirect(url_for('index'))
    return render_template ("index.html",jobs= session["jobs"])

if __name__=='__main__':
        app.run(debug=True)
