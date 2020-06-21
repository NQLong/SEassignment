from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app import Base, engine,db, ins


class Customer(Base):
    __tablename__="customer"
    Uid = Column(Integer,primary_key = True)
    Uname = Column(String,unique = True,nullable = False)
    Upass = Column(String,nullable = False)
    UbillingAddr = Column(String,nullable = True)

    def __init__(self, name, password, bill):
        self.Uname = name
        self.Upass = password
        self.UbillingAddr = bill
    
class Staff(Base):
    __tablename__="staff"
    Sid = Column(Integer,primary_key = True)
    Sname = Column(String,unique = True,nullable = False)
    SPass = Column(String,nullable = False)
    Stype = Column(String,nullable = False)
    Vid = Column(Integer, ForeignKey('vendor.Vid'), nullable = False)
    
    def __init__(self,name, password, stype, Vid):
        self.Sname = name
        self.SPass = password
        self.Stype = stype
        self.Vid = Vid


class Item(Base):
    __tablename__="item"
    Iid = Column(Integer,primary_key = True)
    Iname = Column(String,nullable = False)
    Iprice = Column(Integer,nullable = False)
    Idescript = Column(String)
    Irate = Column(Float,default = 0)
    Vid = Column(Integer, ForeignKey('vendor.Vid'), nullable = False)

    def __init__(self, iname, iprice, ivid,descr):
        self.Iname = iname
        self.Iprice = iprice
        self.Vid = ivid
        self.Idescript = descr

class Vendor(Base):
    __tablename__ = "vendor"
    Vid = Column(Integer,primary_key = True)
    Vname = Column(String,nullable = False)

    def __init__(self, vname):
        self.Vname = vname

class Orders(Base):
    __tablename__ = "orders"
    Oid = Column(Integer, primary_key = True)
    Oprice = Column(Integer, nullable = False)
    Uid = Column(Integer, ForeignKey('customer.Uid'), nullable = False)
    Vid = Column(Integer, ForeignKey('vendor.Vid'), nullable = False)
    Ostat = Column(String, nullable =False)

class LineItem(Base):
    __tablename__ = "lineitem"
    Lid = Column(Integer,primary_key = True)
    LItemID = Column(Integer, ForeignKey("item.Iid"))
    Lquantity = Column(Integer, nullable = False)
    Oid = Column(Integer, ForeignKey("orders.Oid"), nullable = False)