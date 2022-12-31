'''
This module should return empty board for placement the ships, and for shooting the ships
It has also the functions for printing the board.

'''

def prepare_empty_board(board_size):
    '''
    Return empty board
    '''
    return [['0' for i in range(0, board_size)] for b in range(0, board_size)]
