from os import system, name

# swiching player function
def change_player(player):
    if player == 'Player_2':
        player = 'Player_1'
    else:
        player == 'Player_1'
        player = 'Player_2'

    return player 


# create list of alphabetic coordinates depends on size of the board
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


    res_user_shoot = (row_number(size_of_the_board).index(user_shoot[0]),int(user_shoot[1])-1)
    current_player = change_player(current_player)
   
    return res_user_shoot, current_player

def user_shoot(coordinates, test_board, czynnosc ):
    cor_vertical = coordinates[0]
    cor_horizontal = coordinates[1]
    test_board[cor_horizontal][cor_vertical] = czynnosc
    return test_board

    
    

  
def main():      
    # clear_screen()
    
    current_player = "Player_2"
    test_board_1 =  ['0', '0', '0', '0'],\
                    ['0', '0', '0', '0'],\
                    ['0', '0', '0', '0'],\
                    ['0', '0', '0', '0']


    test_board_2 = [['0', '0', '0', '0'],
                    ['0', '0', '0', '0'],
                    ['0', '0', '0', '0'],
                    ['0', '0', '0', '0']]

    board_size = len(test_board_1)
    # print(test_board_1)
    
    # for i in range(board_size):
            
    #             print(test_board_1[i])
    
    for i in range(300): 
       
        coortinates, current_player = user_input(board_size,current_player)

        # clear_screen()
        print(current_player, coortinates)
        
        if current_player == 'Player_1':
            board = test_board_1
            for i in range(board_size):
            
                print(board[i])
                # clear_screen()
        else:
            board = test_board_2
            for i in range(board_size):
            
                print(board[i])
                # clear_screen()
        
        
    

         
        print(strz(board,coortinates))

        czynnosc = strz(board,coortinates)
        user_shoot(coortinates, board, czynnosc)
        # for i in range(board_size):a4
    
            
        #         print(board[i])
        #     # if len(list_available_coordinates(board)) == 0:
            #     print('nie ma wiecej ruchow')
# def update(coortinates, board):
#     board[coortinates[0],coortinates[1]] = "M"


def strz(board, coortinates):
    # czynnosc = None
    # if coortinates in list_missed_shots(board):
    #     print('tu juz strzelales')
    #     czynnosc = 'M'
    if coortinates in list_placed_ships(board):
        czynnosc = 'S'
        return czynnosc
        
    elif coortinates  in list_available_coordinates(board):
        czynnosc = 'M'
    
        
        return czynnosc
              

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

        
                
    # print(current_player, coortinates)


if __name__ == "__main__":
    main()