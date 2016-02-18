import unittest

from game.player import *
from game.character import *


class TestCharacter(unittest.TestCase):
    def test_all_characters(self):
        deck.read_deck()
        for char in Character.characters:
            actual_response = eval(char)(Player()).__repr__()
            correct_response = char
            self.assertEqual(actual_response, correct_response)

    def test_equals(self):
        char1 = Assassin(Player("p1"))
        char2 = Assassin(Player("p1"))
        self.assertEqual(char1, char2)
