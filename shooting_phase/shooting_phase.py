from os import system, name


'''
wartości powinny być pobierane z listy playerów a nie nadawane na stałe
dzięki temu będzie można korzystać z nazw użytkownika zadanych na początku
'''
# switching players
# swiching player function
def change_player(player):
    if player == 'Player_2':
        player = 'Player_1'
    else:
        # tego chyba już nie musi być player == 'Player_1'
        player = 'Player_2'

    return player 


# create list of alphabetic coordinates depends on size of the board
'''
nie będziesz miał board size, będziesz miał tylko i wyłącznie board więc board_size
musisz sobie zmierzyć przez len()

tylko nie wiem do czego ta funkcja?
'''
def row_number(board_size = 5):
    rows = []
    for i in range(65, 65+board_size, 1):
        rows.append(chr(i))
    return rows

def quit_from_application(quit_command):
     if quit_command.upper() == 'QUIT':
            exit()

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#function validate size of input string, scope of input string and return coordinates in form (x,y) and current player after move. scope 26x26
def user_input(size_of_the_board,current_player):
    
    while True:
        user_shoot = input("Make a shoot :").upper()

        quit_from_application(user_shoot)
       
        if len(user_shoot) == 2 and user_shoot[1].isalpha() != True \
            and user_shoot[0].isalpha() == True \
            and int(user_shoot[1]) in range(1, size_of_the_board + 1) \
            and user_shoot[0] in row_number(size_of_the_board):
            # print(row_number(size_of_the_board))
            break
        else:
            clear_screen()
            print('Invaild input!')
            continue


    res_user_shoot = (int(user_shoot[1])-1,row_number(size_of_the_board).index(user_shoot[0]))
    current_player = change_player(current_player)
   
    return res_user_shoot, current_player

def gamewin(board, board2):
    if len(list_placed_ships(board)) == len(list_shooted_ships(board2)):
        text = "Koniec gry"
    return text


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