from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_
engine=create_engine('postgresql://postgres:user24@localhost:5432/postgres')

Session=sessionmaker(bind=engine)
Session=Session()
Base=declarative_base()
class Bank(Base):
    __tablename__='bank'
    accno=Column(Integer, primary_key=True)
    name=Column(String(50))
    city=Column(String(45))
#Base.metadata.create_all(engine )
# b1=Bank(accno=34512,name="Sanskriti",city="banglore")
# b2=Bank(accno=43561,name="Rihana",city="surat")
# b3=Bank(accno=54231,name="Sanskriti",city="bhopal")
# b4=Bank(accno=63122,name="Riya",city="bombay")
# b5=Bank(accno=78352,name="Radhika",city="surat")
# b6=Bank(accno=82424,name="Neha",city="jhansi")
#b7=Bank(accno=83636,name="Ramita",city="kanpur")
#b8=Bank(accno=93253,name="Riva",city="lucknow")
#Session.add(b1)
#Session.add_all([b7,b8])
#Session.commit()

######### READ DATA
# Get all stored data:-
# bankrecords=Session.query(Bank)
# for i in bankrecords:
#     print(i.name,  i.accno,  i.city)

# Get data in order:-
# bankrecords=Session.query(Bank).order_by(Bank.name)
# for i in bankrecords:
#     print(i.name)

# Get data by Filtering:-
# b=Session.query(Bank).filter(Bank.city=="jhansi").first()
# print(b.name,b.accno)

# Get more than two records in bank by Filtering:-
# bankrecords=Session.query(Bank).filter(or_(Bank.name=="Riya",Bank.name=="Neha"))
# for i in bankrecords:
#     print(i.name, i.accno, i.city)

# # count the number of records:-
# i=Session.query(Bank).filter(or_(Bank.name=="Riya",Bank.name=="Neha")).count()
# print(i)

####### UPDATE DATA 
# b=Session.query(Bank).filter(Bank.city=="lucknow").first()
# b.city="jamshedapur"
# Session.commit()
# n=Session.query(Bank).filter(Bank.name=="Sanskriti").first()
# n.name="kriti"
# Session.commit()

####### DELETE DATA
# d=Session.query(Bank).filter(Bank.name=="kriti").first()
# Session.delete(d)
# Session.commit()

