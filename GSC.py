class GameStateController:
    FUNCTIONS = {'GET_STATE': 'getState'}
    CONSTS = {'SUCSES': 'sucses',
              'FAILURE': 'failure'}

    def getState(self):
        return 'GET Game State'

    def execute(self, state):
        method = getattr(self, self.FUNCTIONS[state])
        result = method()
        return result
