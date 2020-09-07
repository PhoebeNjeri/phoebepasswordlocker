import string
import pyperclip
import random
class User:
    """
    Class that generates new instances of user's information
    """
    
    user_list =[]

    def __init__(self,lockname,password):

        self.lockname = lockname
        self.password = password

    def save_user(self):

        '''
        save_user method saves user's information objects into user_list
        '''

        User.user_list.append(self)
        def delete_user(self):
        '''
        function to   delete user instance
        '''
        User.user_list.remove(self)


class Account:

    """
    Class that generates new instances of user's accounts
    """
    
    account_list =[]
    user_account_list=[]
class Account:

    """
    Class that generates new instances of user's accounts
    """
    
    account_list =[]
    user_account_list=[]

    @classmethod
    def check_user(cls,lockname,password):
        '''
        method that checks if the name and password matches
        '''
        current_user=''
        for user in User.user_list:
            if(user.lockname == lockname and password == password):
                current_user = user.lockname
        return current_user
    
    def __init__(self,somedia,username,accpassword):

        self.somedia = somedia
        self.username = username
        self.accpassword = accpassword
def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)

    def generate_newpassword(size=8,char=string):
        '''
        function to generate an 8 character password
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass

    @classmethod
    def display_accounts(cls,somedia):
        '''
        method that returns the account list
        '''
        user_account_list=[]
        for account in cls.account_list:
            # if account.somedia == somedia
            user_account_list.append(account)
        return user_account_list
