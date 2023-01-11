from prepare_game.errors_messages import board_size_error
from prepare_game.const import MIN_BOARD_SIZE, MAX_BOARD_SIZE


def ask_user_dimesion():
    '''
    ask for user dimesnion of table
    '''
    return input("Choose the size of the board: ")

def validate_user_dimension(user_input):
    try:
        board_size = int(user_input)
        if board_size in range(MIN_BOARD_SIZE, MAX_BOARD_SIZE):
            return True
        return False
    except:
        return False

def return_user_dimension(user_input):
    return int(user_input)

def return_dimension():
    user_choice = True
    while user_choice:
        user_dimension = ask_user_dimesion()
        if validate_user_dimension(user_dimension):
            board_size = return_user_dimension(user_dimension)
            break
        else:
            board_size_error()
    
    return board_size

def number_of_ships():
    number_of_ships = [1,1,1,2,2]
    return number_of_ships