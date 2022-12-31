from prepare_game.const import MAX_BOARD_SIZE, MIN_BOARD_SIZE


def board_size_error():
    print(f'You provided incorrect input, please choose the size from \
{MIN_BOARD_SIZE} to {MAX_BOARD_SIZE} at most.')


def invallid_username_error():
    print('Please choose the corect name for the user.')