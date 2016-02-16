import tornado.web
import game_state_controller


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html")


class GameState(tornado.web.RequestHandler):
    """ Get requests to this method will respond in a json with the game state """

    def initialize(self, gsc):
        self.gsc = gsc

    def get(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        response = self.gsc.get_state()
        self.write(response)


class GameReset(tornado.web.RequestHandler):
    """ Posting to this method will reset the game state """

    def post(self):
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
            (r"/reset", GameReset),  # Technical alpha single game version only.
            (r"/game/action", GameTakeAction),
            (r"/game/update", GameUpdate, dict(gsc=self.gsc))
        ]
        settings = {
            "debug": True
        }
        tornado.web.Application.__init__(self, handlers, **settings)
