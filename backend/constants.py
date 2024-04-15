BOARD_SIZE = 10
TICKS_TO_REGENERATE_FIELD = 100
DIRECTIONS = ((0, 0), (0, -1), (0, 1), (-1, 0),
              (-1, 1), (-1, -1), (1, 0), (1, -1), (1, 1))
DEAD_CELL = '#'
ALIVE_CELL = '.'
DEAD_SHIP_CELL = '\u274C'
ALIVE_SHIP_CELL = '\u2705'
SHOT_STATUS = {-1: 'Missed.',
               0: 'Missed (already d3d).', 1: 'Wounded.', 2: 'Dead.'}
