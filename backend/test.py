'''
Test code for the Tables Created! 

'''
from datetime import datetime

import unittest
from Table_Skeleton import Houses, Agent, Commission_Sum, Agent_to_Office_Link, Transactor, Offices, Price_Sum, Sales, Listing_For_Sale, engine
from sqlalchemy.orm import sessionmaker


class TestBlock(unittest.TestCase):

    ### 1 testing Agent Table

    def setUp(self): # runs before everything else
        Session = sessionmaker(bind=engine)  #binding the engine to make sure that we are adding data to the same DB we created in Table_Skeleton.py
        self.session = Session() # initializing session

        
    def test_Add_Into_Agent(self): # tests for  TypeError or more than allowed column instance
        try:    
            self.agent_inst = Agent("Iron", "Man", "ironman@gmail.com", 3138907896)
            self.session.add(self.agent_inst)
            self.session.commit()

        except TypeError:
            raise Exception('The data added does not comply with the Table instantiation defined rules!')


    def test_Agent_Table(self): # checks if data is properly added 
        expected1 = "Tron"
        expected2 = "Man"
        expected3 = "ironman@gmail.com"
        expected4 = 3138907896
        result_we_got1 = self.session.query(Agent.agent_firstName).all()
        result_we_got2 = self.session.query(Agent.agent_lastName).all()
        result_we_got3 = self.session.query(Agent.agent_email).all()
        result_we_got4 = self.session.query(Agent.agent_phoneNumber).all()
        if expected1 in result_we_got1:
            self.assertEqual(expected1, result_we_got1)
        if expected2 in result_we_got2:
            self.assertEqual(expected2, result_we_got2)
        if expected3 in result_we_got3:
            self.assertEqual(expected3, result_we_got3)
        if expected4 in result_we_got4:
            self.assertEqual(expected4, result_we_got4)


    def test_Add_Transactor_Table(self): # checks if the user inserts additional column data
        try:
            self.trans_inst = Transactor("Bete", "Asrat", "bete@gmail.com", 2128909879)
            self.session.add(self.trans_inst)
            self.session.commit()

        except TypeError:
            raise Exception('The data added does not comply with the Table instantiation defined rules!')
  
    def test_Add_Into_Agent_to_Office_Link_Table(self): # checks if the user inserts additional column data
        try:
            self.link_inst = Agent_to_Office_Link(6, 2)
            self.session.add(self.link_inst)
            self.session.commit()
        except TypeError:
            raise Exception('The data added does not comply with the Table instantiation defined rules!')

    def test_Add_Offices_Table(self): # checks if the user inserts additional column data
        try:
            self.link_inst = Offices("San Frnacisco, CA")
            self.session.add(self.link_inst)
            self.session.commit()
        except TypeError:
            raise Exception('The data added does not comply with the Table instantiation defined rules!')

    def test_Add_Listing_For_Sale_Table(self): # checks if the user inserts additional column data
        try:
            self.lists_inst = Listing_For_Sale(777000, 2, 4, 5, datetime(12,4,15),False)
            self.session.add(self.lists_inst)
            self.session.commit()
        except TypeError:
            raise Exception('The data added does not comply with the Table instantiation defined rules!')

    def test_Add_House_Table(self): # checks if the user inserts additional column data
        try:
            self.house_inst = Houses(95104, 2, 4, 600, 2)
            
            self.session.add(self.house_inst)
            self.session.commit()
        except TypeError:
            raise Exception('The data added does not comply with the Table instantiation defined rules!')


if __name__ == '__main__':
    unittest.main()
