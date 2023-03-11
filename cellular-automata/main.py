
from src.game import Game

from src.constants import GAME_DEFAULT_NUM_ITER, GAME_DEFAULT_MOV_ITER, GAME_DEFAULT_RULE, GAME_DEFAULT_INIT_STATE

def main():
    game = Game(GAME_DEFAULT_NUM_ITER, GAME_DEFAULT_MOV_ITER, GAME_DEFAULT_RULE, GAME_DEFAULT_INIT_STATE)
    game.run()

if __name__ == '__main__':
    main()
