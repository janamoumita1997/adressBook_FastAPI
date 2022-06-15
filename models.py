from sqlalchemy import Column, Integer, String, Float
from database import Base

class Item(Base):
    __tablename__="items" #name of table
    id=Column(Integer,primary_key=True)#primary_key=True =>auto-increment of "id"
    location=Column(String(256)) #string of maximum length=256
    longitude=Column(Float) #longitude of the location
    latitude=Column(Float) #latitude of the location