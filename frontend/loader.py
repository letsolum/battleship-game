import os
from backend.field import Field
from frontend.view_out import Viewer
import frontend.constants as constants

class Loader:
    __player_field = Field()

    def load_autodata(self):
        lis = os.listdir('.')
        if lis.count(constants.AUTO_INP) == 1:
            fl = input(
                'Detected auto-input file of your ships. Do you want to use it?[yes/no]: ')
            if fl == 'yes':
                positions = []
                f = open(constants.AUTO_INP, 'r')
                raw = f.read().splitlines()
                for e in raw:
                    start, end = e.split(' ')
                    y_st, x_st = ord(start[0]) - ord('A') + 1, int(start[1:])
                    y_en, x_en = ord(end[0]) - ord('A') + 1, int(end[1:])
                    start, end = [x_st, y_st], [x_en, y_en]
                    positions.append([start, end])
                f.close()
                return positions
        return False

    def input_field(self, output: Viewer):
        positions = []
        for _ in range(10):
            start, end = map(str, input(
                'Input position of new ship (for ex. "A1 A4"): ').split(' '))
            y_st, x_st = ord(start[0]) - ord('A') + 1, int(start[1:])
            y_en, x_en = ord(end[0]) - ord('A') + 1, int(end[1:])
            start, end = [x_st, y_st], [x_en, y_en]
            while not self.__player_field.place_boat(start, end):
                start, end = map(str, input(
                    'Incorrect. Input position of new ship (for ex. "A1 A4"): ').split(' '))
                y_st, x_st = ord(start[0]) - ord('A') + 1, int(start[1:])
                y_en, x_en = ord(end[0]) - ord('A') + 1, int(end[1:])
                start, end = [x_st, y_st], [x_en, y_en]
            positions.append([start, end])
            output.field_out(self.__player_field, True)
        return positions

    def get_input(self):
        curr_sz = self.__player_field.size()
        pos = input('Your turn: ')
        x = ord(pos[0]) - ord('A') + 1
        y = int(pos[1:])
        while x < 1 or x > curr_sz or y < 1 or y > curr_sz:
            pos = input('Incorrect input. Your turn: ')
            x = ord(pos[0]) - ord('A') + 1
            y = int(pos[1:])
        pos = [y, x]
        return pos
