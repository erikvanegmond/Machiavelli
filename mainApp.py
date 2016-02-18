import tornado.web

from game import game_state_controller


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("site/main.html")


class StaticFiles(tornado.web.RequestHandler):
    def get(self, uri):
        root_path = "site/static/"
        path = root_path + uri
        print("path: " + path)
        self.render(path)


class GameState(tornado.web.RequestHandler):
    """ Get requests to this method will respond in a json with the game state """

    def initialize(self, gsc):
        self.gsc = gsc

    def get(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        state = self.gsc.get_state()
        actions = self.gsc.get_actions()
        response = {}
        if len(state) > 0:
            response['state'] = state
        if len(actions) > 0:
            response['actions'] = actions
        self.write(response)


class GameReset(tornado.web.RequestHandler):
    """ Posting to this method will reset the game state """

    def initialize(self, gsc):
        self.gsc = gsc

    def post(self):
        self.gsc.reset()
        self.gsc.add_player("Erik")
        self.gsc.add_player("Justin")
        self.gsc.add_player("Abigail")
        self.gsc.add_player("Sabrina")

        self.write("Reset")  # TODO: Post reset action to game controller.


class GameTakeAction(tornado.web.RequestHandler):
    """ Posting to this method will resolve an action in the game state """

    def get(self):
        self.write("Action taken response")  # TODO: Post action taken to game controller.


class GameUpdate(tornado.web.RequestHandler):
    """ Posting to this method will resolve an action in the game state """

    def initialize(self, gsc):
        self.gsc = gsc

    def post(self):
        self.gsc.update_state()
        self.write("Update")  # TODO: Post update to game controller.


class Application(tornado.web.Application):
    def __init__(self):
        self.gsc = game_state_controller.GameStateController(4, game_name="My Game")
        self.gsc.add_player("Erik")
        self.gsc.add_player("Justin")
        self.gsc.add_player("Abigail")
        self.gsc.add_player("Sabrina")

        handlers = [
            (r"/", MainHandler),
            (r"/game/state", GameState, dict(gsc=self.gsc)),
            (r"/reset", GameReset, dict(gsc=self.gsc)),  # Technical alpha single game version only.
            (r"/game/action", GameTakeAction),
            (r"/game/update", GameUpdate, dict(gsc=self.gsc)),
            (r"/static/(.*)", StaticFiles)
        ]
        settings = {
            "debug": True
        }
        tornado.web.Application.__init__(self, handlers, **settings)
