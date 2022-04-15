'''
Test code for the Tables Created! 

'''
from datetime import datetime
import os, sys
sys.path.insert(0, os.getcwd())

import unittest
from Table_Skeleton import Houses, Agent, Commission_Sum, Agent_to_Office_Link, Transactor, Offices, Price_Sum, Sales, Listing_For_Sale, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Session = sessionmaker(bind=engine)  #binding the engine to make sure that we are adding data to the same DB we created in Table_Skeleton.py
session = Session() # initializing session

Base = declarative_base()

class TestQuery(unittest.TestCase):

### 1 testing Agent Table

    def Add_Into_Agent(self): # checks if the user inserts additional column data
        try:    
            self.agent_inst = Agent("Iron", "Man", "ironman@gmail.com", 3138907896)
            session.add(self.agent_inst)
            session.commit()
        except TypeError:
            raise Exception('The data added does not comply with the Table instantiation defined rules!')

    def testAgent_Table(self): # checks if data is properly added 

        what_is_expected = self.agent_inst
        result_we_got = self.session.query(Agent).all()
        if what_is_expected in result_we_got:
                self.assertEqual(result_we_got, what_is_expected)
        else:
            self.assertEqual(result_we_got, what_is_expected)
  
    def testAgent_Table(self): # checks if we can properly delete

        what_is_expected = []
        self.session.query(Agent).filter(Agent.house_id==1).delete()
        result_we_got = self.session.query(Agent).all()
        self.assertEqual(result_we_got, what_is_expected)

    def testAgent_Table(self): # checks for type error from Add_Into_Agent()
        with self.assertRaises(Exception) as context:
            self.Add_Into_Agent(self)
        self.assertTrue(context.exception, "The data added does not comply with the Table instantiation defined rules!")


### 2 testing Agent_to_Office_Link table

    def Add_Into_Agent_to_Office_Link_Table(self): # checks if the user inserts additional column data
        try:
            self.link_inst = Agent_to_Office_Link(6, 2)
            session.add(self.link_inst)
            session.commit()
        except TypeError:
            raise Exception('The data added does not comply with the Table instantiation defined rules!')

    def testAgent_to_Office_Link_Table(self): # checks if data is properly added 
        what_is_expected = self.link_inst
        result_we_got = self.session.query(Agent_to_Office_Link).all()
        if what_is_expected in result_we_got:
            self.assertEqual(result_we_got, what_is_expected)
        else:
            self.assertEqual(result_we_got, what_is_expected)

    def testAgent_to_Office_Link_Table(self):  # checks if we can properly delete
        what_is_expected = []
        self.session.query(Agent_to_Office_Link).filter(Agent_to_Office_Link.link_id==1).delete()
        result_we_got = self.session.query(Agent_to_Office_Link).all()
        self.assertEqual(result_we_got, what_is_expected)
        
    def testAgent_to_Office_Link_Table(self): # checks for type error from Add_Into_Agent_to_Office_Link_Table()
        with self.assertRaises(Exception) as context:
            self.Add_Into_Agent_to_Office_Link_Table(self)
        self.assertTrue(context.exception, "The data added does not comply with the Table instantiation defined rules!")

 
### 3 testing Transactor table

    def Add_Transactor_Table(self): # checks if the user inserts additional column data
        try:
            self.trans_inst = Transactor("Bete", "Asrat", "bete@gmail.com", 2128909879)
            session.add(self.link_inst)
            session.commit()
        except TypeError:
            raise Exception('The data added does not comply with the Table instantiation defined rules!')

    def testTransactor_Table(self): # checks if data is properly added 
        what_is_expected = self.trans_inst
        result_we_got = self.session.query(Transactor).all()
        if what_is_expected in result_we_got:
            self.assertEqual(result_we_got, what_is_expected)
        else:
            self.assertEqual(result_we_got, what_is_expected)
    
    def testTransactor_Table(self):  # checks if we can properly delete
        what_is_expected = []
        self.session.query(Transactor).filter(Transactor.transactor_id==1).delete()
        result_we_got = self.session.query(Transactor).all()
        self.session.commit()
        self.assertEqual(result_we_got, what_is_expected)
        
    def testTransactor_Table(self): # checks for type error from Add_Transactor_Table()
        with self.assertRaises(Exception) as context:
            self.Add_Transactor_Table(self)
        self.assertTrue(context.exception, "The data added does not comply with the Table instantiation defined rules!")


