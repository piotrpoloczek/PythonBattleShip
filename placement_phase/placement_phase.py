from player.player_attributes import get_player_name, get_player_placement_board, get_player_shooting_board
from printing_board.printing import print_board

import copy


def check_coordinate_is_in_board(coordinate_x,coordinate_y,board):
    return 0 <= coordinate_x <= len(board) and 0 <= coordinate_y <= len(board)

def check_coordinate_is_free(board,coordinate_x,coordinate_y):
    try:
        print_board(board)
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
        return 'Bad','Bad'

    return (coordinate_x,coordinate_y-1)


def check_available_coordinates(board):
    available_coordinates = []
    for row_index, row in enumerate(board):
        for item_index, item in enumerate(row):
            if item == '0':
                available_coordinates.append((row_index, item_index))
    return available_coordinates

def ask_for_coordinates(board):
    while True:
        coordinates = input('enter coordinates\n')
        coordinate_x, coordinate_y= translate_coordinates(coordinates)
        if coordinate_x == 'Bad' or coordinate_y == 'Bad':
            print('bad coordinates')
        elif check_coordinate_is_in_board(coordinate_x,coordinate_y,board) and check_coordinate_is_free(board,coordinate_x,coordinate_y):
            return (coordinate_x,coordinate_y)
        else:
            print('Bad coordinates')

'''
tą funkcję można myślę będzie wrzucić do osobnego modułu ale na razie niech tutaj zostanie
'''
def number_of_ships():
    number_of_ships = [1,1,1,2,2]
    return number_of_ships

def ask_for_orientation():
    while True:
        orientation = input('You want to place the ship in left or down?\n')
        orientation = orientation.lower()
        if orientation == 'left' or orientation == 'down':
            return orientation
        else:
            print('Bad orientation')


def check_for_near_ships_horizontal(board,coordinate_x,coordinate_y):
    try:
        if board[coordinate_x][coordinate_y-1] != 'X' or board[coordinate_x+1][coordinate_y] != 'X' or board[coordinate_x][coordinate_y-1] != 'X':
            return True
        else:
            print('Ship is to close to another ship')
            return False
    except IndexError:
        if board[coordinate_x][coordinate_y-1] != 'X' or board[coordinate_x+1][coordinate_y] != 'X' or board[coordinate_x][coordinate_y-1] != 'X':
            return True
        else:
            print('Ship is to close to another ship')
            return False


def check_for_near_ships_vertical(board,coordinate_x,coordinate_y):
    try:
        if board[coordinate_x-1][coordinate_y] == 'X' or board[coordinate_x][coordinate_y+1] == 'X' or board[coordinate_x+1][coordinate_y] == 'X':
            print('Ship is to close to another ship')
            return False
        else:
            return True
    except IndexError:
        if board[coordinate_x-1][coordinate_y] == 'X' or board[coordinate_x][coordinate_y+1] == 'X' or board[coordinate_x+1][coordinate_y] == 'X':
            print('Ship is to close to another ship')
            return False
        else:
            return True

def place_ship(board,coordinate_x,coordinate_y,orientation,ship_size):
    board_copy = copy.deepcopy(board)
    if orientation == 'left':
        try:
            if check_coordinate_is_in_board(coordinate_x,coordinate_y-1) and board_copy[coordinate_x][coordinate_y-1] == 'X':
                print('Ship is to close to another ship')
                return board,False
            for i in range(0,ship_size):
                if check_for_near_ships_vertical(board_copy,coordinate_x,coordinate_y) == True:
                    board_copy[coordinate_x][coordinate_y] = 'X'
                    coordinate_y += 1
                else:
                    return board,False
            return board_copy,True
        except IndexError:
            if check_coordinate_is_in_board(coordinate_x,coordinate_y) and check_coordinate_is_free(board_copy,coordinate_x,coordinate_y) and (ship_size == 1 or i == ship_size-1):
                board_copy[coordinate_x][coordinate_y] = 'X'
                return board_copy, True
            else:
                return board,False
    elif orientation == 'down':
        try:
            if check_coordinate_is_in_board(coordinate_x-1,coordinate_y) and board_copy[coordinate_x-1][coordinate_y] == 'X':
                print('Ship is to close to another ship')
                return board,False
            for i in range(0,ship_size):
                if check_for_near_ships_horizontal(board_copy,coordinate_x,coordinate_y) == True:
                    board_copy[coordinate_x][coordinate_y] = 'X'
                    coordinate_x += 1
                else:
                    return board,False
            return board_copy,True
        except IndexError:
            if check_coordinate_is_in_board(coordinate_x,coordinate_y) and check_coordinate_is_free(board_copy,coordinate_x,coordinate_y) and (ship_size == 1 or i == ship_size-1):
                board_copy[coordinate_x][coordinate_y] = 'X'
                return board_copy, True
            else:
                return board,False
    # except IndexError:
    #     print('The ship is otside the board!')
    #     return board


'''
To mogłoby być 'player_ships_placement' dlatego że funkcja obsługuje tylko jednego playera
'''
def player_ships_placement(board):
    print_board(board)
    ships_to_place = number_of_ships()
    for i in ships_to_place:
        while True:
            print(f'place ship of size {i}')
            coordinate_x,coordinate_y = ask_for_coordinates(board)
            if i != 1:
                orientation = ask_for_orientation()
            else:
                orientation = 'down'
            board, is_ship_placed = place_ship(board,coordinate_x,coordinate_y,orientation,i)
            print_board(board)
            if is_ship_placed:
                break
            else:
                print('The ship is wrong placed')

'''
i tu można by było zrobic funkcję ships_placement
tutaj można by użyć funkcji które zrobiłem w repop 'piotrpoloczek' w module player, 
tam są gettery i settery do wykorzystania, ale to na zadanie domowe importowanie modułów ;)

Dzięki tej funkcji tylko ta funkcję importujemy w module battleships i mamy sprawę załatwioną.
Łukasz ma trudniejsze zadanie bo rzeczywiście musi zmieniać użytkownika.
'''
def ships_placement(players):
    player_1 = players[0]
    player_2 = players[1]
    player_ships_placement(get_player_placement_board(player_1))
    player_ships_placement(get_player_placement_board(player_2))
    
    # znowu eksportujemy listę z playerami tylko tym razem mają już umieszczone wszystkie statki
    return [player_1, player_2]




#board=[['0', '0', '0', '0','0'],['0', '0', '0', '0','0'],['0', '0', '0', '0','0'],['0', '0', '0', '0','0'],['0', '0', '0', '0','0']]
#ships_placement(board)







# if __name__ == '__main__':
#     battleship_board = board.return_empty_board(5, 5)
#     test_board_1 = [['0', '0', '0', '0'],['0', '0', '0', '0'],['X', '0', 'X', '0'],['0', 'X', 'X', 'X']]
#     test_board_2 = [['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0']]
#     print(check_available_coordinates(battleship_board))
#     print(check_available_coordinates(test_board_1))
#     print(check_available_coordinates(test_board_2))