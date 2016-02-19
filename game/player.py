from game import character

from game.deck import *


class Player:
    def __init__(self, name=""):
        self.gold = 2
        self.hand = []
        self.city = []
        self.temp_hand = []
        self.character = character.Character
        self.name = name
        self.has_build = False
        self.has_character_income = False

        self.draw_cards(4)

    def new_turn(self):
        self.has_build = False
        self.has_character_income = False


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
            self.has_build = True
            return True
        return "Can not build %s" % card

    def get_income_gold(self):
        self.gold += 2

    def get_income_card(self):
        cards = []
        for _ in range(2):
            cards.append(deck.draw_card())
        self.temp_hand = cards
        return [x.name for x in cards]

    def keep_income_card(self, card):
        self.hand.append(card)

    def get_character_income(self):
        color = self.character.get_color()
        for building in self.city:
            if building.color == color:
                self.gold += 1

    def get_turn_actions(self):
        actions = {}
        if self.hand and not self.has_build:
            actions["build"] = [x.name for x in self.hand]
        if self.character.get_color() is not 'grey' and not self.has_character_income:
            actions["character_income"] = ['yes']
        return actions

    def get_status(self):
        status = {"name": self.name, "hand": [x.__repr__() for x in self.hand],
                  "city": [x.__repr__() for x in self.city], "gold": self.gold}
        if isinstance(self.character, character.Character):
            status["character"] = self.character.character
        return status

    def print_status(self):
        print("  name:", self.name)
        print("  character:", self.character)
        print("  hand:", self.hand)
        print("  city:", self.city)
        print("  gold", self.gold)

    def __repr__(self):
        return self.name

    def __str__(self):
        if isinstance(self.character, character.Character):
            return "{} ({})".format(self.name, self.character.character)
        return self.name

    def __eq__(self, other):
        if hasattr(self, 'name') and hasattr(other, 'name'):
            return self.name == other.name
        elif not hasattr(self, 'name') and not hasattr(other, 'name'):
            return False
        else:
            return False
