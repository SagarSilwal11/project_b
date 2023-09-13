from sqlalchemy import create_engine,Column,Integer,String,Boolean
from sqlalchemy.orm import sessionmaker,declarative_base

Base=declarative_base()    


class Entryform(Base):
    __tablename__="User_Details"
    id=Column("id",Integer,autoincrement=True,primary_key=True)
    firstname=Column("fname",String)
    lastname=Column("lname",String)
    title=Column("title",String)
    age=Column("age",Integer)
    nationality=Column("nationality",String)
    completed_course=Column("completed_course",Integer)
    semester=Column("semester",Integer)
    registration_status = Column("Status",String,default=False)
    def __init__(self,firstname,lastname,title,age,nationality,completed_course,semester,registration_status ):
        self.firstname=firstname
        self.lastname=lastname
        self.title=title
        self.age=age
        self.nationality=nationality
        self.completed_course=completed_course
        self.semester=semester
        self.registration_status=registration_status
    def __str__(self):
        return f"{self.firstname}"
    

    
engine=create_engine("sqlite:///Pypy.db",echo=True)
Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)
session=Session()
print("Connected to Database Sucessfull")
        