'''
All FILE EDIT

'''
import os, sys
sys.path.insert(0, os.getcwd())

import unittest
from Table_Skeleton import Houses, Agent, Commission_Sum, Agent_to_Office_Link, Transactor, Offices, Price_Sum, Sales, Listing_For_Sale, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Session = sessionmaker(bind=engine)  #binding the engine to make sure that we are adding data to the same DB we created in Table_Skeleton.py
session = Session() # initializing session

Base = declarative_base()

def test_Unexpected_Input(self):
    try:
        self.testHouse2 = Houses(93908, 3, 5, 1000, 1)
        self.session.add(self.testHouse2)
    except TypeError:
        raise Exception('The data added does not comply with the Table instantiation defined rules!')

class TestQuery(unittest.TestCase):
    #     
    # Test if 
    def testHouse_Table(self):
        what_is_expected = [self.example_house]
        result_we_got = self.session.query(Houses).all()
        self.session.commit()
        self.assertEqual(result_we_got, what_is_expected)
        
    # Test if 
    def testHouse_Table(self):
        what_is_expected = []
        self.session.query(Houses).filter(Houses.house_id==1).delete()
        result_we_got = self.session.query(Houses).all()
        self.session.commit()
        self.assertEqual(result_we_got, what_is_expected)
        
    # Test 
    def testHouse_Table(self):
        with self.assertRaises(Exception) as context:
            test_Unexpected_Input(self)
        self.assertTrue(context.exception, 'The data added does not comply with the Table instantiation defined rules!')

    # tearing down the database
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