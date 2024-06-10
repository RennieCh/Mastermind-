"""
   CS5001
   Fall 2023
   Runying Chen
   Project - Test_mastermind_game
"""

from mastermind_game import MastermindGame
import unittest

class TestCountBullsAndCows(unittest.TestCase):
    '''
        Test suite for the count_bulls_and_cows method in the MastermindGame class.
        It is designed to ensure accurate counting of bulls (correct color in correct position)
        and cows (correct color in incorrect position) based on different combinations of
        secret_code and user's click_colors

        Noted, there are no dulplicate colors is allowed, and only 6 colors can be choosen. 
    '''

    def test_all_bulls(self):
        # test when all colors in click_colors match secret_code in the correct position (bulls)
        # 4 correct colors at correct places is (4 bulls, 0 cows)
        game = MastermindGame()
        game.secret_code = ["red", "blue", "green", "yellow"]
        game.click_colors = ["red", "blue", "green", "yellow"]
        self.assertEqual(game.count_bulls_and_cows(), (4, 0))

        game.secret_code = ["green", "yellow", "purple", "black"]
        game.click_colors = ["green", "yellow", "purple", "black"]
        self.assertEqual(game.count_bulls_and_cows(), (4, 0))

    def test_all_cows(self):
        # test when all colors in click_colors match secret_code in the incorrect position (cows)
        # 4 correct colors at incorrect places (0 bulls, 4 cows)
        game = MastermindGame()
        game.secret_code = ["red", "blue", "green", "yellow"]
        game.click_colors = ["yellow", "green", "blue", "red"]
        self.assertEqual(game.count_bulls_and_cows(), (0, 4))

        game.secret_code = ["green", "yellow", "purple", "black"]
        game.click_colors = ["black", "purple", "yellow", "green"]
        self.assertEqual(game.count_bulls_and_cows(), (0, 4)) 

    def test_mixed_bulls_and_cows(self):
        # test when there are mix bulls and cows
        # 1 bulls and 3 cows
        game = MastermindGame()
        game.secret_code = ["red", "blue", "green", "yellow"]
        game.click_colors = ["red", "green", "yellow", "blue"]
        self.assertEqual(game.count_bulls_and_cows(), (1, 3))

        # 2 bulls and 2 cows
        game.secret_code = ["red", "blue", "green", "yellow"]
        game.click_colors = ["red", "blue", "yellow", "green"]
        self.assertEqual(game.count_bulls_and_cows(), (2, 2))

        # 3 bulls and 0 cows
        game.secret_code = ["red", "blue", "green", "yellow"]
        game.click_colors = ["red", "blue", "green", "black"]
        self.assertEqual(game.count_bulls_and_cows(), (3, 0))

        # 0 bulls and 2 cows
        game.secret_code = ["red", "black", "green", "yellow"]
        game.click_colors = ["purple", "blue", "yellow", "black"]
        self.assertEqual(game.count_bulls_and_cows(), (0, 2))

        # 0 bulls and 3 cows
        game.secret_code = ["purple", "blue", "yellow", "black"]
        game.click_colors = ["yellow", "purple", "black", "green"]
        self.assertEqual(game.count_bulls_and_cows(), (0, 3))

def main():
    unittest.main(verbosity = 3)

main()
