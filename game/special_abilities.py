from game import game_state_controller as gsc

game_state_controller = gsc.GameStateController

def steal():
    current_player = game_state_controller.current_player
    characters = game_state_controller.open_cards
