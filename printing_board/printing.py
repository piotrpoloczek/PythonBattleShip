from prettytable import PrettyTable
from tabulate import tabulate
import os


def add_left_header(board):
    header = [chr(i) for i in range(65, 65+len(board))]

    for index_row, row in enumerate(board):
        row.insert(0, header[index_row])

def add_upper_header(board):
    upper_header = [i for i in range(0, len(board) + 1)]
    upper_header[0] = ''
    board.insert(0, upper_header)


def print_board(board):
    new_board = board[:]
    add_left_header(new_board)
    add_upper_header(new_board)
    os.system('cls')
    print(tabulate(new_board))