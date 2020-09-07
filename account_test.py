import unittest
import pyperclip
from account import User
from account import Account
class testUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''      
        Set up method to run before each test cases.
        '''
        self.new_user = User("PhoebeNjeri","gichuhi4") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.lockname,"PhoebeNjeri")
        self.assertEqual(self.new_user.password,"gichuhi4")
        def test_save_user(self):
        '''
        test_save_user test case to test if the user's object is saved into the user's list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):

	    '''
		delete user's account
		'''

	    self.new_user.save_user()

	    test_user=User("PhoebeNjeri","gichuhi4")
	    test_user.save_user()
	    self.new_user.delete_user()
	    self.assertEqual(len(User.user_list),1)
        class testAccounts(unittest.TestCase):
    '''
    Test class that defines test cases for the account class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def test_check_user(self):
    
        '''
		Function to test whether the login in function check_user works as expected
		'''
        self.new_user = User("PhoebeNjeri","gichuhi4")
        self.new_user.save_user()
        user2 = User('Allan','timmy')
        user2.save_user()

        for user in User.user_list:
            if user.lockname == user2.lockname and user.password == user2.password:
	            current_user = user.lockname
        return current_user

        self.assertEqual(current_user,Account.check_user(user2.password,user2.lockname))

        def setUp(self):
        '''      
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Github","PhoebeNjeri","gichuhi4")



    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.somedia,"Github")
        self.assertEqual(self.new_account.username,"PhoebeNjeri")
        self.assertEqual(self.new_account.accpassword,"gichuhi4")
        




 