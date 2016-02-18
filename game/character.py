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

    def __eq__(self, other):
        """
        Characters are the same if they are the same character, as there is only one of each character
        """
        if type(self) == type(other):
            return True
        return False

    def get_color(self):
        return "grey"

    def special_abilities(self):
        pass


class Assassin(Character):
    character_number = 1
    character = "Assassin"

    def __init__(self, player):
        self.player = player

    def special_abilities(self):
        """
        Should be able to kill another character
        :return:
        """
        pass


class Thief(Character):
    character_number = 2
    character = "Thief"

    def __init__(self, player):
        self.player = player

    def special_abilities(self):
        """
        Should be able to steal from another character
        :return:
        """
        return ['steal']

    def __repr__(self):
        return "Thief"


class Magician(Character):
    character_number = 3
    character = "Magician"

    def __init__(self, player):
        self.player = player

    def special_abilities(self):
        """
        Should be able to swap cards with another character
        :return:
        """
        pass

    def __repr__(self):
        return "Magician"


class King(Character):
    character_number = 4
    character = "King"

    def __init__(self, player):
        self.player = player

    def special_abilities(self):
        """
        Is starting player the next turn
        :return:
        """
        pass

    def get_color(self):
        return "yellow"


class Bishop(Character):
    character_number = 5
    character = "Bishop"

    def __init__(self, player):
        self.player = player

    def special_abilities(self):
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
    character_number = 6
    character = "Merchant"

    def __init__(self, player):
        self.player = player

    def special_abilities(self):
        print("got gold")
        self.player.gold += 1

    def get_color(self):
        return "green"

    def __repr__(self):
        return "Merchant"


class Architect(Character):
    character_number = 7
    character = "Architect"

    def __init__(self, player):
        self.player = player

    def special_abilities(self):
        """
        Recieves two building cards
        :return:
        """
        self.player.draw_cards(2)

    def __repr__(self):
        return "Architect"


class Warlord(Character):
    character_number = 8
    character = "Warlord"

    def __init__(self, player):
        self.player = player

    def special_abilities(self):
        """
        Can destroy a building from another player
        :return:
        """

    def get_color(self):
        return "red"

    def __repr__(self):
        return "Warlord"
