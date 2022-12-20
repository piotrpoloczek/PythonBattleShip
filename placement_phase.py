#import board
"""
Implement the placement phase of the battleship program where players can place ships on a board.
input similar to [['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0']]
"""

BOARD_SIZE = 6


def create_boad():
    board = []
    for i in range(BOARD_SIZE):
        sub_board = []
        for j in range(BOARD_SIZE):
            sub_board.append(('0'))
        board.append(sub_board)
    print(board)


def check_coordinate_is_in_board(coordinate_x,coordinate_y):
    return 0 <= coordinate_x <= BOARD_SIZE-1 and 0 <= coordinate_y <= BOARD_SIZE-1


def check_coordinate_is_free(board,coordinate_x,coordinate_y):
    try:
        return board[coordinate_x][coordinate_y] == '0'
    except IndexError:
        return False


def translate_coordinates(coordinates):
    coordinate_x = 0
    coordinate_y = 0
    letter = coordinates[0].lower()
    possible = list(map(chr, range(97, 128)))
    for i in possible:
        if i == letter:
            break
        coordinate_x += 1

    try:
        coordinate_y = int(coordinates[1:])
    except ValueError:
        return False

    return (coordinate_x,coordinate_y-1)


def ask_for_coordinates(board):
    while True:
        coordinates = input('enter coordinates')
        coordinate_x, coordinate_y= translate_coordinates(coordinates)
        if check_coordinate_is_in_board(coordinate_x,coordinate_y) and check_coordinate_is_free(board,coordinate_x,coordinate_y):
            return (coordinate_x,coordinate_y)
        else:
            print('Bad coordinates')
    


def ship_placement(board):
    pass



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

print(ask_for_coordinates(board=[['0', '0', '0', '0','0'],['0', '0', '0', '0','0'],['0', '0', '0', '0','0'],['0', '0', '0', '0','0'],['0', '0', '0', '0','0']]))



# if __name__ == '__main__':
#     battleship_board = board.return_empty_board(5, 5)
#     test_board_1 = [['0', '0', '0', '0'],['0', '0', '0', '0'],['X', '0', 'X', '0'],['0', 'X', 'X', 'X']]
#     test_board_2 = [['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0']]
#     print(check_available_coordinates(battleship_board))
#     print(check_available_coordinates(test_board_1))
#     print(check_available_coordinates(test_board_2))