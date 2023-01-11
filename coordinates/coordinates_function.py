from printing_board.printing import print_board



def check_coordinate_is_in_board(coordinate_x,coordinate_y,board):
    return 0 <= coordinate_x <= len(board) and 0 <= coordinate_y <= len(board)

def cell_contains_value(board,coordinate_x,coordinate_y, value):
    try:
        print_board(board)
        return board[coordinate_x][coordinate_y] == value
    except IndexError:
        return False

        
def translate_coordinates(coordinates):
    coordinate_x = 0
    coordinate_y = 0
    if coordinates == '':
        return 'Bad','Bad'
    letter = coordinates[0].lower()
    possible = list(map(chr, range(97, 128)))
    for i in possible:
        if i == letter:
            break
        coordinate_x += 1

    try:
        coordinate_y = int(coordinates[1:])
    except ValueError:
        return 'Bad','Bad'

    return (coordinate_x,coordinate_y-1)


def check_available_coordinates(board):
    available_coordinates = []
    for row_index, row in enumerate(board):
        for item_index, item in enumerate(row):
            if item == '0':
                available_coordinates.append((row_index, item_index))
    return available_coordinates

def ask_for_coordinates(board, cell_contains):
    while True:
        coordinates = input('enter coordinates\n')
        coordinate_x, coordinate_y= translate_coordinates(coordinates)
        if coordinate_x == 'Bad' or coordinate_y == 'Bad':
            print('bad coordinates')
        elif check_coordinate_is_in_board(coordinate_x,coordinate_y,board) and cell_contains(board,coordinate_x,coordinate_y, cell_contains):
            return (coordinate_x,coordinate_y)
        else:
            print('Bad coordinates')
