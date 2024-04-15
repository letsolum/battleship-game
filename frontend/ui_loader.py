import pygame
import sys, copy
import frontend.constants as constants
from frontend.board import Board
from backend.field import Field


class UiLoader:
    screen = None
    clock = None
    all_sprites = None
    first_board = None
    second_board = None
    font = None

    def pygame_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        pygame.display.set_caption("BATTLESHIP")
        self.clock = pygame.time.Clock()
        self.screen.fill(constants.WHITE)
        self.all_sprites = pygame.sprite.Group()
        self.first_board = Board([constants.BOARD_WIDTH, constants.BOARD_HEIGHT])
        self.second_board = Board(
            [self.first_board.pos[0] + constants.STICK_WIDTH + constants.SPACE_BETWEEN_BOARDS, self.first_board.pos[1]])
        self.font = pygame.font.SysFont('Arial', constants.FONT_SIZE)
        special_font = pygame.font.SysFont(
            'Arial', constants.SPECIAL_FONT_SIZE)
        self.screen.blit(special_font.render("BOT FIELD", False, constants.BLACK), (
            self.first_board.pos[0] + constants.BOTFIELD_X, self.first_board.pos[1] - constants.BOTFIELD_Y))
        self.screen.blit(special_font.render("YOUR FIELD", False, constants.BLACK), (
            self.second_board.pos[0] + constants.YOURFIELD_X,
            self.second_board.pos[1] - constants.YOURFIELD_Y))
        image_field = pygame.image.load('utils/field_background.jpg')
        self.screen.blit(image_field, (self.first_board.pos[0] + 1, self.first_board.pos[1]))
        image_field = pygame.image.load('utils/field_background_2.jpg')
        self.screen.blit(image_field, (self.second_board.pos[0] + 1, self.second_board.pos[1]))

    def __init__(self):
        self.__player_field = copy.deepcopy(Field())
        self.pygame_init()
        for obj in self.first_board.get_objects():
            if isinstance(obj, pygame.sprite.Sprite):
                self.all_sprites.add(obj)
            else:
                self.screen.blit(obj[0], (obj[1][0], obj[1][1]))
        for obj in self.second_board.get_objects():
            if isinstance(obj, pygame.sprite.Sprite):
                self.all_sprites.add(obj)
            else:
                self.screen.blit(obj[0], (obj[1][0], obj[1][1]))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def track_mouse(self):
        middle_mouse_button_pressed = False
        click_pos = []
        while not middle_mouse_button_pressed:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    middle_mouse_button_pressed = True
                    click_pos = pygame.mouse.get_pos()
                    break
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.time.wait(10)
        return click_pos

    def next_mouse_move(self, brd):
        while True:
            self.clock.tick(constants.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            curr_pos = self.track_mouse()
            curr_pos = [curr_pos[0], curr_pos[1]]
            if brd.inside(curr_pos[0], curr_pos[1]):
                curr_pos[0] -= brd.pos[0]
                curr_pos[1] -= brd.pos[1]
                curr_pos[0] /= brd.offset
                curr_pos[1] /= brd.offset
                curr_pos[0] = int(curr_pos[0]) + 1
                curr_pos[1] = int(curr_pos[1]) + 1
                yield curr_pos
                print(*curr_pos)
            self.all_sprites.draw(self.screen)
            if self.QUIT():
                pygame.quit()
                sys.exit()
            pygame.display.flip()

    def place_start(self, start):
        self.screen.blit(self.font.render(
            'S', False, constants.BLACK),
            (self.second_board.pos[0] + (start[0] - 1) * self.second_board.offset + 5,
             self.second_board.pos[1] + (start[1] - 1) * self.second_board.offset + 3))
        pygame.display.flip()

    def place_cropped_img(self, start, image):
        cut_surface = pygame.Surface(
            (self.second_board.offset - constants.BOARD_EPS, self.second_board.offset - constants.BOARD_EPS))
        cut_surface.blit(image, (0, 0), (
            (start[0] - 1) * self.second_board.offset, (start[1] - 1) * self.second_board.offset,
            self.second_board.offset - constants.BOARD_EPS, self.second_board.offset - constants.BOARD_EPS))
        self.screen.blit(cut_surface,
                         (
                         self.second_board.pos[0] + (start[0] - 1) * self.second_board.offset + constants.BOARD_EPS - 1,
                         self.second_board.pos[1] + (
                                     start[1] - 1) * self.second_board.offset + constants.BOARD_EPS - 1))
        pygame.display.flip()

    def input_field(self):
        positions = []
        mouse = self.next_mouse_move(self.second_board)
        image = pygame.image.load('utils/field_background_2.jpg')
        for _ in range(constants.BOARD_SIZE):
            start = next(mouse)
            self.place_start(start)
            end = next(mouse)
            while not self.__player_field.place_boat(start, end):
                self.place_cropped_img(start, image)
                start = next(mouse)
                self.place_start(start)
                pygame.display.flip()
                end = next(mouse)
            self.place_cropped_img(start, image)
            positions.append([start, end])
            for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                    self.screen.blit(self.font.render(
                        'B', False, constants.GREEN),
                        (self.second_board.pos[0] + (x - 1) * self.second_board.offset + constants.BOARD_EPS + 2,
                         self.second_board.pos[1] + (y - 1) * self.second_board.offset + constants.BOARD_EPS))
            pygame.display.flip()
        return positions

    def get_input(self):
        mouse = self.next_mouse_move(self.first_board)
        pos = next(mouse)
        return pos

    def QUIT(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def __del__(self):
        pygame.quit()
        del self.screen, self.first_board, self.second_board, self.all_sprites, self.__player_field, self.clock
