from collections import deque

from game.game_states import *
from game.player import *

from game.character import *


class GameStateController:
    def __init__(self, n_players, game_name="Name"):
        self.game_name = game_name

        self.state = GameStates.start_game

        self.players = []
        self.player_order = []
        self.n_players = n_players
        self.current_player = Player
        self.king_player = Player

        self.number_of_open_cards = 0
        # TODO Fix for expansion
        if n_players == 4:
            self.number_of_open_cards = 2
        elif n_players == 5:
            self.number_of_open_cards = 1

        self.chosen_characters = []
        self.open_cards = []
        self.closed_cards = []
        # TODO Just default, maybe allow for creating your own deck with the expansion
        self.character_deck = [eval(char) for char in Character.characters]  # Character.characters[:]
        self.character_deck.sort(key=lambda x: x.character_number)  # make sure they are sorted

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
            print("state", self.state)
            print("order", order)
            raise TypeError

    def get_player_with_character(self, check_character):
        for player in self.players:
            if player.character == check_character:
                return player

    def take_open_cards(self):
        for _ in list(range(self.number_of_open_cards)):
            while True:
                card = random.choice(self.character_deck)
                if card == "King":
                    continue
                elif card in self.chosen_characters:
                    continue
                self.chosen_characters.append(card)
                break

    def update_state(self):
        if self.state == GameStates.start_game:
            self.king_player = self.players[0]
            self.current_player = self.players[0]
            self.state = GameStates.rounds_pick_characters_prepare
        elif self.state == GameStates.rounds_pick_characters_prepare:
            # Remove characters from players and table, and make all characters available again
            self.chosen_characters = []
            self.open_cards = []
            self.closed_cards = []
            for player in self.players:
                if player.character == "King":
                    self.king_player = player
                player.character = Character
            self.take_open_cards()
            self.player_order = self.get_player_order()
            self.state = GameStates.rounds_pick_characters
        elif self.state == GameStates.rounds_pick_characters:
            self.update_state_rounds_pick_characters()
        elif self.state == GameStates.turns_order_players:
            self.player_order = self.get_player_order()
            self.state = GameStates.turns_call_character
        elif self.state == GameStates.turns_call_character:
            if self.player_order:
                next_player = self.player_order[0]
                self.player_order.pop(0)
                self.current_player = next_player
                self.state = GameStates.turns_begin
            else:
                self.state = GameStates.rounds_pick_characters_prepare
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

    def get_possible_characters(self):
        possible = []
        for c in self.character_deck:
            if c not in self.open_cards and c not in self.chosen_characters and c not in self.closed_cards:
                possible.append(c)
        return possible

    def __str__(self):
        return "State:{}, current_player, {}".format(self.state, self.current_player)

    def __repr__(self):
        return "State:{}, current_player, {}".format(self.state, self.current_player)

    def reset(self):
        self.__init__(self.n_players, game_name=self.game_name)
        deck.read_deck()

    def get_state(self):
        state = {'game_name': self.game_name, 'n_players': self.n_players, 'open_cards': self.open_cards,
                 'n_open_cards': self.number_of_open_cards, 'closed_cards': len(self.closed_cards),
                 'game_state': self.state.name, 'players': [x.name for x in self.players]}
        if isinstance(self.current_player, Player):
            state['current_player'] = self.current_player.__str__()
        if isinstance(self.king_player, Player):
            state['king_player'] = self.king_player.__str__()

        return state

    def get_actions(self):
        actions = {}
        if isinstance(self.current_player, Player):
            if self.state == GameStates.rounds_pick_characters:
                actions['pick_character'] = [x.character for x in self.get_possible_characters()]
        return actions

    def take_action(self, action):

        return "action taken"
