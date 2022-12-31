from prepare_game.prepare_board import prepare_empty_board
from prepare_game.prepare_user import prepare_user_name
from prepare_game.prepare_difficulity import return_dimension


def prepare_player(board_size):
    player_1 = {}
    player_1['user'] = prepare_user_name()
    player_1['placement_board'] = prepare_empty_board(board_size)
    player_1['shooting_board'] = prepare_empty_board(board_size)
    return player_1

def prepare_game():
    difficulity_level = return_dimension()
    player_1 = prepare_player(difficulity_level)
    player_2 = prepare_player(difficulity_level) 
    return [player_1, player_2]