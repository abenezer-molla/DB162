from Table_Skeleton import Agent, Agent_to_Office_Link, Transactor, Offices, Price_Sum, Transaction_Objects, Houses, Sales, Listing_For_Sale, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
from datetime import datetime


Session = sessionmaker(bind=engine)  #binding the engine to make sure that we are adding data to the same DB we created in Table_Skeleton.py

session = Session() # initializing session

#Agent class will recieve the data in the following format :-
#Agent(agent_firstName, agent_lastName, agent_email, agent_phoneNumber)

agent1 = Agent('Abenezer', 'Molla','abenmolla@gmail.com', 4153778679) 
agent2 = Agent('Bereket', 'Ademe','bereket@gmail.com', 4156789086)
agent3 = Agent('Gedion', 'Mulat','gedion@gmail.com', 4155678947)
agent4 = Agent('Abiy', 'Ahmed','abiy@gmail.com', 4155679302)
agent5 = Agent('Teferi', 'Mekonnen','teferi@gmail.com', 4159038809)
agent6 = Agent('Teddy', 'Afro','teddyafro@gmail.com', 41530981837)


# The 6 lines of code below will add the agent instance created above into Agent table

session.add(agent1) 
session.add(agent2)
session.add(agent3)
session.add(agent4)
session.add(agent5)
session.add(agent6)


######

#Transactor class will recieve the data in the following format :-
#Transactor(transactor_firstName, transactor_lastName, transactor_email, transactor_phoneNumber)

transactor1 = Transactor('James', 'Bond','jamesbond@gmail.com', 2136789503)
transactor2 = Transactor('Gal', 'Gadot','galgadot@gmail.com', 2136784098)
transactor3 = Transactor('Diane', 'Kruger','dianekruger@gmail.com', 2130928659)
transactor4 = Transactor('Jennifer' ,'Aniston', 'jenniferaniston@gmail.com', 2138030027)
transactor5 = Transactor('Emma', 'Watson','emmawatson@gmail.com', 2130289170)
transactor6 = Transactor('Emilia', 'Clarke','emiliaclarke@gmail.com', 2137048372)

# The 6 lines of code below will add the transactor instance created above into Transactor table

session.add(transactor1)
session.add(transactor2)
session.add(transactor3)
session.add(transactor4)
session.add(transactor5)
session.add(transactor6)


#####

#Offices class will recieve the data in the following format :-
#Offices(office_address)

office1 = Offices('New York City, NY')
office2 = Offices('Los Angeles, CA')
office3 = Offices('Boston, MA')
office4 = Offices('Las Vegas, NV')
office5 = Offices('Seattle, WA')
office6 = Offices('Atlanta, GA')

# The 6 lines of code below will add the office instances created above into Offices table

session.add(office1)
session.add(office2)
session.add(office3)
session.add(office4)
session.add(office5)
session.add(office6)


###

#Agent_to_Office_Link class will recieve the data in the following format :-
#Agent_to_Office_Link(office_id, agent_id)

link1 = Agent_to_Office_Link(6, 1)
link2 = Agent_to_Office_Link(2, 2)
link3 = Agent_to_Office_Link(1, 4)
link4 = Agent_to_Office_Link(5, 3)
link5 = Agent_to_Office_Link(3, 6)
link6 = Agent_to_Office_Link(4, 5)

# The 6 lines of code below will add the link instances created above into table

session.add(link1)
session.add(link2)
session.add(link3)
session.add(link4)
session.add(link5)
session.add(link6)


###

#Houses class will recieve the data in the following format :-
#Houses(house_address, number_of_bedrooms, number_of_bathrooms, area_in_squareMeter, office_id)

house1 = Houses(94102, 3, 3, 500, 1)
house2 = Houses(941074, 3, 4, 600, 3)
house3 = Houses(97104, 2, 4, 300, 4)
house4 = Houses(96407, 1, 1, 150, 2)
house5 = Houses(94110, 3, 2, 250, 6)
house6 = Houses(83602, 5, 5, 1000,5)

# The 6 lines of code below will add the house instances created above into Houses table

session.add(house1)
session.add(house2)
session.add(house3)
session.add(house4)
session.add(house5)
session.add(house6)


###

#Listing_For_Sale class will recieve the data in the following format :-
#Listing_For_Sale(price,agent_id, seller_id, house_id , listing_date ,isSold)

listing1 = Listing_For_Sale(1234592, 1, 5, 3, datetime(2022, 4, 8), False)
listing2 = Listing_For_Sale(980598, 3, 6,1,datetime(2022, 4, 7), False)
listing3 = Listing_For_Sale(903789, 6, 2,5,datetime(2022, 4, 6),False)
listing4 = Listing_For_Sale(879069, 5, 3,1, datetime(2022, 4, 5),False)
listing5 = Listing_For_Sale(2009087, 2,1,4, datetime(2022, 4, 4),False)
listing6 = Listing_For_Sale(509890, 4,4,6, datetime(2022, 4, 3),False)


# The 6 lines of code below will add the listing instances created above into Listing_For_Sale table

session.add(listing1)
session.add(listing2)
session.add(listing3)
session.add(listing4)
session.add(listing5)
session.add(listing6)


#Price_Sum class will recieve the data in the following format :-
#Price_Sum(price_sum)

session.add(Price_Sum(price_sum=0))

session.commit()


###


# reference --> https://docs.sqlalchemy.org/en/13/orm/session_basics.html

def Transaction_Processor(transaction_object):
    '''
    This method will take inputs from the returned values of "Transaction_Objects function which I have imported from Table_Skeleton.py"
    Updates the value of price_sum(of Price_Sum class) and the value of isSold(from Listing_For_Sale class) only when the house is sold. 

    '''
    try: 
        session.execute(insert(Sales), [transaction_object])
        session.query(Listing_For_Sale).filter(Listing_For_Sale.house_id == transaction_object['house_id']).update(
            {Listing_For_Sale.isSold: True},synchronize_session=False
        ) # once the house is sold, change the boolean value from False to True
        session.query(Price_Sum).filter(Price_Sum.price_id == 1).update(
            {Price_Sum.price_sum: Price_Sum.price_sum + transaction_object['price']},
            synchronize_session=False
        ) # update the price_sum when ever a new house is being sold
        session.commit()
    except:
        session.rollback() # if no the house is not sold yet, then rollback and don't commit anything to the DB. 
        raise   
    session.close() # at the end, close the DB


for each_transaction_object in Transaction_Objects():  # looping through each value from what is returned from Transaction_Objects function. 
    Transaction_Processor(each_transaction_object) # inserting each transaction_object to the Transaction_Processor function above. 
session.commit()


