class User :

    '''
    Class that generate new instances for password
    '''

    user_list = [] #empty user list

    def save_user(self):

        '''
        save_user method saves user objects into user_list.
        '''

      

        User.user_list.append(self) 

    def delete_user(self):

        '''
        delete user method delete saved user objects from user list.
        '''


      

        User.user_list.remove(self)

    
    
    
    
    
    @classmethod
    def find_by_name(cls,name):

        '''
       Method that takes in a name returns a user that matches that name.
       
       Args:
            name: name to search for
        Returns:
            User of the person that matches the name.
            
        '''
        for user in cls.user_list:
            if user.last_name == name:
                return user 

    @classmethod
    def user_exist(cls,name):

        '''
       Method that checks if a user exist from the credential list.
       
       Args:
            name: name to search if it exists
        Returns:
            Boolean: True or false depending if the user exists.
            
        '''
       
        for user in cls.user_list:
            if user.last_name == name:
                    return True

        return False

    @classmethod
    def display_names(cls):  
        '''
        method that returns names list
        '''
       
        return cls.user_list

    def __init__(self,first_name,last_name,password,confirmation_password):
        '''
       _init_method that help us define properties for our objects.
       
       Args:
            first_name:New firstname.
            last_name:New lastname.
            password:New user password.
            confirmation_password:New user confirmation password.

        '''
        #docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.confirmation_password = confirmation_password
    