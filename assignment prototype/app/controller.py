from app.models import Customer, Staff, Item, Vendor,Orders, LineItem
from flask import session
from app import db, Base, engine

Base.metadata.create_all(engine)
class CookServices():
    def auth(self):
        if session.get("employee") == None:
            return False
        elif session["employee"].Stype == "cook":
            return True
        return False
