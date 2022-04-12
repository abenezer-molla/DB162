from Table_Skeleton import Agent, Agent_to_Office_Link, Transactor, Offices, Price_Sum, Commission_Sum, Houses, Sales, Listing_For_Sale, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
from datetime import datetime


Session = sessionmaker(bind=engine)
session = Session()
agent1 = Agent('Abenezer', 'Molla','abenmolla@gmail.com', 4153778679)
agent2 = Agent('Bereket', 'Ademe','bereket@gmail.com', 4156789086)
agent3 = Agent('Gedion', 'Mulat','gedion@gmail.com', 4155678947)
agent4 = Agent('Abiy', 'Ahmed','abiy@gmail.com', 4155679302)
agent5 = Agent('Teferi', 'Mekonnen','teferi@gmail.com', 4159038809)
agent6 = Agent('Teddy', 'Afro','teddyafro@gmail.com', 41530981837)

session.add(agent1)
session.add(agent2)
session.add(agent3)
session.add(agent4)
session.add(agent5)
session.add(agent6)


###

transactor1 = Transactor('James', 'Bond','jamesbond@gmail.com', 2136789503)
transactor2 = Transactor('Gal', 'Gadot','galgadot@gmail.com', 2136784098)
transactor3 = Transactor('Diane', 'Kruger','dianekruger@gmail.com', 2130928659)
transactor4 = Transactor('Jennifer' ,'Aniston', 'jenniferaniston@gmail.com', 2138030027)
transactor5 = Transactor('Emma', 'Watson','emmawatson@gmail.com', 2130289170)
transactor6 = Transactor('Emilia', 'Clarke','emiliaclarke@gmail.com', 2137048372)

session.add(transactor1)
session.add(transactor2)
session.add(transactor3)
session.add(transactor4)
session.add(transactor5)
session.add(transactor6)


###

office1 = Offices('New York City, NY')
office2 = Offices('Los Angeles, CA')
office3 = Offices('Boston, MA')
office4 = Offices('Las Vegas, NV')
office5 = Offices('Seattle, WA')
office6 = Offices('Atlanta, GA')

session.add(office1)
session.add(office2)
session.add(office3)
session.add(office4)
session.add(office5)
session.add(office6)


###

link1 = Agent_to_Office_Link(6, 1)
link2 = Agent_to_Office_Link(2, 2)
link3 = Agent_to_Office_Link(1, 4)
link4 = Agent_to_Office_Link(5, 3)
link5 = Agent_to_Office_Link(3, 6)
link6 = Agent_to_Office_Link(4, 5)

session.add(link1)
session.add(link2)
session.add(link3)
session.add(link4)
session.add(link5)
session.add(link6)


###



###


house1 = Houses(94102, 3, 3, 500, 1)
house2 = Houses(941074, 3, 4, 600, 1)
house3 = Houses(97104, 2, 4, 300, 1)
house4 = Houses(96407, 1, 1, 150, 1)
house5 = Houses(94110, 3, 2, 250, 1)
house6 = Houses(83602, 5, 5, 1000,1)

session.add(house1)
session.add(house2)
session.add(house3)
session.add(house4)
session.add(house5)
session.add(house6)




###

listing1 = Listing_For_Sale(1234592, 1, 5, 3, datetime(2022, 3, 20), False)
listing2 = Listing_For_Sale(980598, 3, 6,1,datetime(2022, 3, 21), False)
listing3 = Listing_For_Sale(903789, 6, 2,5,datetime(2022, 3, 22),False)
listing4 = Listing_For_Sale(879069, 5, 3,1, datetime(2022, 3, 23),False)
listing5 = Listing_For_Sale(2009087, 2,1,4, datetime(2022, 3, 24),False)
listing6 = Listing_For_Sale(509890, 4,4,6, datetime(2022, 3, 25),False)

session.add(listing1)
session.add(listing2)
session.add(listing3)
session.add(listing4)
session.add(listing5)
session.add(listing6)

session.commit()


###


def Transaction_Processor(transaction_object):
    try: 
        session.execute(insert(Sales), [transaction_object])
        session.query(Listing_For_Sale).filter(Listing_For_Sale.house_id == transaction_object['house_id']).update(
            {Listing_For_Sale.isSold: True},synchronize_session=False
        )
        session.query(Price_Sum).filter(Price_Sum.price_id == 1).update(
            {Price_Sum.price_sum: Price_Sum.price_sum + transaction_object['price']},
            synchronize_session=False
        )
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

print("ABEN")

ListVal = [{'buyer_id': 6, 'agent_id': 2, 'house_id': 1, 'price': 1000000, 'date_sold': datetime(2022, 4, 11)},
                        {'buyer_id': 4, 'agent_id': 1, 'house_id': 2, 'price': 999999, 'date_sold': datetime(2022, 4, 10)},
                        {'buyer_id': 2, 'agent_id': 4, 'house_id': 6, 'price': 1200000, 'date_sold': datetime(2022, 4, 9)},
                        {'buyer_id': 3, 'agent_id': 3, 'house_id': 5, 'price': 8000000, 'date_sold': datetime(2022, 4, 8)},
                        {'buyer_id': 4, 'agent_id': 5, 'house_id': 4, 'price': 950000, 'date_sold': datetime(2022, 4, 7)},
                        {'buyer_id': 1, 'agent_id': 6, 'house_id': 3, 'price': 867890, 'date_sold': datetime(2022, 4, 6)}
                        ]
print("CHECK ABEN")

for i in ListVal:
    print("DETAILS", i)
    Transaction_Processor(i)

session.commit()




print(session.query(Transactor).all())
print(session.query(Agent).all())
print(session.query(Offices).all())
print(session.query(Agent_to_Office_Link).all())
print(session.query(Houses).all())
print(session.query(Listing_For_Sale).all())
print(session.query(Sales).all())
print(session.query(Price_Sum).all())
