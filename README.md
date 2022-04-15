# DB162

Steps to run this program:

MacOS >

Requirements

- pip3 install sqlalchemy
- python_version = "3.9"

Steps:

1.  Open terminal (if you are using Visual Studuo Code, the keyboard shortcut will be "ctrl~")
2.  change directory to DB162(if it is not opened in this directory already) - type > cd DB162
3.  chnage directory to backend folder - type > cd backend
4.  initilize virtual environment - type > pipenv shell
5.  run the Table_Skeleton.py file - type > python Table_Skeleton.py
6.  run the Data_Insertion.py file - type > python Data_Insertion.py
7.  run the Required_Queries.py file - type > python Required_Insertion.py
8.  run the test.py file - type > python test.py

Tables

- Agent
  Columns

  - agent_id (int) - PRIMARY KEY
  - agent_firstName (string)
  - agent_lastName (string)
  - agent_email (string)
  - agent_phoneNumber (big_int)

- Transactor
  Columns

  - transactor_id(int) - PRIMARY KEY
  - transactor_firstName(string)
  - transactor_lastName(string)
  - transactor_email(string)
  - transactor_phoneNumber(big_int)

- Offices
  Columns

  - office_id(int) - PRIMARY KEY
  - office_address(string)

- Houses
  Columns

  - house_id (int) PRIMARY KEY
  - house_address (string)
  - number_of_bedrooms (int)
  - number_of_bathrooms (int)
  - area_in_squareMeter (int)
  - office_id (int) - ForeignKey('Offices.office_id')

- Sales
  Columns

  - sale_id (int) - PRIMARY KEY
  - buyer_id (int) - ForeignKey('Transactor.transactor_id')
  - agent_id (int) - ForeignKey('Agent.agent_id')
  - house_id (int) - ForeignKey('Houses.house_id')
  - price (int)
  - date_sold (Date)

- Price_Sum
  Columns

  - price_id (int) - PRIMARY KEY
  - price_sum (int)

- Commission_Sum
  Columns

  - commission_id(int) - PRIMARY KEY
  - link_id(int) -
  - commision(int)

- Listing_For_Sale
  Columns

  - listing_id(int) - PRIMARY KEY
  - house_id(int) - ForeignKey('Houses.house_id')
  - seller_id(int) - ForeignKey('Transactor.transactor_id')
  - agent_id(int) - ForeignKey('Agent.agent_id')
  - listing_date(datetime)
  - price(int)
  - isSold(bool)

- Agent_Office_Link
  Columns
  - link_id(int)
  - office_id(int)
  - agent_id(int)

####

Optional cool features to explore if you are opening this with VS Code:-

VS Code has a SQLite Explorer that you can install by following simple steps -

- click on the "Extentions" button on the left side of VSCode
- search "SQLite"
- click install
- Now, right-click on the db (moneyflow.db), then click "open database."
- Now you should be seeing your database apearing at the bottom lefthand corner(under SQLITE EXPLORER)
- there, you can click on each table listed within the db, and you will be able to view a beautiful table.
