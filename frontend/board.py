import pygame
import frontend.constants as constants


class Stick(pygame.sprite.Sprite):
    def __init__(self, position, horizontal):
        pygame.sprite.Sprite.__init__(self)
        length = constants.STICK_WIDTH
        width = constants.STICK_HEIGHT
        if not horizontal:
            length, width = width, length
        self.image = pygame.Surface(
            (length, width))
        self.image.fill(constants.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (position[0] + length / 2, position[1] + width / 2)


class FiringCell(pygame.sprite.Sprite):
    def __init__(self, position, dead_inside):
        pygame.sprite.Sprite.__init__(self)
        l = constants.STICK_WIDTH / constants.BOARD_SIZE / 1.5
        self.image = pygame.Surface((l, l))
        self.image.fill(constants.BLACK)
        if dead_inside:
            self.image.fill(constants.RED)
        self.rect = self.image.get_rect()
        self.rect.center = (position[0] + 15, position[1] + 15)


class Board:
    def __init__(self, position):
        self.objects = []
        self.pos = position
        self.offset = constants.STICK_WIDTH / constants.BOARD_SIZE
        hor = 'A'
        font = pygame.font.SysFont('Arial', constants.FONT_SIZE)
        for i in range(constants.BOARD_SIZE + 1):
            self.objects.append(
                Stick([position[0] + i * self.offset, position[1]], False))
            self.objects.append(
                Stick([position[0], position[1] + i * self.offset], True))
            if i == constants.BOARD_SIZE:
                continue
            self.objects.append([font.render(
                chr(ord(hor) + i), True, constants.BLUE),
                [position[0] + i * self.offset + 3 * constants.BOARD_EPS,
                 position[1] - constants.FONT_SIZE - constants.BOARD_EPS]])
            self.objects.append([font.render(
                str(i + 1), True, constants.BLUE),
                [position[0] - constants.FONT_SIZE - len(str(i + 1)) * constants.BOARD_EPS,
                 position[1] + i * self.offset + 2 * constants.BOARD_EPS]])

    def get_objects(self):
        return self.objects

    def inside(self, x, y):
        return x >= self.pos[0] and x - self.pos[0] < constants.STICK_WIDTH and y >= self.pos[1] and y - self.pos[
            1] < constants.STICK_WIDTH

    def __del__(self):
        del self.pos, self.objects, self.offset
