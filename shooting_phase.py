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

#function validate size of input string, scope of input string and return coordinates in form (x,y) and current player after move.
def user_input(size_of_the_board,current_player):
    
    while True:
        user_shoot = input("Make a shoot :").upper()

        quit_from_application(user_shoot)
   
#validation of input
       
        if len(user_shoot) == 2 and user_shoot[1].isalpha() != True \
            and user_shoot[0].isalpha() == True \
            and int(user_shoot[1]) in range(1, size_of_the_board + 1) \
            and int(user_shoot[0] in row_number(size_of_the_board)):
            break
        else:
            clear_screen()
            continue


    res_user_shoot = (row_number(size_of_the_board).index(user_shoot[0]),int(user_shoot[1])-1)
    current_player = change_player(current_player)
   
    return res_user_shoot, current_player


  
def main():      
   
    coortinates, current_player = user_input(6, current_player = 'Player_a')
    print(current_player, coortinates)
   


if __name__ == "__main__":
    main()