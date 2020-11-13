import unittest #importing the unittest module
from credential import Credential #importing the credential class


class TestCredential(unittest.TestCase):
    '''
    Test class that defines text cases for the credential class behaviour
    
    Args:
        unittest.TestCase: TextCase that helps creating text cases
    '''


    def setUp(self):
        '''
        Set up method that run before each test cases
        '''
       
        self.new_credential = Credential("Alvin","Twitter","123456") # create credential object

    
    def test_init(self):
        '''
        Test to check if the object is initialized properly
        '''
        

        self.assertEqual(self.new_credential.username,"Alvin")
        self.assertEqual(self.new_credential.account_name,"Twitter")
        self.assertEqual(self.new_credential.password,"123456")
        

    def test_save_credential(self):
       '''
       test to check if the credential object is saved in the credential list
       '''
        self.new_credential.save_credential() # saving the new account
        self.assertEqual(len(Credential.credential_list),1)  


    def tearDown(self):
            '''
            test to clean up after each test run
            '''
            Credential.credential_list = []    


    def test_save_multiple_credential(self):
            '''
            test to check if we can save multiple credential in the credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user") 
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)


    def test_delete_credential(self):
            '''
            to delete credentials
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user") 
            test_credential.save_credential()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credential.credential_list),1) 

    def test_find_credential_by_credential_name(self):
       '''
       to find credential by credential name
       '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","user") 
        test_credential.save_credential()

        found_credential = Credential.find_by_name("Test")

        self.assertEqual(found_credential.username,test_credential.username)  



    def test_credential_exists(self):
        '''
        to check whether the credential exists
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","user") # new account
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("Alvin")
        self.assertTrue(credential_exists)    
        
                       


if __name__ == '__main__':
    unittest.main()  