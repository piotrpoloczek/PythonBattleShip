def get_player_placement_board(player):
    return player['placement_board']

def get_player_shooting_board(player):
    return player['shooting_board']

def get_player_name(player):
    return player['name']

def set_player_placement_board(player, placement_board):
    player['placement_board'] = placement_board

def set_player_shooting_board(player, shooting_board):
    player['shooting_board'] = shooting_board

def set_player_name(player, name):
    player['name'] = name