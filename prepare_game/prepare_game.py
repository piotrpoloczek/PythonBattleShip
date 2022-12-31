from prepare_board import prepare_empty_board
from prepare_user import prepare_user_name


def prepare_player():
    player_1 = {}
    player_1['user'] = prepare_user_name()
    player_1['placement_board'] = prepare_empty_board()
    player_1['shooting_board'] = prepare_empty_board()
    return player_1

def prepare_game():
    player_1 = prepare_player()
    player_2 = prepare_player()
    # tutaj zwracam listę z dwoma słownikami dla graczy
    # tylko tą funkcję wykorzystujemy w głównej pętli 
    return [player_1, player_2]