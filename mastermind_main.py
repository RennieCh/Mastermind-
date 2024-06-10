"""
    CS5001
    FALL 2023
    Runying Chen
    Project - Mastermind Main
"""

import turtle
from Point import Point
from Marble import Marble
import math
import random
import time
import os
from mastermind_game import MastermindGame, calculate_distance, record_error
from constants import COLORS, TRIES_X, TRIES_Y, TRIES_SIZE, PEGS_X, \
     PEGS_Y, PEGS_SIZE, PLAY_X, PLAY_Y, PLAY_SIZE, STATUS_AREA_X, \
     STATUS_AREA_Y, STATUS_AREA_LENTH, STATUS_AREA_WIDTH, LEADER_AREA_X, \
     LEADER_AREA_Y, LEADER_AREA_LENTH, LEADER_AREA_WIDTH, PLAY_AREA_X, \
     PLAY_AREA_Y, PLAY_AREA_LENTH, PLAY_AREA_WIDTH, CHECK_POS, CHECK_GIF, \
     CHECK_WIDTH, CHECK_RADIUS, CHECK_PIONT, XBUTTON_POS, XBUTTON_GIF, \
     XBUTTON_WIDTH, XBUTTON_RADIUS, XBUTTON_PIONT, QUIT_POS, QUIT_GIF, \
     QUIT_WIDTH, QUIT_LENGTH, QUIT_PIONT, TRY_MARBLES, TRY_ARROW_X, \
     TRY_ARROW_Y, MAX_TRIES, WIN_GIF, LOSE_GIF, QUIT_GAME, NOTFINDLEADER, \
     LEADERFILE

def main():
    try:
        game = MastermindGame()
        turtle.mainloop()
    except Exception as e:
        record_error(e)

if __name__ == "__main__":
    main()  
