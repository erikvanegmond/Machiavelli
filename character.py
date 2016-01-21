class Character:
    characters = ['Assassin',
                  'Thief',
                  'Magician',
                  'King',
                  'Bishop',
                  'Merchant',
                  'Architect',
                  'Warlord']

    def __init__(self, character, player):
        if character in self.characters:
            self.character = character
        else:
            raise NameError
        self.player = player

    def __repr__(self):
        return self.character

    def get_color(self):
        return "grey"

    def special_ability(self):
        pass


class Assassin(Character):
    def __init__(self, player):
        self.player = player

    def special_ability(self):
        """
        Should be able to kill another character
        :return:
        """
        pass

    def __repr__(self):
        return "Assassin"


class Thief(Character):
    def __init__(self, player):
        self.player = player

    def special_ability(self):
        """
        Should be able to steal from another character
        :return:
        """
        pass

    def __repr__(self):
        return "Thief"


class Magician(Character):
    def __init__(self, player):
        self.player = player

    def special_ability(self):
        """
        Should be able to swap cards with another character
        :return:
        """
        pass

    def __repr__(self):
        return "Magician"


class King(Character):
    def __init__(self, player):
        self.player = player

    def special_ability(self):
        """
        Is starting player the next turn
        :return:
        """
        pass

    def get_color(self):
        return "yellow"

    def __repr__(self):
        return "King"


class Bishop(Character):
    def __init__(self, player):
        self.player = player

    def special_ability(self):
        """
        protected against condottiere
        :return:
        """
        pass

    def get_color(self):
        return "blue"

    def __repr__(self):
        return "Bishop"


class Merchant(Character):
    def __init__(self, player):
        self.player = player

    def special_ability(self):
        print("got gold")
        self.player.gold += 1

    def get_color(self):
        return "green"

    def __repr__(self):
        return "Merchant"


class Architect(Character):
    def __init__(self, player):
        self.player = player

    def special_ability(self):
        """
        Recieves two building cards
        :return:
        """
        self.player.draw_cards(2)

    def __repr__(self):
        return "Architect"


class Warlord(Character):
    def __init__(self, player):
        self.player = player

    def special_ability(self):
        """
        Can destroy a building from another player
        :return:
        """

    def get_color(self):
        return "red"

    def __repr__(self):
        return "Warlord"

