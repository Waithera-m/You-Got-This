import unittest
from app.models import User

class UserClassTest(unittest.TestCase):

    '''
    class inherits from TestCase and facilitates the creation of test units
    '''
    def setUp(self):

        '''
        function runs before every test
        '''
        self.new_user = User(password = 'allonsy')

    def test_password_setter(self):

        '''
        function checks if user's password is hashed
        '''
        self.assertTrue(self.new_user.password_hash is not None)
    
    def test_no_access_password(self):

        '''
        function tests if app raises AttributeError when one tries to access the password property
        '''
        with self.assertRaises(AttributeError):
            self.new_user.password
    
    def test_password_verification(self):

        '''
        function checks if app verifies hashed passwords
        '''
        self.assertTrue(self.new_user.verify_password('allonsy'))