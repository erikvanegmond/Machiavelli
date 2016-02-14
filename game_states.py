from enum import Enum


class AutoNumber(Enum):
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj


class GameStates(AutoNumber):
    start_game = ()
    rounds_pick_characters_prepare = ()
    rounds_pick_characters = ()
    turns_order_players = ()
    turns_call_character = ()
    turns_begin = ()
    turns_income = ()
    turns_general = ()
    turns_end = ()
    game_end = ()

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
