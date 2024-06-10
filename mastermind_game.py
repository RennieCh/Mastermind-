"""
    CS5001
    FALL 2023
    Runying Chen
    Project - Mastermind Class
"""
import turtle
from Point import Point
from Marble import Marble
import math
import random
import time
import os
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

# Helper functions
def calculate_distance(point_1, point_2, radius):
    '''
        Function: calculate_distance
            calculate the distance between 2 points of a circle
        Parameters:
            2 Point objects with x and y coordinates, for example Point(0, 0)
        Return:
            float(distance btween 2 points)
    '''
    return math.sqrt((point_2.x - point_1.x) ** 2 + (point_2.y -
                                                     (point_1.y + radius)) ** 2)

def record_error(exception):
    date_time = time.strftime('%Y-%m-%d %H:%M')
    mode = 'a' if os.path.exists('mastermind_errors.err') else 'w'
    with open('mastermind_errors.err', mode) as file:
        # Write the error and occured time
        file.write(f'An exception: {type(exception).__name__}, reported at {date_time}\n')

class MastermindGame:
    COLORS = COLORS

    def __init__(self):
        '''
            constructors of MastermindGame
        '''
        self.clicks = 0
        self.click_colors = []
        self.current_try = 0
        self.secret_code = self.generate_secret_code()
        self.player_name = self.pop_window("5001 MasterMind", "Your Name:")
        self.status_marbles = self.create_marbles(self.create_marble_pos(TRIES_X, TRIES_Y),
                                                  TRIES_SIZE)
        self.pegs_marbles = self.create_marbles(self.create_marble_pos(PEGS_X, PEGS_Y),
                                                PEGS_SIZE)
        self.play_marbles = self.create_play_marbles()
        self.arrow = self.create_try_arrow()
        self.score = None
        self.initialize_screen()
        self.draw_game_board()
        self.draw_empty_marbles()
        self.draw_play_marbles()
        self.draw_buttons()
        self.write_best_scores(LEADERFILE)
        turtle.Screen().onclick(self.click_control)
    
    def initialize_screen(self):
        '''
            Method: initialize_screen()
                initialize the gameboard screen
        '''
        width = 680
        heigh = 720
        self.screen = turtle.Screen()    
        self.screen.setup(width, heigh)  #set up the size for a turtle screen
        self.screen.title("CS5001 MasterMind by Runying Chen")

    def pop_window(self, title, prompt):
        '''
            Method: pop_window
                pop up a dialog window for users input
            Parameters:
                title (string)
                prompt (string)
            Return:
                result(string)
        '''
        return turtle.textinput(title, prompt)
    
    def draw_rectangle(self, x, y, length, width, pen_color):
        '''
            Methof: draw_rectangle
                draw a rectangle in gameboard
            Parameter:
                x-coordinate (int)
                y-coordinate (int)
                length (int)
                width (int)
                pen_color (string)
        '''
        t = turtle.Turtle()
        t.speed(0)
        t.pensize(6)
        t.color(pen_color)
        t.up()
        t.goto(x, y)
        t.down()
        for i in range(2):
            t.forward(width)
            t.right(90)
            t.forward(length)
            t.right(90)
        t.hideturtle()

    def draw_game_board(self):
        '''
            Method: draw_game_board
                draw the play area, status area, and leader board in gameboard
        '''
        # draw the status area
        self.draw_rectangle(STATUS_AREA_X, STATUS_AREA_Y, STATUS_AREA_LENTH,
                            STATUS_AREA_WIDTH, "black")

        # draw the leader area
        self.draw_rectangle(LEADER_AREA_X, LEADER_AREA_Y, LEADER_AREA_LENTH,
                            LEADER_AREA_WIDTH, "blue")

        # draw the play area
        self.draw_rectangle(PLAY_AREA_X, PLAY_AREA_Y, PLAY_AREA_LENTH,
                            PLAY_AREA_WIDTH, "black")

        # write on leader board
        tt = turtle.Turtle()
        tt.color("blue")
        tt.up()
        tt.goto(160, 300)
        tt.write("Leaders: ", True, align = "left", font = ('Arial', 20, 'normal'))
        tt.hideturtle()

    def create_try_arrow(self): 
        '''
            Method: create_try_arrow
                create an arrow to point at the status marbles for each try
            Return:
                a turtle object
        '''
        arrow = turtle.Turtle()
        arrow.turtlesize(2)
        arrow.fillcolor('red')
        arrow.up()
        arrow.goto(TRY_ARROW_X[0], TRY_ARROW_Y[0])
        arrow.down()
        return arrow

    def move_try_arrow(self, turtle_object, x, y):
        '''
            Method: move_try_arrow
                move a turtle object to a given x and y coordinates for each try
            Parameter:
                a turtle object
                x coordiante
                y coordinate
        '''
        turtle_object.up()
        turtle_object.goto(x, y)
        turtle_object.down

    def update_leaderfile(self, score, name, file_name):
        '''
            Method: update_leaderfile
                Update/write on the leaderfile with the given score and name.
            Parameter:
                score (int)
                name (string)
                file_name (string)
        '''
        # Format the line to write to the file
        line_to_write = f"{score + 1} : {name}\n"
        
        # Check if the file exists to determine the mode
        mode = 'a' if os.path.exists(file_name) else 'w'
        
        # Open the file with the appropriate mode
        with open(file_name, mode) as file:
            # Write the new score entry
            file.write(line_to_write)

    def read_scores(self, file_name):
        '''
            Method: read_scores
                Reads and returns scores from a file.
            Parameter:
                file_name (string): the file path
            Returns:
                list of tuples: ('score' : 'name')
        '''
        if not os.path.exists(file_name):
            self.pop_gif(NOTFINDLEADER, 5)
            return []

        # Read the scores from the file and sort them
        with open(file_name, 'r') as file:
            lines = file.readlines()
            scores = []
            for line in lines:
                score, name = line.strip().split(' : ')
                scores.append((int(score), name))
            # Sort the list of tuples by the score
            scores.sort(key=lambda x: x[0])
        return scores
    
    def display_scores(self, scores):
        '''
            Method: display_score
                Displays scores using Turtle
            Parameter:
                score (list of tuples)
        '''
        t = turtle.Turtle()
        t.hideturtle()
        t.color('blue')
        t.up()

        # the x, y coordinares where the scores display
        coordinates = [(160, 265), (160, 235), (160, 205)]

        # display 3 best scores
        for i, (score, name) in enumerate(scores[:3]):
            x, y = coordinates[i]
            t.goto(x, y)
            t.write(f"{score} : {name}", True, align="left",
                    font=('Arial', 15, 'normal'))

    def write_best_scores(self, file_name):
        '''
            Method: write_best_scores
                Reads scores from a file and displays them in gameboard
            Parameter:
                file_name (string)
        '''
        scores = self.read_scores(file_name)
        if scores:
            self.display_scores(scores)
            
    def create_button(self, gif, x, y):
        '''
            Method: create_button
                use a gif to create a button at a given x and y coordinates
            Parameters:
                gif(string - name of the gif file)
                x coordinate
                y coordinate
        '''
        pen = turtle.Turtle()
        screen = turtle.Screen()
        pen.hideturtle()
        pen.up()
        # change the turtle object as the gif
        screen.addshape(gif)
        pen.shape(gif)
        pen.goto(x, y)
        pen.down()
        pen.showturtle()

    def create_marble_pos(self, x_list, y_list):
        '''
            Method: create_marble_pos
                create point position for the marbles to be displayed in gameboard
            Parameter:
                x_list (List of x coordinates)
                y_list (list of y coordinates)
            Return:
                a list of Point objects
        '''
        marble_positions = []
        for y in y_list:
            for x in x_list:
                position = Point(x, y)
                marble_positions.append(position)
        return marble_positions

    def create_marbles(self, marble_positions, marble_radius):
        '''
            Method: creat_marble
                create the status/peg marbles in gameboard with given positions
            Parameter:
                a list of Point objects
                marble_radius (int)
            Return:
                a list of marble objects
        '''
        marbles = [] 
        for position in marble_positions:
            marble = Marble(position, 'empty', size = marble_radius)
            marbles.append(marble)
        return marbles

    def create_play_marbles(self):
        '''
            Method: create_play_marbles
                create play area marbles with given colors
            Parameter:
                none
            Return:
                a dictionary of marble objects
        '''
        # generate position points
        play_positions = self.create_marble_pos(PLAY_X, PLAY_Y)

        # create the marble objects
        play_marbles = []
        for i in range(len(COLORS)):
            play_marbles.append(Marble(play_positions[i], self.COLORS[i], PLAY_SIZE))

        # use dictionary to record the play marbles, so it can be index by colors
        marble_dict = {}
        for i in range(len(self.COLORS)):
            marble_dict[self.COLORS[i]] = play_marbles[i]
        return marble_dict

    def draw_empty_marbles(self):
        '''
            Method: draw_empty_marbles
                draw the empty marbles when the game starts
        '''
        # Draw empty marbles for status area
        for marble in self.status_marbles:
            marble.draw_empty()

        # Draw empty marbles for pegs
        for marble in self.pegs_marbles:
            marble.draw_empty()

    def draw_play_marbles(self):
        '''
            Method: draw_play_marbles
                draw the play marbles when game starts
        '''
        for color in self.COLORS:
            self.play_marbles[color].draw()

    def draw_buttons(self):
        '''
            Methof: draw_buttons
                draw the check, x, and quit buttons when game starts
        '''
        # Draw buttons
        self.create_button(CHECK_GIF, CHECK_POS.x, CHECK_POS.y)
        self.create_button(XBUTTON_GIF, XBUTTON_POS.x, XBUTTON_POS.y)
        self.create_button(QUIT_GIF, QUIT_POS.x, QUIT_POS.y)


    def get_play_marble(self, x, y, play_marbles):
        '''
            Method: get_play_marble
                When player clicks on a color marble at the play area,
                return the Marble object
            Parameters:
                x (int): x-coordinate
                y (int): y-coordinate
                play_marbles (dict): collection of marble objects
            Return:
                a Marble object or None
        '''
        point = Point(x, y)
        play_positions = self.create_marble_pos(PLAY_X, PLAY_Y)

        for i, color in enumerate(COLORS):
            if calculate_distance(play_positions[i], point, PLAY_SIZE) <= PLAY_SIZE:
                return play_marbles[color]
        return None

    def click_check_button(self, x, y):
        '''
            Method: click_check_botton
                confrim if a player click on the check botton
            Parameters:
                x and y coordinates
            Return:
                a boolean (True means the player click on the check botton)
        '''
        point = Point(x, y)
        if calculate_distance(CHECK_PIONT, point, CHECK_RADIUS) <= CHECK_RADIUS:
            return True

    def click_x_button(self, x, y):
        '''
            Method: click_x_botton
                confrim if a player click on the Xbotton
            Parameters:
                x and y coordinates
            Return:
                a boolean (True means the player click on the Xbotton)
        '''
        point = Point(x, y)
        if calculate_distance(XBUTTON_PIONT, point, XBUTTON_RADIUS) <= XBUTTON_RADIUS:
            return True

    def click_quit_button(self, x, y):
        '''
            Method: click_quit_botton
                confrim if a player click on the Xbotton
            Parameters:
                x-coordinate (int)
                y-coordinate (int)
            Return:
                a boolean (True means the player quit on the Xbotton)
        '''
        if QUIT_PIONT.x <= x <= QUIT_PIONT.x + QUIT_LENGTH \
           and QUIT_PIONT.y <= y <= QUIT_PIONT.y + QUIT_WIDTH:
            # when player click on quit, exit the game
            self.pop_gif(QUIT_GAME, 5)
            turtle.bye()

    def click_control(self, x, y):
        '''
            Method: click_control
                Determines the action based on where the player clicks on the screen.
            Parameters:
                x-coordinate (int)
                y-coordinate (int)
        '''
        # Check if the quit button was clicked
        if self.click_quit_button(x, y):
            return

        # Check if play_marbles was clicked and if the player has chosen enough marbles
        if len(self.click_colors) < TRY_MARBLES:
            play_marble = self.get_play_marble(x, y, self.play_marbles)
            if play_marble:
                self.handle_play_marble_click(play_marble)
                return

        # If the X button was clicked
        elif self.click_x_button(x, y):
            self.handle_x_button()
            return

        # if the check button was clicked 
        elif self.click_check_button(x, y):
            self.handle_check_button()
            return


    def handle_play_marble_click(self, play_marble):
        '''
            Method: handle_play_marble_click
                when a play marbles is clicked, update the status marble for each try
        '''
        # Add the marble's color to the click colors if it hasn't already been chosen
        if play_marble.get_color() not in self.click_colors \
           and len(self.click_colors) < TRY_MARBLES:
            play_marble.draw_empty()
            # the index of the status marble of the current try
            index = self.clicks
            self.status_marbles[index].set_color(play_marble.get_color())
            self.status_marbles[index].draw()
            self.click_colors.append(play_marble.get_color())
            self.clicks += 1

    def handle_x_button(self):
        '''
            Method: handle_x_button
                when x button is clicked, clear the click colors and reset the status marbles
                of the current try and re-draw the play marbles
        '''
        # get the status marbles for the current try
        current_status_marbles = self.status_marbles[self.current_try * TRY_MARBLES :
                                                     self.current_try * TRY_MARBLES + TRY_MARBLES]
        for marble in current_status_marbles:
            marble.draw_empty()
        # re-draw the play marbles
        for color in COLORS:
            self.play_marbles[color].draw()
        self.click_colors = []   # reset click_colors
        self.clicks = self.current_try * TRY_MARBLES

    def handle_check_button(self):
        '''
            Method: handle_check_button
                when a check button is clicked, display the result of bulls and cows
                in peg marbles for the current try.     
        '''
        if len(self.click_colors) != TRY_MARBLES:
            return  # Only proceed if enough marbles are selected

        bulls, cows = self.count_bulls_and_cows()
        self.draw_bulls_and_cows(bulls, cows)

        # if game win 
        if bulls == TRY_MARBLES:
            self.score = self.current_try
            self.handle_game_end(WIN_GIF, f"{self.player_name} wins in {self.current_try + 1} tries!")

        # if game lose
        elif self.current_try == MAX_TRIES - 1 and bulls != TRY_MARBLES:
            self.handle_game_end(LOSE_GIF, "Out of tries!")

        else:
            self.prepare_for_next_try()

    def draw_bulls_and_cows(self, bulls, cows):
        '''
            Method: draw_bulls_and_cows
                draw the bulls and cows resuls using the peg marbles
                black indicates bulls, color at corrent position
                red indicate cowsm, color at incorrent position
            Parameter:
                bulls (int): number of bulls
                cows (int): number of cows
        '''
        # get the pegs marbles object for the current try
        try_pegs = self.pegs_marbles[self.current_try * TRY_MARBLES:
                                     (self.current_try + 1) * TRY_MARBLES]
        for i in range(bulls):
            self.set_peg_and_draw(try_pegs[i], 'black')
        for i in range(cows):
            self.set_peg_and_draw(try_pegs[bulls + i], 'red')

    def set_peg_and_draw(self, peg, color):
        '''
            Method: set_peg_and_draw
                set the color of a peg marble object, then draw the marble
            Parameter:
                peg (a Marble object)
                color (string)
        '''
        peg.set_color(color)
        peg.draw()

    def handle_game_end(self, gif, message):
        '''
            Method: handle_game_end
                if the game win/lose, pop a gif, pop the secret code, update the score,
                and update the leaderfile
            Parameter:
                gif (string): the gif path
                message (string): text to be print on shell
        '''
        print(message)
        self.pop_gif(gif, 5)
        turtle.Screen().onclick(None)  # Disable further clicks
        self.pop_window("Secret code", ', '.join(self.secret_code))
        if self.score is not None:
            self.update_leaderfile(self.score, self.player_name, LEADERFILE)
        # restart the game
        self.reset_game()

    def prepare_for_next_try(self):
        '''
            Method: prepare_for_next_try
                if game does not end, prepare gameboard from current try to next try 
        '''
        if self.current_try < MAX_TRIES - 1:
            # move the try arrow
            self.move_try_arrow(self.arrow, TRY_ARROW_X[0],
                                TRY_ARROW_Y[self.current_try + 1])
            # re-draw the play marbles
            for color in COLORS:
                self.play_marbles[color].draw()
            self.click_colors = []  # Reset for the next try
            self.current_try += 1

    def pop_gif(self, gif, seconds):
        '''
            Method: pop_gif
                pop up a gif turtle at (0, 0) for somes seconds
            Parameter:
                gif(string - name of the gif file)
                seconds(ints)
            Return:
                none
        '''
        pen = turtle.Turtle()
        screen = turtle.Screen()
        pen.hideturtle()
        screen.addshape(gif)
        pen.shape(gif)
        pen.showturtle()
        time.sleep(seconds)
        pen.hideturtle()
        del pen
        screen.update()

    def generate_secret_code(self):
        '''
            Function: generate_secret_code
                ramontly generate a list contains 4 color elements
            Parameter:
                none
            Return:
                a list 
        '''
        return random.sample(COLORS, 4)

    def count_bulls_and_cows(self):
        '''
            Method: count_bulls_and_cows
                Count the number of bulls and cows in the user's guess
                compared to the secret code.
            Returns:
                A tuple with two integers (number of bulls, number of cows).
        '''
        bulls = 0
        cows = 0

        self.secret_code, self.click_colors
        # First pass to count bulls (correct color in the correct position)
        for i in range(len(self.secret_code)):
            if self.click_colors[i] == self.secret_code[i]:
                bulls += 1

        # Second pass to count cows (correct color in the incorrect position)
        for i in range(len(self.secret_code)):
            if self.click_colors[i] != self.secret_code[i] \
               and self.click_colors[i] in self.secret_code:
                cows += 1
        return bulls, cows

    def reset_game(self):
        '''
            Method: reset_game
                resets the game to its initial state
        '''
        # reset all the attribut for the gameborad
        self.screen.clear()
        self.screen.reset()
        self.clicks = 0
        self.click_colors = []
        self.current_try = 0
        self.secret_code = self.generate_secret_code()
        self.player_name = self.pop_window("5001 MasterMind", "Your Name:")
        self.status_marbles = self.create_marbles(self.create_marble_pos(TRIES_X, TRIES_Y),
                                                  TRIES_SIZE)
        self.pegs_marbles = self.create_marbles(self.create_marble_pos(PEGS_X, PEGS_Y),
                                                PEGS_SIZE)
        self.play_marbles = self.create_play_marbles()
        self.arrow = self.create_try_arrow()
        self.score = None
        self.initialize_screen()
        self.draw_game_board()
        self.draw_empty_marbles()
        self.draw_play_marbles()
        self.draw_buttons()
        self.write_best_scores(LEADERFILE)
        turtle.Screen().onclick(self.click_control)
        # update the screen
        self.screen.update()
