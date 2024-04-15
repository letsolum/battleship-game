import backend.constants as constants


class Cell:
    # public
    def set_dead(self):
        self.__dead = True

    def set_cover(self):
        self.__cover = True

    def set_ship(self, num):
        self.__ship = num
        self.__part = True

    def equals(self, curr_x, curr_y):
        return curr_x == self.__x and curr_y == self.__y

    def out(self, secret):
        if secret:
            return (' ' + constants.ALIVE_CELL) * (not self.__part) + constants.ALIVE_SHIP_CELL * (self.__part)
        if not self.__dead:
            return ' ' + constants.ALIVE_CELL
        elif self.__cover or not self.__part:
            return ' ' + constants.DEAD_CELL
        else:
            return constants.DEAD_SHIP_CELL

    def is_dead(self):
        return self.__dead

    def ship_num(self):
        return self.__ship

    def is_cover(self):
        return self.__cover

    def is_part(self):
        return self.__part

    def get_cords(self):
        return [self.__x, self.__y]

    # private


    def __init__(self):
        pass

    def __init__(self, x_, y_):
        self.__x, self.__y = x_, y_
        self.__dead = False
        self.__cover = False
        self.__part = False
        self.__ship = -1

    def __del__(self):
        self.__dead = False


