import board
"""
Implement the placement phase of the battleship program where players can place ships on a board.
input similar to [['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0']]
"""

BOARD_SIZE = 5


def create_boad():
    board = []
    for i in range(BOARD_SIZE):
        sub_board = []
        for j in range(BOARD_SIZE):
            sub_board.append(('0'))
        board.append(sub_board)
    print(board)

def check_available_coordinates(board):
    available_coordinates = []
    for row_index, row in enumerate(board):
        for item_index, item in enumerate(row):
            if item == '0':
                available_coordinates.append((row_index, item_index))
    return available_coordinates

def ask_user_input():
    pass

def validate_user_input():
    pass

create_boad()

# if __name__ == '__main__':
#     battleship_board = board.return_empty_board(5, 5)
#     test_board_1 = [['0', '0', '0', '0'],['0', '0', '0', '0'],['X', '0', 'X', '0'],['0', 'X', 'X', 'X']]
#     test_board_2 = [['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0']]
#     print(check_available_coordinates(battleship_board))
#     print(check_available_coordinates(test_board_1))
#     print(check_available_coordinates(test_board_2))