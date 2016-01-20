from deck import *


class Player:
    def __init__(self):
        self.gold = 2
        self.hand = []
        self.city = []
        self.character = ""

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

    def print_status(self):
        print("hand:", self.hand)
        print("city:", self.city)
        print("gold", self.gold)
