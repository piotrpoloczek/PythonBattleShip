player_1 = {
    'name': 'Piotr',
    'shooting_board': [
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0']],
    'placement_board': [
        ['0', '0', 'X', '0', '0'],
        ['X', '0', 'X', '0', '0'],
        ['X', '0', 'X', '0', '0'],
        ['0', '0', 'X', '0', '0'],
        ['0', '0', '0', 'X', 'X']],
}

player_2 = {
    'name': 'Łukasz',
    'shooting_board': [
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0']],
    'placement_board': [
        ['0', '0', 'X', '0', '0'],
        ['X', '0', 'X', '0', '0'],
        ['X', '0', 'X', '0', '0'],
        ['0', '0', 'X', '0', '0'],
        ['0', '0', '0', 'X', 'X']],
}

def error_msg():
    pass

def coordinate_outside_board():
    pass

def coordinate_already_shooted():
    pass

def get_user_input():
    return input("Please enter the coordinates: ")

def validate_user_input():
    pass

def return_coordinates():
    pass

def check_shoot(shooting_board_player_1, placement_board_player_2, coordinates):
    pass

def shoot_success(shooting_board_player_1):
    #add shoted to the board
    pass

def shoot_fail(shooting_board_player_2):
    #add missed to the board
    pass

def shoot(shooting_board_player_1, placement_board_player_2, coordinates):
    if check_shoot(shooting_board_player_1, placement_board_player_2, coordinates) is True:
        return shoot_success(shooting_board_player_1)
    else:
        return shoot_fail(shooting_board_player_1)

def shooting_phase(shooting_board_player_1, placement_board_player_2):
    user_turn = True

    while user_turn:
        user_input = get_user_input()
        if validate_user_input(user_input, shooting_board_player_1, placement_board_player_2) is True:
            coordinates = return_coordinates(user_input)
            shoot(shooting_board_player_1, placement_board_player_2, coordinates)
            user_turn = False
        else:
            # some error message should be there
            error_msg(user_input, shooting_board_player_1, placement_board_player_2)

