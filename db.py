from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgres://dvrasipcdyeqjm:8976b22c7162e02fdd7a27e306d81aec2ca97d358f70ad2667d906180581'
                       'caaa@ec2-3-226-163-72.compute-1.amazonaws.com:5432/d2d94atldmahtn')


Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base
