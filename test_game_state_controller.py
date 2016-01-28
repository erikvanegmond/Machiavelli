from game_state_controller import *
import unittest


class TestGameStateController(unittest.TestCase):
    def test_add_player(self):
        deck.read_deck()  # resetting the deck
        gsc = GameStateController(4)

        gsc.add_player("Player 1")
        gsc.add_player("Player 2")
        gsc.add_player("Player 3")
        gsc.add_player("Player 4")

        actual_result = gsc.players
        correct_result = [Player("Player 1"), Player("Player 2"), Player("Player 3"), Player("Player 4")]
        self.assertEquals(actual_result, correct_result)

        with self.assertRaises(IndexError):
            gsc.add_player("Player 5")

    def test_player_order_players(self):
        deck.read_deck()  # resetting the deck

        gsc = GameStateController(4)

        gsc.add_player("Player 1")
        gsc.add_player("Player 2")
        gsc.add_player("Player 3")
        gsc.add_player("Player 4")

        gsc.king_player = gsc.players[0]
        actual_result = gsc.get_player_order(order='players')
        correct_result = [Player("Player 1"), Player("Player 2"), Player("Player 3"), Player("Player 4")]
        self.assertEqual(actual_result, correct_result)

        gsc.king_player = gsc.players[1]
        actual_result = gsc.get_player_order(order='players')
        correct_result = [Player("Player 2"), Player("Player 3"), Player("Player 4"), Player("Player 1")]
        self.assertEqual(actual_result, correct_result)

    def test_player_order_characters(self):
        deck.read_deck()  # resetting the deck

        gsc = GameStateController(4)

        gsc.add_player("Player 1")
        gsc.add_player("Player 2")
        gsc.add_player("Player 3")
        gsc.add_player("Player 4")

        gsc.players[0].character = gsc.character_deck[3]
        gsc.players[1].character = gsc.character_deck[2]
        gsc.players[2].character = gsc.character_deck[6]
        gsc.players[3].character = gsc.character_deck[1]

        actual_result = gsc.get_player_order(order='characters')
        correct_result = [Player("Player 4"), Player("Player 2"), Player("Player 1"), Player("Player 3")]
        self.assertEqual(actual_result, correct_result)

    def test_update_state(self):
        deck.read_deck()  # resetting the deck
        gsc = GameStateController(4)

        gsc.add_player("Player 1")
        gsc.add_player("Player 2")
        gsc.add_player("Player 3")
        gsc.add_player("Player 4")

        expected_results = ["GameStates.start_game <class 'player.Player'>",
                            "GameStates.rounds_pick_characters_prepare Player 1",
                            "GameStates.rounds_pick_characters Player 1",
                            "GameStates.rounds_pick_characters Player 2",
                            "GameStates.rounds_pick_characters Player 3",
                            "GameStates.rounds_pick_characters Player 4",
                            "GameStates.turns_order_players <class 'player.Player'>"]
        for correct_result in expected_results:
            actual_result = str(gsc.state) + " " + str(gsc.current_player)
            self.assertEquals(actual_result, correct_result)
            if gsc.state == GameStates.turns_order_players:
                gsc.players[0].character = gsc.character_deck[3]
                gsc.players[1].character = gsc.character_deck[2]
                gsc.players[2].character = gsc.character_deck[6]
                gsc.players[3].character = gsc.character_deck[1]
            gsc.update_state()

        expected_results = ["GameStates.turns_call_character <class 'player.Player'>",
                            "GameStates.turns_begin Player 4",
                            "GameStates.turns_income Player 4",
                            "GameStates.turns_general Player 4",
                            "GameStates.turns_end Player 4",
                            "GameStates.turns_call_character Player 4",
                            "GameStates.turns_begin Player 2",
                            "GameStates.turns_income Player 2",
                            "GameStates.turns_general Player 2",
                            "GameStates.turns_end Player 2",
                            "GameStates.turns_call_character Player 2",
                            "GameStates.turns_begin Player 1",
                            "GameStates.turns_income Player 1",
                            "GameStates.turns_general Player 1",
                            "GameStates.turns_end Player 1",
                            "GameStates.turns_call_character Player 1",
                            "GameStates.turns_begin Player 3",
                            "GameStates.turns_income Player 3",
                            "GameStates.turns_general Player 3",
                            "GameStates.turns_end Player 3",
                            "GameStates.turns_call_character Player 3",
                            "GameStates.rounds_pick_characters_prepare Player 3"]

        for correct_result in expected_results:
            actual_result = str(gsc.state) + " " + str(gsc.current_player)
            self.assertEquals(actual_result, correct_result)
            gsc.update_state()

