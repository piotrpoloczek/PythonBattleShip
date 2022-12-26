current_player = 'Player_2'

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


#function validate size of input string, scope of input string and return coordinates in form (x,y) and current player after move.
def user_input(size_of_the_board,current_player):
    while True:
        
        user_shoot = input("Make a shoot :").upper() 
        if len(user_shoot) > 2:
            continue
        try:
            if user_shoot[0] in row_number(size_of_the_board):
                if int(user_shoot[1]) in range(0, size_of_the_board + 1):
                    row = row_number(size_of_the_board)
                    res_user_shoot = (row.index(user_shoot[0]),int(user_shoot[1]))
                    current_player = change_player(current_player)
                    return res_user_shoot, current_player
            else:
                print('Invalid input!, try again!')
                continue
        except IndexError:

            print('')

       
coortinates, current_player = user_input(6, current_player)
print(current_player, coortinates)
