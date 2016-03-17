class GameStateController:
    ACTIONS = {'pickcharacter': 'get_state'}
    CONSTS = {'SUCCESS': 'success',
              'FAILURE': 'failure'}

    def __init__(self):
        pass

    def get_state(self, gameid, user):
        return {'status': self.CONSTS['SUCCESS'], 'data': {'gameid': gameid, 'user': user}}

    def preform_action(self, data):
        action = data.action
        print(action)
        if action not in d:
            return {status: CONSTS['FAILURE'], reason: 'Action not allowed'}
        return getattr(self, ACTIONS[action])
