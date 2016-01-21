from enum import Enum


class GameStates(Enum):
    start_game = 0
    rounds_pick_characters = 1
    turns_begin = 2
    turns_income = 3
    turns_general = 4
    turns_end = 5

    def next(self):
        if self == self.start_game:
            return self.rounds_pick_characters
        elif self == self.rounds_pick_characters:
            return self.turns_begin
        elif self == self.turns_begin:
            return self.turns_income
        elif self == self.turns_income:
            return self.turns_general
        elif self == self.turns_general:
            return self.turns_end
        elif self == self.turns_end:
            return self.rounds_pick_characters




