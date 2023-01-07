from prepare_game.prepare_board import prepare_empty_board
from prepare_game.prepare_user import prepare_user_name
from prepare_game.prepare_difficulity import return_dimension
from player.player_attributes import set_player_name, set_player_placement_board, set_player_shooting_board


def prepare_player(board_size):
    player_1 = {}
    set_player_name(player_1, prepare_user_name())
    set_player_placement_board(player_1, (board_size))
    set_player_shooting_board(player_1, prepare_empty_board(board_size))
    return player_1

def prepare_game():
    difficulity_level = return_dimension()
    player_1 = prepare_player(difficulity_level)
    player_2 = prepare_player(difficulity_level) 
    return [player_1, player_2]