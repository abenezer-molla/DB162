from sqlalchemy import create_engine, Column, Integer,BigInteger, ForeignKey, Date, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, column_property
from sqlalchemy.sql import case
from datetime import datetime

engine = create_engine('sqlite:///moneyflow.db') # my databse that will contain all the Tables belows(defined in class)
engine.connect()

Base = declarative_base()


class Transactor(Base): # defining Transactor table

    __tablename__ = "Transactor"

    transactor_id= Column(Integer,primary_key=True,unique=True)
    transactor_firstName=Column(String(25),nullable=False)
    transactor_lastName=Column(String(80),nullable=False)
    transactor_email=Column(String(),nullable=False)
    transactor_phoneNumber=Column(BigInteger,nullable=False)

    def __init__(self, transactor_firstName, transactor_lastName, transactor_email, transactor_phoneNumber):

        self.transactor_firstName = transactor_firstName
        self.transactor_lastName = transactor_lastName
        self.transactor_email = transactor_email
        self.transactor_phoneNumber = transactor_phoneNumber

        

class Agent(Base): # defining Agent table

    __tablename__ = "Agent"

    agent_id=Column(Integer,primary_key=True, unique=True)
    agent_firstName=Column(String(25),nullable=False)
    agent_lastName=Column(String(25),nullable=False)
    agent_email=Column(String(80),nullable=False)
    agent_phoneNumber=Column(BigInteger,nullable=False)

    def __init__(self, agent_firstName,agent_lastName, agent_email, agent_phoneNumber):
    
        self.agent_firstName = agent_firstName
        self.agent_lastName = agent_lastName
        self.agent_email = agent_email
        self.agent_phoneNumber = agent_phoneNumber

class Offices(Base): # defining Offices table

    __tablename__ = "Offices"

    office_id=Column(Integer,primary_key=True, unique=True)
    office_address=Column(String(25),nullable=False)

    def __init__(self, office_address):
        self.office_address = office_address


class Houses(Base): # defining Houses table

    __tablename__ = "Houses"

    house_id=Column(Integer,primary_key=True,unique=True)
    house_address=Column(String(25),nullable=False)
    number_of_bedrooms=Column(Integer,nullable=False)
    number_of_bathrooms=Column(Integer,nullable=False)
    area_in_squareMeter=Column(Integer,nullable=False)
    office_id=Column(Integer, ForeignKey('Offices.office_id'))

    def __init__(self, house_address, number_of_bedrooms, number_of_bathrooms, area_in_squareMeter, office_id):
    
        self.house_address = house_address
        self.number_of_bedrooms = number_of_bedrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.area_in_squareMeter = area_in_squareMeter
        self.office_id = office_id



class Sales(Base): # defining Sales table
    __tablename__='Sales'

    sale_id = Column(Integer, primary_key=True, unique=True)
    buyer_id = Column(Integer, ForeignKey('Transactor.transactor_id'))
    agent_id = Column(Integer, ForeignKey('Agent.agent_id'))
    house_id = Column(Integer, ForeignKey('Houses.house_id'))
    price = Column(Integer)
    date_sold = Column(Date)

    sales_commission = column_property(price * case(
        [
            (price < 100000, 0.1),
            (price < 200000, 0.075),
            (price < 500000, 0.06),
            (price < 1000000, 0.05),
        ], else_ = 0.04))

    def __init__(self, buyer_id, agent_id, house_id, price, date_sold, sales_commission):

        self.buyer_id = buyer_id
        self.agent_id = agent_id
        self.house_id = house_id
        self.price = price
        self.date_sold = date_sold
        self.sales_commission = sales_commission


class Price_Sum(Base):  # defining Price_Sum table

    __tablename__ = 'Price_Sum' 

    price_id=Column(Integer,primary_key=True, unique=True)
    price_sum=Column(Integer)

    def __init__(self,price_sum):
        self.price_sum = price_sum


class Commission_Sum(Base): # defining Commission_Sum table

    __tablename__ = "Commission_Sum"

    commission_id=Column(Integer,primary_key=True, unique=True)
    link_id =Column(String(25),nullable=False)
    commision=Column(String(80),nullable=False)

    def __init__(self, commission_id, link_id, commision):
        
        self.commission_id = commission_id
        self.link_id = link_id
        self.commision = commision


class Listing_For_Sale(Base): # defining Listing_For_Sale table

    __tablename__ = "Listing_For_Sale"

    listing_id=Column(Integer,primary_key=True, unique=True)
    house_id=Column(Integer, ForeignKey('Houses.house_id'))
    seller_id=Column(Integer, ForeignKey('Transactor.transactor_id') )
    agent_id=Column(Integer,ForeignKey('Agent.agent_id'))
    listing_date=Column(Date)
    price=Column(Integer)
    isSold=Column(Boolean)

    def __init__(self, price,agent_id, seller_id, house_id , listing_date ,isSold ):

        self.price = price
        self.agent_id = agent_id
        self.house_id = house_id
        self.seller_id = seller_id
        self.listing_date = listing_date
        self.isSold = isSold


class Agent_to_Office_Link(Base):  # defining Agent_Office_Link table

    __tablename__ = "Agent_Office_Link"

    link_id=Column(Integer,primary_key=True,unique=True)
    office_id=Column(Integer,nullable=False)
    agent_id=Column(Integer,nullable=False)
    

    def __init__(self, office_id, agent_id):
        
        self.office_id = office_id
        self.agent_id = agent_id

def Transaction_Objects(): 
    '''
    This function will return list_of_transaction_objects
    which is the a list dictionaries in which each dictionary will contain the important detials associated with the sold house. 
    The returned value from this function will be used as input for Transaction_Processor(inside Data_Insertion.py) to update value sin different Tables once the sold house is identified.
    
    '''

    list_of_transaction_objects = [{'buyer_id': 6, 'agent_id': 2, 'house_id': 1, 'price': 1000000, 'date_sold': datetime(2022, 4, 14)},
                        {'buyer_id': 4, 'agent_id': 1, 'house_id': 2, 'price': 999999, 'date_sold': datetime(2022, 4, 13)},
                        {'buyer_id': 2, 'agent_id': 4, 'house_id': 6, 'price': 1200000, 'date_sold': datetime(2022, 4, 12)},
                        {'buyer_id': 3, 'agent_id': 3, 'house_id': 5, 'price': 8000000, 'date_sold': datetime(2022, 4, 11)},
                        {'buyer_id': 4, 'agent_id': 5, 'house_id': 4, 'price': 950000, 'date_sold': datetime(2022, 4, 10)},
                        {'buyer_id': 1, 'agent_id': 6, 'house_id': 3, 'price': 867890, 'date_sold': datetime(2022, 4, 9)}
                        ]

    return list_of_transaction_objects

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
