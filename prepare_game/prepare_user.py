'''
This module should return empty board for placement the ships, and for shooting the ships
It has also the functions for printing the board.

'''

from errors_messages import invallid_username_error


def ask_user_name():
    '''
    ask for user name in game
    '''
    return input("Choose your name in this game: ")

def validate_user_name(user_input):
    if user_input.isalpha():
        return True 
    return False 

def prepare_user_name():
    user_choice = True
    while user_choice:
        user_name = ask_user_name()
        if validate_user_name:
            user_choice = False
        else:
            invallid_username_error()
    
    return user_name

    