### 4 testing Offices table

    def Add_Offices_Table(self): # checks if the user inserts additional column data
        try:
            self.link_inst = Offices("San Frnacisco, CA")
            session.add(self.link_inst)
            session.commit()
        except TypeError:
            raise Exception('The data added does not comply with the Table instantiation defined rules!')

    def testOffices_Table(self):  # checks if data is properly added 
        what_is_expected = self.link_inst
        result_we_got = self.session.query(Offices).all()
        if what_is_expected in result_we_got:
            self.assertEqual(result_we_got, what_is_expected)
        else:
            self.assertEqual(result_we_got, what_is_expected)
 
    def testOffices_Table(self):  # checks if we can properly delete
        what_is_expected = []
        self.session.query(Offices).filter(Offices.office_id==1).delete()
        result_we_got = self.session.query(Offices).all()
        self.session.commit()
        self.assertEqual(result_we_got, what_is_expected)
        
    def testOffices_Table(self):  # checks for type error from Add_Offices_Table()
        with self.assertRaises(Exception) as context:
            self.Add_Offices_Table(self)
        self.assertTrue(context.exception, "The data added does not comply with the Table instantiation defined rules!")

### 5 testing Sales table

    def Add_Sales_Table(self): # checks if the user inserts additional column data
        try:
            #buyer_id, agent_id, house_id, price, date_sold, sales_commission
            self.link_inst = Sales(2, 3, 5, 890000, datetime(2022, 4, 13))
            session.add(self.link_inst)
            session.commit()
        except TypeError:
            raise Exception('The data added does not comply with the Table instantiation defined rules!')

    def testSales_Sum_Table(self):  # checks if data is properly added 
        what_is_expected = self.link_inst
        result_we_got = self.session.query(Sales).all()
        if what_is_expected in result_we_got:
            self.assertEqual(result_we_got, what_is_expected)
        else:
            self.assertEqual(result_we_got, what_is_expected)

    def testSales_Sum_Table(self): # checks if we can properly delete

        what_is_expected = []
        self.session.query(Sales).filter(Sales.sale_id==1).delete()
        result_we_got = self.session.query(Sales).all()
        self.session.commit()
        self.assertEqual(result_we_got, what_is_expected)
        
    def testSales_Sum_Table(self): # checks for type error from Add_Sales_Table()

        with self.assertRaises(Exception) as context:
            self.Add_Sales_Table(self)
        self.assertTrue(context.exception, "The data added does not comply with the Table instantiation defined rules!")


### 6 testing Add_Listing_For_Sale_Table table

    def Add_Listing_For_Sale_Table(self): # checks if the user inserts additional column data
        try:
            self.lists_inst = Listing_For_Sale(777000, 2, 4, 5, datetime(12,4,15),False)
            session.add(self.sales_inst)
            session.commit()
        except TypeError:
            raise Exception('The data added does not comply with the Table instantiation defined rules!')

    def testListing_For_Sale_Table(self):  # checks if data is properly added 
        what_is_expected = self.lists_inst
        result_we_got = session.query(Listing_For_Sale).all()

        if what_is_expected in result_we_got:
            self.assertEqual(result_we_got, what_is_expected)
        else:
            self.assertEqual(result_we_got, what_is_expected)
        
    def testListing_For_Sale_Table(self): # checks if we can properly delete
        what_is_expected = []
        session.query(Listing_For_Sale).filter(Listing_For_Sale.listing_id==1).delete()
        result_we_got = session.query(Listing_For_Sale).all()
        self.assertEqual(result_we_got, what_is_expected)
        
    def testListing_For_Sale_Table(self): # checks for type error from Add_Listing_For_Sale_Table()
        with self.assertRaises(Exception) as context:
            self.Add_Listing_For_Sale_Table(self)
        self.assertTrue(context.exception, "The data added does not comply with the Table instantiation defined rules!")


### 7 testing Houses table

    def Add_House_Table(self): # checks if the user inserts additional column data
        try:
            self.lists_inst = Houses(95104, 2, 4, 600, 2)
            session.add(self.sales_inst)
            session.commit()
        except TypeError:
            raise Exception('The data added does not comply with the Table instantiation defined rules!')

    def testHouse_Table(self):  # checks if data is properly added 
        what_is_expected = self.lists_inst
        result_we_got = session.query(Houses).all()

        if what_is_expected in result_we_got:
            self.assertEqual(result_we_got, what_is_expected)
        else:
            self.assertEqual(result_we_got, what_is_expected)
        
    def testHouse_Table(self):  # checks if we can properly delete
        what_is_expected = []
        session.query(Houses).filter(Houses.listing_id==1).delete()
        result_we_got = session.query(Houses).all()
        self.assertEqual(result_we_got, what_is_expected)
        
    def testHouse_Table(self):  # checks for type error from Add_House_Table()
        with self.assertRaises(Exception) as context:
            self.Add_House_Table(self)
        self.assertTrue(context.exception, "The data added does not comply with the Table instantiation defined rules!")
        
### tearing down the database

    def deleteDB(self):
        Houses.__table__.drop(engine)
        Agent.__table__.drop(engine)
        Agent_to_Office_Link.__table__.drop(engine)
        Transactor.__table__.drop(engine)
        Offices.__table__.drop(engine)
        Price_Sum.__table__.drop(engine)
        Sales.__table__.drop(engine)
        Listing_For_Sale.__table__.drop(engine)
        Commission_Sum.__table__.drop(engine)
        
if __name__ == '__main__':
    unittest.main()
