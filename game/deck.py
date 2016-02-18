import json
import random
import os

from game.card import Card


class Deck:
    deck = []
    trash = []

    def __init__(self):
        self.read_deck()
        # pass

    def __repr__(self):
        return ", ".join(self.deck)

    def draw_card(self):
        card = self.deck.pop()
        return card

    def read_deck(self):
        self.deck = []
        root_path = os.path.dirname(os.path.abspath(__file__))
        deck_file = 'start_deck.json'
        with open(root_path+"\\"+deck_file) as f:
            deck_list = json.load(f)
            for card in deck_list:
                self.deck.append(
                    Card(card['name'], card['cost'], card['color'], card['value'], card['special_ability']))
        random.shuffle(self.deck)


deck = Deck()



