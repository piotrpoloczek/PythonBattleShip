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

def user_shoot(coordinates, test_board):
    cor_vertical = coordinates[0]
    cor_horizontal = coordinates[1]
    test_board[cor_horizontal][cor_vertical] = "S"
    return test_board

    
    

  
def main():      
    # clear_screen()
  
    current_player = "Player_1"
    placement_board_1 = [['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0']] 
    placement_board_2 = [['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0']]
    shooting_board_1 = [['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0']] 
    shooting_board_2 = [['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0'],['0', '0', '0', '0']]
    board_size = len(placement_board_1)
   
     
    coortinates, current_player = user_input(board_size,current_player)

    print(current_player)
    
    while True:
        user_shoot(coortinates, placement_board_1)
        for i in range(board_size):
            print(shooting_board_1[i])
       
        
                
    # print(current_player, coortinates)


if __name__ == "__main__":
    main()