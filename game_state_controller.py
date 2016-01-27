from collections import deque

from game_states import *
from player import *


class GameStateController:
    def __init__(self, n_players):
        self.state = GameStates.start_game

        self.players = []
        self.player_order = []
        self.n_players = n_players
        self.current_player = Player
        self.king_player = Player

        self.open_cards = 0

        # TODO Fix for expansion
        if n_players == 4:
            self.open_cards = 2
        elif n_players == 5:
            self.open_cards = 1

        self.character_deck = []

    def add_player(self, player):
        if self.state is GameStates.start_game and len(self.players) < self.n_players:
            self.players.append(Player(player))
        else:
            raise IndexError("To many players")

    def get_player_order(self):
        player_order = deque(self.players)
        player_order.rotate(-self.players.index(self.king_player))
        return list(player_order)

    def update_state(self):
        if self.state == GameStates.start_game:
            self.king_player = self.players[0]
            self.current_player = self.players[0]
            self.state = GameStates.rounds_pick_characters_prepare
        elif self.state == GameStates.rounds_pick_characters_prepare:
            self.player_order = self.get_player_order()
            self.state = GameStates.rounds_pick_characters
        elif self.state == GameStates.rounds_pick_characters:
            self.update_state_rounds_pick_characters()
        elif self.state == GameStates.turns_call_character:

            self.state = GameStates.turns_begin
        elif self.state == GameStates.turns_begin:
            self.state = GameStates.turns_income
        elif self.state == GameStates.turns_income:
            self.state = GameStates.turns_general
        elif self.state == GameStates.turns_general:
            self.state = GameStates.turns_end
        elif self.state == GameStates.turns_end:
            self.state = GameStates.rounds_pick_characters

    def update_state_rounds_pick_characters(self):
        if self.n_players == 2:
            # TODO implement special case
            pass
        elif self.n_players == 3:
            # TODO implement special case
            pass
        elif 4 <= self.n_players <= 7:
            current_index = self.players.index(self.current_player)

            if current_index + 1 == self.n_players:
                self.state = GameStates.turns_call_character
                self.current_player = Player
            else:
                self.current_player = self.players[current_index + 1]
            pass
        else:
            # Something not right with n_players
            pass
