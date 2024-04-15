from backend.cell import Cell
import backend.constants as constants


class Ship(Cell):
    # public
    def shot(self, x, y):
        for curr_cell in self.__cells:
            if curr_cell.equals(x, y):
                if curr_cell.is_dead():
                    return 0
                self.__sz -= 1
                curr_cell.set_dead()
                if self.__sz == 0:
                    self.__alive = False
                    for curr in self.__cover:
                        curr.set_dead()
                    return 2
                return 1
        return -1

    def add_cover(self, cell):
        self.__cover.append(cell)

    def is_alive(self):
        return self.__alive

    # private
    __sz = 0
    __alive = True
    __cells = []
    __cover = []
    directions = constants.DIRECTIONS

    def __init__(self):
        pass

    def __init__(self, cells_):
        self.__sz = len(cells_)
        self.__cells = cells_
        self.__cover = []
