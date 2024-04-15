from backend.field import Field
import copy

class Player:


    def construct_field(self, positions: list):
        for pos in positions:
            self.__field.place_boat(pos[0], pos[1])

    def enemy_shot(self, pos):
        return self.__field.shot(pos)

    def lose(self):
        if self.__field.lose():
            pass
        return self.__field.lose()

    def get_field(self):
        return self.__field

    def __init__(self):
        self.__field = copy.deepcopy(Field())

    def __del__(self):
        del self.__field