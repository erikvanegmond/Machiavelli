from game import character

from game.deck import *


class Player:
    def __init__(self, name=""):
        self.gold = 2
        self.hand = []
        self.city = []
        self.character = character.Character
        self.name = name

        self.draw_cards(4)

    def draw_cards(self, number_of_cards):
        for _ in range(number_of_cards):
            self.draw_card()

    def draw_card(self):
        self.hand.append(deck.draw_card())

    def build(self, hand_index):
        card = self.hand[hand_index]
        if card.cost <= self.gold:
            self.gold -= card.cost
            self.hand.remove(card)
            self.city.append(card)
            return True
        print("Can not build %s" % card)
        return False

    def get_general_income(self):
        color = self.character.get_color()
        for building in self.city:
            if building.color == color:
                self.gold += 1

    def get_turn_options(self):
        options = []
        if self.hand:
            options.append("build")
        special = self.character.special_abilities()
        if special:
            options += special
        return options

    def print_status(self):
        print("  name:", self.name)
        print("  character:", self.character)
        print("  hand:", self.hand)
        print("  city:", self.city)
        print("  gold", self.gold)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if hasattr(self, 'name') and hasattr(other, 'name'):
            return self.name == other.name
        elif not hasattr(self, 'name') and not hasattr(other, 'name'):
            return False
        else:
            return False