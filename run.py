#!/usr/bin/env python3.6


import string
import sys
import random
from user import User
from credential import Credential


def create_user(fname,lname,password,confirmation_password):
    """
    Function to create a new user
    """
    new_user = User(fname,lname,password,confirmation_password)
    return new_user




def create_credential(username, account_name, password):
    """
    Function to create  credential user
    """
    new_credential = Credential( username,account_name, password)
    return new_credential


def save_names(user):
    """
    Function to save user
    """
    user.save_user()

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))


def save_credential(credential):
    """
    Function to save credential
    """
    credential.save_credential()

def del_user(user):
    """
    Method that deletes a user
    """
    return user.delete_user(user)

def del_credential(credential):
    """
    Method that delete a credential
    """
    return Credential.delete_credential(credential)

def find_user(name):
    """
    Function that finds user 
    """
    return Credential.find_by_name(name)


def find_credential(name):
    """
    Function that finds credential 
    """
    return Credential.find_by_name(name)

def check_existing_names(name):
    """
    Method that checks whether a particular account and the user exist based on searched account_name
    """
    return User.user_exist(name)


def check_existing_credential(name):
    """
    Method that checks whether a particular account and returns boolean
    """
    return Credential.credential_exist(name)

def display_names():
    """
    Function which displays all saved names
    """
    return Credential.display_credential()


def display_credential():
    """
    Function which displays all saved credentials
    """
    return Credential.display_credential()

def main():
            print("Hello Welcome to Password locker. What is your name?")
            user_name=input()

            print(f"Hello {user_name}. you have to fill in info to create password")
            print('\n')

            print("New Password")
            print("-"*10)

            print("First name..")
            f_name = input()

            print("Last name..")
            l_name = input()

            print(" Password..")
            password = input()

            print("Confirmation Password..")
            confirmation = input()
            if password == confirmation:
                 print("account succesfully created")
            else:
                 print("password incorrect")
                 sys.exit()

            print('\n')
            print("please login with your First name")
            print('\n')
            print("Enter your First name")
            login_name = input()
            print("Enter your Password")
            pwrd = input()


            if pwrd == password and f_name == login_name:
                print("succesfully loged in")
                print('\n')
            else:
                print(f"incorrect username or password:{pwrd} {login_name}")
                sys.exit()

            
            while True:
                print("Use these short codes : np - create a new password, dp - display password, fp -find a password, del - delete password, gp - generate password,ex -exit the contact list")

                short_code = input().lower()

                if short_code == 'np':
                    print("New Password")
                    print("-"*20)

                    print("Username")
                    username = input()

                    print("Account name..")
                    account_name = input()

                    print(" Password..")
                    password = input()

                    save_credential(create_credential(username,account_name,password)) # create and save password
                    print ('\n')
                    print(f"New Credential Name... {username} created")
                    print(f"New Credential Name... {account_name} created")
                    print(f"New Credential Name... {password} created")
                    print("New account created")
                    print ('\n')
                
                elif short_code == 'dp':

                    if display_names():
                            print("Here is a list of all your password")
                            print('\n')

                            for credential in display_names():
                                    print(f"credential name...{credential.username}")
                                    print(f"account name...{credential.account_name}")
                                    print(f"password...{credential.password}")
                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any password saved yet")
                            print('\n')

                elif short_code == 'fp':

                    print("Enter the credential you want to search for")

                    search_name = input()
                    if check_existing_credential(search_name):
                            search_credential = find_credential(search_name)
                            print(f"{search_credential.username} {search_credential.account_name} {search_credential.password}")
                            print('-' * 20)
                            print(f"username...{search_credential.username}")
                            print(f"account name...{search_credential.account_name}")
                            print(f"password...{search_credential.password}")
                    else:
                            print("That password does not exist")

                elif short_code == 'del':

                     print("Enter delete credential name")

                     search_name = input()
                     if check_existing_credential(search_name):
                            Credential = find_credential(search_name)
                            del_credential(Credential)
                            print('\n')
                            print(f"{Credential.account_name} deleted")
                            print('\n')
                            print("credential and password deleted")

                     else:
                            print("credential name does not exist")

                elif short_code == "gp":
                     print("print credential name")
                     account_name = input()
                     print("enter number of length of password to generate")
                     size = int(input())
                     password=pw_gen(size)
                     save_credential(create_credential(username,account_name,password))
                     print('\n')
                     print(f"password is created...{password}")
                     print('\n')
                
                elif short_code == "ex":
                    print("Bye .......")
                    break
                else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()                   




                
                    








