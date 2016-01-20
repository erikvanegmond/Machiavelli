class Character:
    characters = ['Assassin',
                  'Thief',
                  'Magician',
                  'King',
                  'Bishop',
                  'Merchant',
                  'Architect',
                  'Warlord']

    def __init__(self, character):
        if character in self.characters:
            self.character = character
        else:
            raise NameError
        pass

    def __repr__(self):
        return self.character

    def get_color(self):
        if self.character == 'Assassin':
            return 'grey'
        elif self.character == 'Thief':
            return 'grey'
        elif self.character == 'Magician':
            return 'grey'
        elif self.character == 'King':
            return 'yellow'
        elif self.character == 'Bishop':
            return 'blue'
        elif self.character == 'Merchant':
            return 'green'
        elif self.character == 'Architect':
            return 'grey'
        elif self.character == 'Warlord':
            return 'red'

    def special_ability(self, player):
        if self.character == 'Assassin':
            print("Kills another character (not implemented yet)")
        elif self.character == 'Thief':
            print("Steals from another character (not implemented yet)")
        elif self.character == 'Magician':
            print("Swaps cards (not implemented yet)")
        elif self.character == 'King':
            print(" (not implemented yet)")
        elif self.character == 'Bishop':
            print("protected against Warlord (not implemented yet)")
        elif self.character == 'Merchant':
            player.gold += 1
        elif self.character == 'Architect':
            player.draw_cards(2)
        elif self.character == 'Warlord':
            print("may destroy a building (not implemented yet)")
