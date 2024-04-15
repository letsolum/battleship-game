import random
import sys, copy
from time import sleep
from frontend.view_out import Viewer
from frontend.loader import Loader
from frontend.ui_loader import UiLoader
from frontend.ui_output import UiOutput
from backend.player import Player
from backend.bot import Bot

def play(out_put, in_put, player, bot, order):
    window = out_put.run(in_put.clock, in_put.screen)
    while not bot.lose() and not player.lose():
        if order == 1:
            pos = bot.next_turn()
            status = player.enemy_shot(pos)
            if status > 0:
                order = 1 - order
            out_put.shot_output(pos, 'Bot', status)
            out_put.shot(status, player.get_field())
        else:
            pos = in_put.get_input()
            status = bot.enemy_shot(pos)
            if status > 0:
                order = 1 - order
            out_put.shot_output(pos, 'Player', status)
            out_put.shot(status, bot.get_field())
        next(window)
        order = 1 - order
    if bot.lose():
        out_put.smb_win('Player', in_put.screen)
    else:
        out_put.smb_win('Bot', in_put.screen)
    sleep(3)

def run():
    args = sys.argv
    player = copy.deepcopy(Player())
    bot = copy.deepcopy(Bot())
    in_put = None
    out_put = None
    order = random.randint(0, 1)
    if args[-1] in {'-c', '--console'}:
        in_put = copy.deepcopy(Loader())
        out_put = copy.deepcopy(Viewer())
        autodata = in_put.load_autodata()
        if autodata:
            out_put.first_output(True, player.get_field())
            player.construct_field(autodata)
        else:
            out_put.first_output(False, player.get_field())
            positions = in_put.input_field(out_put)
            player.construct_field(positions)

        bot.generate_field()
        if order == 1:
            out_put.bot_starts()
        else:
            out_put.player_starts()

    else:
        in_put = UiLoader()
        out_put = UiOutput(in_put.first_board, in_put.second_board,
                           bot.get_field(), player.get_field())
        positions = in_put.input_field()
        player.construct_field(positions)
        bot.generate_field()
    play(out_put, in_put, player, bot, order)
    del bot, player, in_put, out_put
