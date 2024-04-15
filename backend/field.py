from backend.cell import Cell
from backend.ship import Ship
import backend.constants as constants


class Field(Cell):
    directions = constants.DIRECTIONS

    def all_dead(self):
        dead_cells = []
        for i in range(1, constants.BOARD_SIZE + 1):
            for j in range(1, constants.BOARD_SIZE + 1):
                if self.__field[i][j].is_dead():
                    dead_cells.append([i, j])
        return dead_cells

    def size(self):
        return self.__sz

    def place_boat(self, start, end):
        if not self.__check_correctness(start, end):
            return False
        self.__bts_spec[abs(start[0] - end[0]) +
                        abs(start[1] - end[1]) + 1] -= 1
        self.__cnt_boats += 1
        cells_ = []
        for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            for j in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                self.__field[i][j].set_ship(self.__cnt_boats)
                cells_.append(self.__field[i][j])
        self.__boats.append(Ship(cells_))
        for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            for j in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                for [x, y] in self.directions:
                    i, j = i + x, j + y
                    if not self.__field[i][j].is_part():
                        self.__field[i][j].set_cover()
                        self.__boats[self.__field[i - x][j -
                                                         y].ship_num() - 1].add_cover(self.__field[i][j])
                    i, j = i - x, j - y
        return True

    def shot(self, pos):
        x, y = int(pos[0]), int(pos[1])
        ans = -1
        if self.__field[x][y].ship_num() >= 0:
            ans = self.__boats[self.__field[x][y].ship_num() - 1].shot(x, y)
        self.__field[x][y].set_dead()
        self.__cnt_boats -= (ans == 2)
        if self.__cnt_boats == 0:
            self.__all_dead = True
        return ans

    def get_cell(self, i, j):
        return self.__field[i][j]

    def lose(self):
        return self.__all_dead

    __sz = constants.BOARD_SIZE
    __all_dead = False
    __cnt_boats = 0

    def __init__(self):
        self.__field = []
        self.__boats = []
        self.__bts_spec = dict()
        for i in range(self.__sz + 2):
            self.__field.append([Cell(i, j) for j in range(self.__sz + 2)])
        for curr in range(1, 5):
            self.__bts_spec[curr] = 5 - curr

    def __check_correctness(self, start, end):
        if min(start[0], start[1]) < 1 or max(start[0], start[1]) > self.__sz:
            return False
        if min(end[0], end[1]) < 1 or max(end[0], end[1]) > self.__sz:
            return False
        if (start[0] != end[0] and start[1] != end[1]) or (abs(start[0] - end[0]) + abs(start[1] - end[1]) > 3):
            return False
        if self.__bts_spec[abs(start[0] - end[0]) + abs(start[1] - end[1]) + 1] == 0:
            print('spec')
            return False
        flag = True
        for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            for j in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                for [x, y] in self.directions:
                    i, j = i + x, j + y
                    if self.__field[i][j].is_part():
                        flag = False
                    i, j = i - x, j - y
        return flag

    def __del__(self):
        for x in self.__field:
            for y in x:
                del y
        del self.__field, self.__boats, self.__bts_spec

