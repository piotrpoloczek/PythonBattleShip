'''
This module should return empty board for placement the ships, and for shooting the ships
It has also the functions for printing the board.

'''

from errors_messages import board_size_error


def return_empty_board(board_size):
    '''
    Return empty board
    '''
    return [['0' for i in range(0, board_size)] for b in range(0, board_size)]

def ask_user_dimesion():
    '''
    ask for user dimesnion of table
    '''
    return input("Choose the size of the board: ")

def validate_user_dimension():
    pass

def return_user_dimension():
    pass

def return_board():
    '''
    return list of lists
    '''
    pass

def display_board(board):
    '''
    only for printing the list of lists
    '''
    for row in board:
        for item in row:
            print(item, end='')
        print()

def prepare_empty_board():
    user_choice = True
    while user_choice:
        user_dimension = ask_user_dimesion()
        if validate_user_dimension:
            board_size = return_user_dimension()
            user_choice = False
        else:
            board_size_error()
    
    return return_empty_board(board_size)

    


#board_battle = return_empty_board(20, 10)
#display_board(board_battle)
#print(board_battle)
test_board_1 = [['0', '0', '0', '0'],['0', '0', '0', '0'],['X', '0', 'X', '0'],['0', 'X', 'X', 'X']]
