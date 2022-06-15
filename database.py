from ssl import create_default_context
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#create database engine
engine=create_engine("sqlite:///todo.db")# creates a todo.db in current working directory

Base = declarative_base() #ways to access the actual database

SessionLocal=sessionmaker(bind=engine,expire_on_commit=False)
