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
    def credential_exist(cls,name):

        '''
       Method that checks if a credential exist from the credential list.
       
       Args:
            name: name to search if it exists
        Returns:
            Boolean: True or false depending if the credential exists.
            
        '''
       
        for credential in cls.credential_list:
            if credential.account_name == name:
                    return True

        return False

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


    