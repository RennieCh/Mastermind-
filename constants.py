from Point import Point

# marble colors
COLORS = ("red", "blue", "green", "yellow", "purple", "black")

# x and y coordinates for tries status, and size of tries cycle
TRIES_X = [-232, -178, -124, -70]
TRIES_Y = [280, 230, 180, 130, 80, 30, -20, -70, -120, -170]
TRIES_SIZE = 15

# x and y coordinates for scoring pegs, and size of pegs cycle
PEGS_X = [0, 18]
PEGS_Y = [300, 280, 250, 230, 200, 180, 150, 130, 100, 80, 50, 30, 0, -20,
          -50, -70, -100, -120, -150, -170]
PEGS_SIZE = 4

# x and y coordinates for play area circle, and size of play cycle
PLAY_X = [-280, -220, -160, -100, -40, 20]
PLAY_Y = [-300]
PLAY_SIZE = 20

# constants for game board
STATUS_AREA_X = -320
STATUS_AREA_Y = 330
STATUS_AREA_LENTH = 535
STATUS_AREA_WIDTH = 430

LEADER_AREA_X = 130
LEADER_AREA_Y = 330
LEADER_AREA_LENTH = 535
LEADER_AREA_WIDTH = 180

PLAY_AREA_X = -320
PLAY_AREA_Y = -220
PLAY_AREA_LENTH = 120
PLAY_AREA_WIDTH = 630

# checkbutton, xbutton, and quit button position points and GIF name
CHECK_POS = Point(90, -280)    # postion for the shape
CHECK_GIF = "checkbutton.gif"
CHECK_WIDTH = 60
CHECK_RADIUS = 60/2
CHECK_PIONT = Point(90, -307) # default point to detect clicked area calculation

XBUTTON_POS = Point(160, -280)  # postion for the shape
XBUTTON_GIF = "xbutton.gif"
XBUTTON_WIDTH = 60
XBUTTON_RADIUS = 60/2
XBUTTON_PIONT = Point(160, -307) # default point to detect clicked area calculation

QUIT_POS = Point(250 , -280)    # postion for the shape
QUIT_GIF = "quit.gif"
QUIT_WIDTH = 55
QUIT_LENGTH = 100
QUIT_PIONT = Point(202, -307)   # default point to detect clicked area calculation

# constants for tries
TRY_MARBLES = 4
TRY_ARROW_X = [-270]
TRY_ARROW_Y = [295, 245, 195, 145, 95, 45, -5, -55, -105, -155]
MAX_TRIES = 10

# win, lose, and quit game gif for pop up windows 
WIN_GIF = 'winner.gif'
LOSE_GIF = 'Lose.gif'
QUIT_GAME = 'quitmsg.gif'
NOTFINDLEADER = 'leaderboard_error.gif'

# learder file
LEADERFILE = 'leaderboard.txt'
