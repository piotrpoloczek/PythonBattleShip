from prepare_game.prepare_game import prepare_game
from printing_board.printing import print_board
from placement_phase.placement_phase import ships_placement
#from shooting_phase import shooting


def main_loop():
    players = prepare_game()
    print(players)
    players = ships_placement(players)
    #shooting(players)

    #example how to use the print_board function in other modules
    print_board(players[0]['placement_board'])

    
if __name__ == '__main__':
    main_loop()