from game.character import *
from game.game_states import *
from game.player import Player
from game.utils import *

from game.deck import deck


class Game:
    def __init__(self, n_players):
        self.players = []
        self.state = GameStates.start_game
        self.n_players = n_players
        self.current_player = 0
        self.possible_characters = []

    def run(self):
        print(self.state)
        player = Player
        if not self.state is GameStates.start_game:
            player = self.players[self.current_player]
            player.print_status()

        if self.state == GameStates.start_game:
            # add players
            for i in range(self.n_players):
                player_name = "player %d" % i
                self.players.append(Player(name=player_name))
            self.state = self.state.next()
            self.possible_characters = Character.characters[:]
        elif self.state == GameStates.rounds_pick_characters:
            self.character_stage(player, self.possible_characters)
            self.current_player = (self.current_player + 1) % self.n_players
            if not self.current_player:
                self.state = self.state.next()
        elif self.state == GameStates.turns_begin:
            self.state = self.state.next()
        elif self.state == GameStates.turns_income:
            self.income_stage(player)
            self.state = self.state.next()
        elif self.state == GameStates.turns_general:
            print(player.get_turn_options())
            self.state = self.state.next()
        elif self.state == GameStates.turns_end:
            self.current_player = (self.current_player + 1) % self.n_players
            if not self.current_player:
                for player in self.players:
                    player.character = None
                self.possible_characters = Character.characters[:]
                self.state = GameStates.rounds_pick_characters
            else:
                self.state = GameStates.turns_begin

        else:
            print("Unknown state")

    def character_stage(self, player, possible_characters):
        question, possibilities = generate_question(possible_characters)
        while True:
            choice = input(question)
            try:
                choice = int(choice)
                if choice in possibilities:
                    char = possible_characters[choice]
                    possible_characters.remove(char)
                    player.character = eval(char)(player)
                    break
            except TypeError as e:
                print("Error!", e)
                continue

    def income_stage(self, player):
        while True:
            choice = input("income (press 1), cards (press 2)? ")
            if choice == '1':
                player.gold += 2
                print("gold", player.gold)
                break
            elif choice == '2':
                self.income_stage_pick_card(player)
                break
            else:
                print("did not understand")

    def income_stage_pick_card(self, player):
        card1 = deck.draw_card()
        card2 = deck.draw_card()
        while True:
            card_choice = input("%s (press 1) or %s (press 2)" % (card1, card2))
            if card_choice == '1':
                player.hand.append(card1)
                deck.trash.append(card2)
                break
            elif card_choice == '2':
                player.hand.append(card2)
                deck.trash.append(card1)
                break
            else:
                print("did not understand")
        print(player.hand)


    def build_stage(self, player):
        question, possibilities = generate_question(player.hand)
        while True:
            choice = input(question)
            try:
                choice = int(choice)
                if choice in possibilities:
                    if player.build(choice):
                        break
            except TypeError:
                continue
