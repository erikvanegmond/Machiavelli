from player import *
from card import *
import unittest


class TestPlayer(unittest.TestCase):
    def test_player_init(self):
        player = Player("test player")
        actual_result = player.name
        correct_result = "test player"
        self.assertEquals(actual_result, correct_result)

    def test_player_build(self):
        test_card = Card('test card', 2, 'grey', 2)
        player = Player("test player")
        player.gold = 2
        player.hand = [test_card]
        player.city = []

        self.assertTrue(player.build(0))

        #card is now in the city
        actual_result = player.city
        correct_result = [test_card]
        self.assertEquals(actual_result, correct_result)

        #hand is now empty
        actual_result = player.hand
        correct_result = []
        self.assertEquals(actual_result, correct_result)

        #there should be no more gold
        actual_result = player.gold
        correct_result = 0
        self.assertEquals(actual_result, correct_result)


