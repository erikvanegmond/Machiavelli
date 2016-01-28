from collections import deque

from character import *
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

        self.chosen_characters = []
        # TODO Just default, maybe allow for creating your own deck with the expansion
        self.character_deck = [eval(char) for char in Character.characters]  # Character.characters[:]
        self.character_deck.sort(key=lambda x: x.character_number) # make sure they are sorted

    def add_player(self, player):
        if self.state is GameStates.start_game and len(self.players) < self.n_players:
            self.players.append(Player(player))
        else:
            raise IndexError("To many players")

    def get_player_order(self, order=None):
        if self.state == GameStates.rounds_pick_characters_prepare or order == 'players':
            player_order = deque(self.players)
            player_order.rotate(-self.players.index(self.king_player))
            return list(player_order)
        elif self.state == GameStates.turns_order_players or order == 'characters':
            player_order = []
            for c in self.character_deck:
                player = self.get_player_with_character(c)
                if player:
                    player_order.append(player)
            return player_order
        else:
            print("state",self.state)
            print("order",order)
            raise TypeError

    def get_player_with_character(self, check_character):
        for player in self.players:
            if player.character == check_character:
                return player

    def update_state(self):
        if self.state == GameStates.start_game:
            self.king_player = self.players[0]
            self.current_player = self.players[0]
            self.state = GameStates.rounds_pick_characters_prepare
        elif self.state == GameStates.rounds_pick_characters_prepare:
            # Remove characters from player and make all characters available again
            self.chosen_characters = []
            for player in self.players:
                if player.character == "King":
                    self.king_player = player
                player.character = Character

            self.player_order = self.get_player_order()
            self.state = GameStates.rounds_pick_characters
        elif self.state == GameStates.rounds_pick_characters:
            self.update_state_rounds_pick_characters()
        elif self.state == GameStates.turns_order_players:
            self.player_order = self.get_player_order()
            self.state = GameStates.turns_call_character
        elif self.state == GameStates.turns_call_character:
            print(self.player_order)
            if self.player_order:
                next_player = self.player_order[0]
                self.player_order.pop(0)
                self.current_player = next_player
                self.state = GameStates.turns_begin
            else:
                print("no more characters left")
        elif self.state == GameStates.turns_begin:
            self.state = GameStates.turns_income
        elif self.state == GameStates.turns_income:
            self.state = GameStates.turns_general
        elif self.state == GameStates.turns_general:
            self.state = GameStates.turns_end
        elif self.state == GameStates.turns_end:
            self.state = GameStates.turns_call_character

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
                self.state = GameStates.turns_order_players
                self.current_player = Player
            else:
                self.current_player = self.players[current_index + 1]
            pass
        else:
            # Something not right with n_players
            pass
