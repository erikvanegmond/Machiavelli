from character import *
import player
import unittest


class TestCharacter(unittest.TestCase):
    def test_all_characters(self):
        for char in Character.characters:
            actual_response = eval(char)(player.Player()).__repr__()
            correct_response = char
            self.assertEqual(actual_response, correct_response)
