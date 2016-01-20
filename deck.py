import random
import json
from card import Card





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
        deck_file = 'start_deck.json'
        with open(deck_file) as f:
            deck_list = json.load(f)
            for card in deck_list:
                self.deck.append(Card(card['name'], card['cost'], card['color'], card['worth'], card['special']))
        random.shuffle(self.deck)
        # self.deck.reverse()
deck = Deck()
