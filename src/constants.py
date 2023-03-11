
import numpy

GAME_SCREEN_SIZE = (1024, 1024)
GAME_SCREEN_COLOR = (00, 78, 78)

GAME_FRAME_RATE = 100

GAME_DEFAULT_NUM_ITER = 500
GAME_DEFAULT_MOV_ITER = 500

# RULE ??
GAME_DEFAULT_RULE = (
                        ((1, 1, 1), 0),
                        ((1, 1, 0), 1),
                        ((1, 0, 1), 1),
                        ((1, 0, 0), 0),
                        ((0, 1, 1), 1),
                        ((0, 1, 0), 1),
                        ((0, 0, 1), 1),
                        ((0, 0, 0), 0),
                        )

GAME_DEFAULT_INIT_STATE = numpy.zeros(GAME_DEFAULT_NUM_ITER)
GAME_DEFAULT_INIT_STATE[250] = 1

# TOTALISTIC CELLULAR AUTOMATON
# GAME_DEFAULT_RULE = (
#                         ((6/3, 6/3, 6/3), 1),
#                         ((5/3, 5/3, 5/3), 0),
#                         ((4/3, 4/3, 4/3), 0),
#                         ((3/3, 3/3, 3/3), 1),
#                         ((2/3, 2/3, 2/3), 2),
#                         ((1/3, 1/3, 1/3), 1),
#                         ((0/3, 0/3, 0/3), 0),
#                         )


# RULE 90
# GAME_DEFAULT_RULE = (
#                         ((1, 1, 1), 0),
#                         ((1, 1, 0), 0),
#                         ((1, 0, 1), 0),
#                         ((1, 0, 0), 1),
#                         ((0, 1, 1), 0),
#                         ((0, 1, 0), 1),
#                         ((0, 0, 1), 1),
#                         ((0, 0, 0), 0),
#                         )

# RULE 2049
# GAME_DEFAULT_RULE = (
#                         ((6/3, 6/3, 6/3), 2),
#                         ((5/3, 5/3, 5/3), 2),
#                         ((4/3, 4/3, 4/3), 1),
#                         ((3/3, 3/3, 3/3), 0),
#                         ((2/3, 2/3, 2/3), 2),
#                         ((1/3, 1/3, 1/3), 2),
#                         ((0/3, 0/3, 0/3), 0),
#                         )
