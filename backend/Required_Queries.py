
from Table_Skeleton import Agent, Sales, Offices, Commission_Sum, Houses, Sales, Listing_For_Sale, engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Index
from sqlalchemy import func, extract, insert

Session = sessionmaker(bind=engine)

session  = Session()

calendar_year = 2022 # since this is the year I used the transactions were taking place when I defined Transaction_Object() from Table_Skeleton.py
calendar_month = 4 # since this is the month I used the transactions were taking place when I defined Transaction_Object() from Table_Skeleton.py

'''
 Question 1 - Find the top 5 offices with the most sales for that month.

'''

Index(Houses.office_id, Houses.house_id) #applications of composite indexing for faster retreival
#reference --> https://user3141592.medium.com/single-vs-composite-indexes-in-relational-databases-58d0eb045cbe
Index(Sales.date_sold, Sales.price)

firstAnswer = session.query(
    Offices.office_address, 
    func.sum(Sales.price)).filter(
    extract('year',Sales.date_sold) == calendar_year, extract('month', Sales.date_sold) == calendar_month).join(
    Houses,Houses.house_id == Sales.house_id).join(
    Offices,Offices.office_id == Houses.office_id).group_by(
    Houses.office_id).order_by(func.sum(Sales.price).desc()).limit(5).all()

print("firstAnswer = ", firstAnswer)

'''
#Question 2 - Find the top 5 estate agents who have sold the most (include their contact details and their sales details so that it is easy contact them and congratulate them).

'''

Index(Sales.agent_id)
secondAnswer = session.query(Agent.agent_firstName, Agent.agent_lastName, Agent.agent_email,
    Agent.agent_phoneNumber, func.sum(Sales.price)).filter(
    extract('year', Sales.date_sold) == calendar_year, extract('month', Sales.date_sold) == calendar_month).join(
    Agent,Agent.agent_id == Sales.agent_id).group_by(
    Sales.agent_id).order_by(func.sum(Sales.price).desc()).limit(5).all()
print("secondAnswer = ", secondAnswer)

'''
#Question 3 - Calculate the commission that each estate agent must receive and store the results in a separate table. For all houses that were sold that month, calculate the average number of days that the house was on the market.

'''

Index(Sales.sales_commission)
select_commission_by_month_and_year = session.query(Sales.agent_id, func.sum(Sales.sales_commission)).filter(
    extract('year', Sales.date_sold) == calendar_year, extract('month', Sales.date_sold) == calendar_month).group_by(
    Sales.agent_id)

result_to_be_inserted = insert(Commission_Sum).from_select(names=['link_id', 'commision'],select=select_commission_by_month_and_year)
session.execute(result_to_be_inserted)
session.commit()

thirdAnswer_a = session.query(Commission_Sum).all()

thirdAnswer_b = session.query(func.avg(func.julianday(Sales.date_sold) - func.julianday(Listing_For_Sale.listing_date))).filter(
    extract('year', Sales.date_sold) == calendar_year, extract('month', Sales.date_sold) == calendar_month).join(
    Listing_For_Sale, Listing_For_Sale.house_id == Sales.house_id).first()


print("thirdAnswer_a = ", thirdAnswer_a)
print("thirdAnswer_b = ", thirdAnswer_b)


'''
#Question 4 - For all houses that were sold that month, calculate the average selling price.

'''

fourthAnswer = session.query(func.avg(Sales.price)).filter(
    extract('year', Sales.date_sold) == calendar_year, extract('month', Sales.date_sold) == calendar_month).first()

print("query4", fourthAnswer)



