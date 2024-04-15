import backend.constants as constants


class Viewer:
    def __get_letter(self, j):
        return chr(ord('A') + j - 1)

    def field_out(self, field, secret):
        print(' ' * 5, end='')
        for i in range(0, field.size() + 1):
            if i != 0:
                print(i, end=(' ' * (3 - len(str(i))) + '|'))
            for j in range(1, field.size() + 1):
                if i == 0:
                    print(self.__get_letter(j), end=' ')
                else:
                    print(field.get_cell(i, j).out(secret), end='')
            print()
        print()

    def first_output(self, autodetected, field):
        if autodetected:
            self.field_out(field, True)
            return
        print("There's your field, where u have to placed ships:")
        self.field_out(field, False)

    def bot_starts(self):
        print('Random decided, that bot starts first.')

    def player_starts(self):
        print('Random decided, that you start first.')

    def shot_output(self, pos, creature, status=None):
        print(creature + ' fired into the cage ', chr(
            ord('A') + pos[1] - 1), pos[0], sep='')

    def shot(self, status, field):
        print(constants.SHOT_STATUS[status])
        self.field_out(field, False)
