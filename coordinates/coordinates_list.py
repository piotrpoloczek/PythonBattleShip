from prepare_game.const import EMPTY_CELL, SHIP_IN_CELL, MISSED_CELL, SHIP_HITED, SHIP_SINK


def return_coordinates_with_item(board, searched_item):
    return [(row_index, item_index) for row_index, row in enumerate(board) for item_index, item in enumerate(row) if item == searched_item]

def list_available_coordinates(board):
    return return_coordinates_with_item(board, EMPTY_CELL)
    
def list_shooted_ships(board):
    return return_coordinates_with_item(board, SHIP_SINK)

def list_missed_shots(board):
    return return_coordinates_with_item(board, MISSED_CELL)

def list_placed_ships(board):
    return return_coordinates_with_item(board, SHIP_IN_CELL)

def list_hited_ships(board):
    return return_coordinates_with_item(board, SHIP_HITED)