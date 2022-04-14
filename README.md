# DB162

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
  -

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
