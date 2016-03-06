class GameStateController:
    ACTIONS = {'pickcharacter': 'get_state'}
    CONSTS = {'SUCCESS': 'success',
              'FAILURE': 'failure'}

    def get_state(self):
        return {status: CONSTS['SUCCESS'], data: {state: 'something'}}

    def preform_action(self, data):
        action = data.action
        print(action)
        if action not in d:
            return {status: CONSTS['FAILURE'], reason: 'Action not allowed'}
        return getattr(self, ACTIONS[action])
