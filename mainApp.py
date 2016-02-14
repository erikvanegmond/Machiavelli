import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html")


class GameState(tornado.web.RequestHandler):
    """ Get requests to this method will respond in a json with the game state """

    def get(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        response = {'gameName': 'exdample'}  # TODO: Get the response from game controller.
        self.write(response)


class GameReset(tornado.web.RequestHandler):
    """ Posting to this method will reset the game state """

    def post(self):
        self.write("Reset")  # TODO: Post reset action to game controller.


class GameTakeAction(tornado.web.RequestHandler):
    """ Posting to this method will resolve an action in the game state """

    def get(self):
        self.write("Action taken response")  # TODO: Post action taken to game controller.


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/game/state", GameState),
            (r"/reset", GameReset),  # Technical alpha single game version only.
            (r"/game", GameTakeAction)
        ]
        settings = {
            "debug": True
        }
        tornado.web.Application.__init__(self, handlers, **settings)