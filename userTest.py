import unittest

from user import User

class TestUser(unittest.TestCase):
    
     def setUp(self):
         
         
        self.new_user = User("alvin","malvin","alma","alma")
          
          
          
     def test_init(self):
         '''
         test to initialize and instantiate the methods
         '''
         self.assertEqual(self.new_user.first_name,"alvin")
         self.assertEqual(self.new_user.last_name,"malvin")
         self.assertEqual(self.new_user.password,"alma")
         self.assertEqual(self.new_user.confirmation_password,"alma")
     
               
         
     def test_save_user(self):
         '''
         to show whether the user's details can be saved
         '''
         self.new_user.save_user() 
         self.assertEqual(len(User.user_list),1)
        
     def test_save_multiple_user(self):
         '''
         test to enable save for multiple users
         '''
         self.new_user.save_user()
         test_user = User("Twitter","alvin","alma","alma") 
         test_user.save_user()
         self.assertEqual(len(User.user_list),2)
    
     def tearDown(self):
         '''
         cleans up the user_list after each test is run
         '''
         User.user_list = []

     def test_delete_user(self):
         '''
         test to delete_user
         '''
         self.new_user.save_user()
         test_user = User("Twitter","alvin","alma","alma") 
         test_user.save_user()

         self.new_user.delete_user()
         self.assertEqual(len(User.user_list),1)
     def test_find_user_by_username(self):
         '''
         to find user by username
         '''

         self.new_user.save_user()
         test_user = User("Twitter","alvin","alma","alma")
         test_user.save_user()

         found_user = User.find_by_name("alvin")

         self.assertEqual(found_user.last_name,test_user.last_name)
     def test_user_exist(self):
         '''
         test to affirm that the user exists
         '''

         self.new_user.save_user()
         test_user = User("Twitter","alvin","alma","alma") 
         test_user.save_user()

         user_exist = User.user_exist("malvin")

         self.assertTrue(user_exist)
     def test_display_names(self):
         '''
         test to display all current users
         '''

         self.assertEqual(User.display_names(),User.user_list)
   
     
if __name__ ==  '__main__':
 unittest.main()