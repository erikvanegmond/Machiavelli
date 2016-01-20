from player import Player
from deck import deck
from character import Character
from utils import *

class Game:
    players = []  # this means you can only play one game at the time, this variable is static (i think)

    def __init__(self, n_players):
        for _ in range(n_players):
            self.players.append(Player())

    def run(self):
        for _ in range(3):
            possible_characters = Character.characters[:]
            for i, player in enumerate(self.players):
                print("player", i)
                player.print_status()
                self.character_stage(player, possible_characters)
                player.get_general_income()
                player.print_status()
                self.income_stage(player)
                player.character.special_ability(player)
                player.print_status()
                self.build_stage(player)
                player.print_status()
                print()

    def character_stage(self, player, possible_characters):
        question = ""
        possibilities = range(len(possible_characters))
        for i, char in enumerate(possible_characters):
            question += char + "(press " + str(i) + ") "
        while True:
            choice = input(question)
            try:
                choice = int(choice)
                if choice in possibilities:
                    char = possible_characters[choice]
                    possible_characters.remove(char)
                    player.character = Character(char)
                    break
            except TypeError:
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
