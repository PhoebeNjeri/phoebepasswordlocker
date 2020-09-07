import pyperclip
from account import User
from account import Account
def create_user(myname,mypassword):
    '''
    Function to create a new user's account
    '''
    new_user = User(myname,mypassword)
    return new_user
    def save_user(user):
    '''
    Function to save the user
    '''
    user.save_user()
def verify_user(lockname,password):
    '''
    function that verifies the existance of user
    '''
    checking_user = Account.check_user(lockname,password)
    return checking_user
def generate_newpassword():
    '''
    function to generate password
    '''
    gen_pas = Account.generate_newpassword()
    return gen_pas 
def create_account(somedia,username,accpassword):
    '''
    Function to add a new social media's account
    '''
    new_account = Account(somedia,username,accpassword)
    return new_account