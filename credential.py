class Credential:
    """
    Class that generates new instances of users.
    """
    credential_list = [] #empty credential list

    def save_credential(self):

        '''
        save_credential method saves credential objects into credential list.
        '''

      

        Credential.credential_list.append(self)    


    
    @classmethod
    def find_by_name(cls,name):

        '''
       Method that takes in a name returns a credential that matches that name.
       
       Args:
            name: name to search for
        Returns:
            Credential of the person that matches the name.
            
        '''
        for credential in cls.credential_list:
            if credential.account_name == name:
                return credential  


    @classmethod
   

    @classmethod
    def display_credential(cls):  
        '''
        method that returns credentials list
        '''
       
        return cls.credential_list
    
    def delete_credential(self):

        '''
        delete credential method delete saved credential objects from credential list.
        '''


      

        Credential.credential_list.remove(self)


    def __init__(self,account_name,username,password):
        '''
       _init_method that help us define properties for our objects.
       
       Args:
            account_name:New credention account name.
            username:New credention username.
            password:New credential password.

        '''
        #docstring removed for simplicity

        self.username = username
        self.account_name = account_name
        self.password = password