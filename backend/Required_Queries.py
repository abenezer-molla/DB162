
from Table_Skeleton import Agent, Agent_to_Office_Link, Sales, Transactor, Offices, Price_Sum, Commission_Sum, Houses, Sales, Listing_For_Sale
#Needs Real Work Here


year = 2022
month = 12

# Question 1 - Find the top 5 offices with the most sales for that month.

db.Index("idx1",Houses.office_id, Houses.house_id)       # uses composite indexing to index the tables
db.Index("idx2",Sales.date_sold, Sales.price)
query1 = db.session.query(
    Offices.office_address, 
    db.func.sum(Sales.pr)).filter(
    db.extract('year',Sales.date_sold) == year, db.extract('month', Sales.sale_date) == month).join(
    Houses,Houses.house_id == Sales.house_id).join(
    Offices,Offices.office_id == Houses.office_id).group_by(
    Houses.office_id).order_by(db.func.sum(Sales.price).desc()).limit(5).all()
print(query1)

#Question 2 - Find the top 5 estate agents who have sold the most (include their contact details and their sales details so that it is easy contact them and congratulate them).

db.Index('idx3', Sales.estate_agent_id)
query2 = db.session.query(Agent.agent_firstName, Agent.agent_lastName, Agent.agent_email,
    Agent.agent_phoneNumber, db.func.sum(Sales.price_sold)).filter(
    db.extract('year', Sales.date_sold) == year, db.extract('month', Sales.date_sold) == month).join(
    Agent,Agent.agent_id == Sales.agent_id).group_by(
    Sales.agent_id).order_by(db.func.sum(Sales.sale_price).desc()).limit(5).all()
print(query2)

#Question 3 - Calculate the commission that each estate agent must receive and store the results in a separate table. For all houses that were sold that month, calculate the average number of days that the house was on the market.

db.Index("idx4", Sales.estate_agent_commission)
to_select = db.session.query(Sales.agent_id, db.func.sum(Sales.commission)).filter(
    db.extract('year', Sales.date_sold) == year, db.extract('month', Sales.date_sold) == month).group_by(
    Sales.estate_agent_id)
i = db.insert(Commission_Sum).from_select(names=['agent_id', 'commission'],select=to_select)
db.session.execute(i)
query3a = db.session.query(Commission_Sum).all()

query3b = db.session.query(db.func.avg(db.func.julianday(Sales.sale_date) - db.func.julianday(Listing_For_Sale))).filter(
    db.extract('year', Sales.sale_date) == year, db.extract('month', Sales.sale_date) == month).join(
    Listing_For_Sale, Listing_For_Sale.house_id == Sales.house_id).first()

print(query3a)
print(query3b)

#Question 4 - For all houses that were sold that month, calculate the average selling price.

query4 = db.session.query(db.func.avg(Sales.sale_price)).filter(
    db.extract('year', Sales.sale_date) == year, db.extract('month', Sales.sale_date) == month).first()

print(query4)



