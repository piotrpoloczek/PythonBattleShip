from os import system, name
from player.player_attributes import get_player_name, get_player_placement_board, get_player_shooting_board
from coordinates.coordinates_function import ask_for_coordinates
from prepare_game.const import EMPTY_CELL


def shooting_phase(player_1, player_2):
    actual_player = player_1
    while True:
        player_turn(actual_player)
        if check_winner(player_1, player_2):
            return get_winner(player_1, player_2)
        actual_player = change_actual_player(actual_player, player_1, player_2)

def player_turn(player):
    player_placement_board = get_player_placement_board(player)
    ask_for_coordinates(player_placement_board, EMPTY_CELL)
    pass

def check_winner(player_1, player_2):
    # check if there is winner
    pass

def get_winner(player_1, player_2):
    # return the winner player_1 or player_2
    pass

def change_actual_player(actual_player, player_1, player_2):
    if actual_player == player_1:
        return player_2
    else:
        return player_1


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



def return_coordinates_with_item(board, searched_item):
    return [(row_index, item_index) for row_index, row in enumerate(board) for item_index, item in enumerate(row) if item == searched_item]

def list_available_coordinates(board):
    return return_coordinates_with_item(board, '0')
    
def list_shooted_ships(board):
    return return_coordinates_with_item(board, 'S')

def list_missed_shots(board):
    return return_coordinates_with_item(board, 'M')

def list_placed_ships(board):
    return return_coordinates_with_item(board, 'X')

def list_hited_ships(board):
    return return_coordinates_with_item(board, 'H')
        
def print_headerer(board_size):
    for i in range(board_size):
            headerer_letter = row_number(board_size)
            print(' ', end=" ")
            if i != board_size - 1 :
                print(headerer_letter[i],end="  ")
            else:
                print(f'{headerer_letter[i]}')
    return None

if __name__ == "__main__":
    main()