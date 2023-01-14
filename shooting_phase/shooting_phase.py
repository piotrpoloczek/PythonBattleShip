from os import system, name
from player.player_attributes import get_player_name, get_player_placement_board, get_player_shooting_board
from player.player_functions import change_player, get_winner, check_winner
from coordinates.coordinates_function import ask_for_coordinates, coordinates_ship_sinked
from prepare_game.const import EMPTY_CELL, MISSED_CELL, SHIP_HITED
from coordinates.coordinates_list import (
    list_available_coordinates, list_shooted_ships,
    list_missed_shots, list_hited_ships, list_placed_ships)


def shooting_phase(player_1, player_2):
    actual_player = player_1
    opponent = player_2
    while True:
        player_turn(actual_player, opponent)
        if check_winner(player_1, player_2):
            return get_winner(player_1, player_2)
        actual_player = change_player(actual_player, player_1, player_2)
        opponent = change_player(opponent, player_1, player_2)

def player_turn(actual_player, opponent):
    player_shooting_board = get_player_shooting_board(actual_player)
    opponent_placement_board = get_player_placement_board(opponent)

    coordinates = ask_for_coordinates(player_shooting_board, EMPTY_CELL)
    
    while True:
        if coordinates in list_missed_shots(opponent_placement_board):
            print('you already chose that cell, and you miss')
        elif coordinates in list_hited_ships(opponent_placement_board):
            print('you already choose that cell, and you hitted the ship')
        elif coordinates in list_shooted_ships(opponent_placement_board):
            print('you already choose that cell, and you sank the ship')
        elif coordinates in list_available_coordinates(opponent_placement_board):
            print('you missed the ships')
            make_shoot(opponent_placement_board, coordinates, MISSED_CELL)
            break
        elif coordinates in list_placed_ships(opponent_placement_board):
            print('you hit the ship')
            make_shoot(opponent_placement_board, coordinates, SHIP_HITED)

            coordinates_ship_sinked(opponent_placement_board, coordinates)
            break

    

def make_shoot(board, coordinates, cell_sign):
    coordinate_x = coordinates[0]
    coordinate_y = coordinates[1]
    board[coordinate_x, coordinate_y] = cell_sign



def game_shooting(players):
        print(players)
        game = True  
        
        current_player = "Player_1"
        board_size = len(placement_board_1)

        while game == True:   
        
            print_headerer(board_size)
            if current_player == 'Player_1':
                board = placement_board_2
                board2 = shooting_board_1
                for i in range(board_size):
                    
                    print(board[i], '|', board2[i])
                print('-------------------------------------------')
            else:
                board = placement_board_1
                board2 = shooting_board_2
                
                for i in range(board_size):
                
                    print(board[i], '|', board2[i])
                print('-------------------------------------------')
            coordinates, current_player = user_input(board_size,current_player)
            

            print(strz(board,board2, coordinates))
            # check_sink(board2,coordinates)

def main():      
    # clear_screen()
    placement_board_1 = [['0', 'X', '0'],['0', 'X', '0'],['0', '0', '0']]
    placement_board_2 = [['X', '0', 'X'],['X', '0', '0'],['0', 'X', '0']]

    game_shooting(placement_board_1,placement_board_2)
       

def create_board(board_size):
    
        board = []
        for i in range(board_size):
            sub_board = []
            for j in range(board_size):
                sub_board.append(('0')) 
            board.append(sub_board)
        return board
            
def intersection(lst1, lst2):
    # temp = set(lst2)
    # lst3 = [value for value in lst1 if value in temp]
    # return lst3
    
    return list(set(lst1) & set(lst2))
 
def check_sink(board2,coordinatess):
    
    list_of = intersection(check_nearest(coordinatess),list_hited_ships(board2))
    # print(list_of)
    c = coordinatess[0]
    d = coordinatess[1] 
    
    for item in(list_of):
        a = item[0]
        b = item[1]
        board2[a][b] = 'S'
        board2[c][d] = 'S'
        text = "You've sink a ship!"
        return text
        

def strz(board,board2, coordinatess):
    if coordinatess in list_placed_ships(board):
        board2[coordinatess[0]][coordinatess[1]] = 'H'
        text = "You've hit a ship!"
    else:
        board2[coordinatess[0]][coordinatess[1]] = 'M'
        text = "You've missed!" 
    return text
       
def check_nearest(coordin):
    
    test_coor = []
    
    test_coor.append((coordin[0]+1,coordin[1]))
    test_coor.append((coordin[0],coordin[1]+1))
    test_coor.append((coordin[0]-1,coordin[1]))
    test_coor.append((coordin[0],coordin[1]-1))
    

    return test_coor

