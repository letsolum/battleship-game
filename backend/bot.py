import copy
import random
import backend.constants as constants
from backend.field import Field


class Bot:
    def __init__(self):
        self.__ticks_to_regenerate = constants.TICKS_TO_REGENERATE_FIELD
        self.__field = copy.deepcopy(Field())

    def generate_field(self):
        curr_sz = self.__field.size()
        self.__game_started = True
        i = 0
        while i < self.__field.size():
            start = [random.randint(1, curr_sz),
                     random.randint(1, curr_sz)]
            end = [start[0], random.randint(1, curr_sz)]
            count_ticks = 0
            while not self.__field.place_boat(start, end):
                if count_ticks > self.__ticks_to_regenerate:
                    self.__field = Field()
                    i = 0
                start = [random.randint(1, curr_sz),
                         random.randint(1, curr_sz)]
                end = [start[0], random.randint(1, 10)]
                count_ticks += 1
            i += 1

    def next_turn(self):
        curr_sz = self.__field.size()
        pos = [random.randint(1, curr_sz), random.randint(1, curr_sz)]
        return pos

    def enemy_shot(self, pos):
        return self.__field.shot(pos)

    def lose(self):
        return self.__field.lose()

    def get_field(self):
        return self.__field

    def __del__(self):
        del self.__field
