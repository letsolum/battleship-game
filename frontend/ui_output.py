from frontend.board import Board, FiringCell
import pygame, sys
import frontend.constants as constants


class UiOutput:
    def __init__(self, bot: Board, player: Board, bot_fld, player_fld):
        self.bot_board = bot
        self.player_board = player
        self.all_sprites = pygame.sprite.Group()
        self.already_outputted = set()
        self.player_field = player_fld
        self.bot_field = bot_fld

    def update_pos(self, pos, board):
        pos = [pos[0] - 1, pos[1] - 1]
        pos[0] *= board.offset
        pos[1] *= board.offset
        pos = [pos[0] + board.pos[0], pos[1] + board.pos[1]]
        return pos

    def add_cover(self, field, board):
        dead_inside = field.all_dead()
        for pos in dead_inside:
            curr_pos = self.update_pos(pos, board)
            if tuple(curr_pos) not in self.already_outputted:
                self.all_sprites.add(FiringCell(curr_pos, False))
                self.already_outputted.add(tuple(curr_pos))

    def shot_output(self, pos, creature, status):
        source = []
        if creature == 'Player':
            source = [self.bot_board, self.bot_field]
        else:
            source = [self.player_board, self.player_field]
        pos = self.update_pos(pos, source[0])
        self.all_sprites.add(FiringCell(pos, status >= 0))
        self.already_outputted.add(tuple(pos))
        if constants.SHOT_STATUS[status] == 'Dead.':
            self.add_cover(source[1], source[0])

    def shot(self, status, field):
        pass

    def run(self, clock, screen):
        for obj in self.player_board.get_objects():
            if not isinstance(obj, pygame.sprite.Sprite):
                continue
            self.all_sprites.add(obj)
        for obj in self.bot_board.get_objects():
            if not isinstance(obj, pygame.sprite.Sprite):
                continue
            self.all_sprites.add(obj)
        while True:
            clock.tick(constants.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.all_sprites.draw(screen)
            pygame.display.flip()
            yield

    def smb_win(self, creature, screen):
        font = pygame.font.SysFont('Arial', constants.FONT_SIZE * constants.BOARD_SIZE)
        screen.blit(font.render(creature + 'WIN!', False, constants.RED), constants.WIN_POS)
        pygame.display.update()
        pygame.display.flip()

    def __del__(self):
        pygame.quit()
        del self.all_sprites, self.bot_field, self.player_field, self.bot_board, self.player_board, self.already_outputted
