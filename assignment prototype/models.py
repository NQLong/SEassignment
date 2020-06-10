from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session, relationship


Base = declarative_base() 
engine = create_engine('postgres://super:12340@localhost/test')
db = scoped_session(sessionmaker(bind=engine))
ins = inspect(engine)

# class Vendor(Base):
#     __tablename__="vendors"
#     id = Column(Integer, primary_key=True)
#     Name
#     Staffs
#     Foods
#     Order

# class User(Base):
#     __tablename__="user"
#     id = Column(Integer,primary_key = True)
#     Username = Column(String,unique = True,nullable = False)
#     Password = Column(String,nullable = False)
#     Order = 

    
class Staff(Base):
    __tablename__="staff"
    id = Column(Integer,primary_key = True)
    Username = Column(String,unique = True,nullable = False)
    Password = Column(String,nullable = False)
    acctype = Column(Integer,nullable = False)
# class Staff(Base):
#     __tablename__="staffs"
#     id = Column(Integer,primary_key = True)
#     Username
#     Password
#     VendorID
    
# class Food(Base):
#     __tablename__="foods"
#     id = Column(Integer, primary_key=True)
#     Name
#     Amount
#     ActiveAmount
#     VendorID
#     Price
#     EstimateTime

# class Order(Base):
#     __tablename__="orders"
#     id = Column(Integer, primary_key=True)
#     UserID
#     LineItem
#     VendorID
#     CreateTime

# class LineItem(Base):
#     __tablename__="lineitems"
#     id = Column(Integer, primary_key=True)
#     FoodID
#     Amount