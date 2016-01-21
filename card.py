class Card:
    def __init__(self, name, cost, color, worth=None, special_ability=None, description=None):
        """

        :param name: Name of the card
        :param cost: Cost of the card
        :param color: The color of the card, which character benefits
        :param worth:The worth of the card at the end of the game
        :param special_ability: The special ability of the card, if any
        """
        self.name = name
        self.cost = cost
        if worth:
            self.worth = worth
        else:
            self.worth = cost
        self.color = color
        self.special_ability = special_ability
        self.description = description

    def __repr__(self):
        string = "%s (%d)" % (self.name, self.cost)
        return string

    def get_dict(self):
        return {'name': self.name, 'cost': self.cost, 'worth': self.worth, 'color': self.color,
                'special_ability': self.special_ability, 'description': self.description}
