# --- accounts.py --
# This file contains code for managing your account

accounts = {}  # dictionary where key is the  password and value is User

# Write a function adds user details to accounts


def add_account(name, password):
    """
    Adds the key value pair to the accounts dictionary
    """
    accounts[password] = name


def login(name, password):
    """
    returns true if the password and corresponding name exist in the 
    accounts dicitionary
    """
    if accounts[password] is name:
        return True
    else:
        return False