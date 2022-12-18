'''
create the board
ask user for dimensionf of table

return list of list with dimesnion from user
[['.', '.', ]]

verifivation that len(list) < 10
'''

def return_empty_board(width, lenght):
    '''
    return empty list of list
    '''
    return [['0' for i in range(0, width)] for b in range(0, lenght)]

def ask_user_dimesion():
    '''
    ask for user dimesnion of table
    '''
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

#board_battle = return_empty_board(20, 10)
#display_board(board_battle)
#print(board_battle)
test_board_1 = [['0', '0', '0', '0'],['0', '0', '0', '0'],['X', '0', 'X', '0'],['0', 'X', 'X', 'X']]
