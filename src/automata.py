
"""Works on the updation of the game state
"""

import pygame
import numpy

from src.constants import GAME_SCREEN_SIZE

from typing import Tuple


class Automata:
    """The automata object
    """

    def __init__(self, num_iter: int, mov_iter: int, rule: Tuple[Tuple[Tuple[int, int, int], int]], init_state: Tuple[int]):
        """The automata object, with a specific rule and state dimensions

        Args:
            num_iter (int): The number of iterations to run
            mov_iter (int): The number of iterations to show on the screen
            rule (Tuple[Tuple[Tuple[int, int, int], int]]): The rule "dict"
            init_state (Tuple[int]): The initial state tuple for the automata
        """

        # The basic dimensions of the automata
        self.num_iter = num_iter
        self.mov_iter = mov_iter

        # The rule
        self.rule = rule

        # State variables
        self.curr_state = numpy.array(init_state)
        self.state_len = len(init_state)
        self.state_dim = (num_iter + 1, len(init_state))    # Since the initial state is also stored in history
        self.state_history = numpy.zeros(self.state_dim)
        self.state_history[0, :] = init_state
        self.curr_iter = 0 + 1                              # The first iteration row

        # Assumption that the frame numbers are even
        self.frame_len = len(rule[0][0])                    # The number of elements in the frame

        # More on the dimensions of the automata for rendering on the screen
        x, y = GAME_SCREEN_SIZE
        min_dim = min(x // self.state_len, y // self.mov_iter)
        self.cell_size = (min_dim, min_dim) # A square cell
        self.screen_dim = (min_dim * self.state_len, min_dim * self.mov_iter)

        # Cells surfaces
        self.white_cell = None
        self.black_cell = None
        self.grey_cell = None



    def draw(self, screen: pygame.Surface):
        """Draws the moving frame on the screen

        Args:
            screen (pygame.Surface): _description_
        """
        for i in range(self.mov_iter):
            for j in range(self.state_len):
                if self.curr_iter < self.mov_iter:
                    cell_val = self.state_history[i][j]
                else:
                    cell_val = self.state_history[self.curr_iter - self.mov_iter + i][j]

                # HARDCODE ALERT!!!
                if cell_val == 0:
                    screen.blit(self.white_cell, (j * self.cell_size[0], i * self.cell_size[1]))
                # elif cell_val == 1:
                #     screen.blit(self.grey_cell, (j * self.cell_size[0], i * self.cell_size[1]))
                elif cell_val == 1: #2:
                    screen.blit(self.black_cell, (j * self.cell_size[0], i * self.cell_size[1]))
                else:
                    print(f"UNEXPECTED CELL VALUE {cell_val}")
                    exit(1)

        return None


    def update(self, dt: float):
        """Updates the state of the curr array and puts it into the states history matrix

        Args:
            dt (float): The delta time from the last frame update
        """
        # The number of updates per second is determined by the game FPS
        # A simple but effective measure

        temp_state = numpy.zeros(self.state_len)
        for center in range(self.state_len):
            curr_frame = numpy.zeros(self.frame_len)

            # Assumption that the frame numbers are even
            half_frame = self.frame_len // 2
            for frame_shift in range(-1 * half_frame, half_frame + 1):
                virt_index = center + frame_shift

                if virt_index < 0 or virt_index >= self.state_len:
                    pass
                else:
                    curr_frame[frame_shift + half_frame] = self.curr_state[virt_index]

            # HARDCODE:
            # e.g. average value of current frame
            # curr_frame[:] = numpy.mean(curr_frame)

            # Finding and applying the rule
            for rule in self.rule:
                if rule[0] == tuple(curr_frame):
                    temp_state[center] = rule[1]

        self.curr_state = temp_state
        self.state_history[self.curr_iter, :] = self.curr_state
        self.curr_iter += 1

        return None
