
import pygame

from typing import Tuple

from src.constants import GAME_SCREEN_SIZE, GAME_SCREEN_COLOR, GAME_FRAME_RATE
from src.automata import Automata


class Game:
    """The game object
    """

    def __init__(self, num_iter: int, mov_iter: int, rule: Tuple[Tuple[Tuple[int, int, int], int]], init_state: list):
        """Initialize the game object

        Args:
            num_iter (int): The number of iterations to run
            mov_iter (int): The number of iterations to show in a window

            rule (Tuple[Tuple[Tuple[int, int, int], int]]): A list defining the rules
            init_state (list): A list defining the initial state
        """
        # Basic initialization
        pygame.init()
        self.game_running = True

        # Delta Time
        self.clock = pygame.time.Clock()
        self.dt = 0.001                     # HARDCODE ALERT!!

        # Automata object
        self.automata = Automata(num_iter, mov_iter, rule, init_state)

        # The screen
        self.screen = pygame.display.set_mode(self.automata.screen_dim)     # A rectangular screen

        self.automata.white_cell = pygame.transform.scale(pygame.image.load("./assets/cells/white_cell.png").convert(), self.automata.cell_size)
        self.automata.black_cell = pygame.transform.scale(pygame.image.load("./assets/cells/black_cell.png").convert(), self.automata.cell_size)
        self.automata.grey_cell = pygame.transform.scale(pygame.image.load("./assets/cells/grey_cell.png").convert(), self.automata.cell_size)


    def run(self):
        """Runs the game
        """
        while self.game_running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False

            self.screen.fill(GAME_SCREEN_COLOR)

            # AUTOMATA
            self.automata.draw(self.screen)
            self.automata.update(self.dt)

            pygame.display.flip()

            self.dt = self.clock.tick(GAME_FRAME_RATE)

        self.quit(reason="Manual quit")


    def quit(self, reason):
        pygame.quit()
