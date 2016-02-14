import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class GameState(tornado.web.RequestHandler):
    """ Get requests to this method will respond in a json with the game state """
    def get(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        response = {'gameName': 'example'}
        self.write(response)


class GameReset(tornado.web.RequestHandler):
    """ Posting to this method will reset the game state """
    def post(self):
        self.write("Reset")


class GameTakeAction(tornado.web.RequestHandler):
    """ Posting to this method will resolve an action in the game state """
    def get(self):
        self.write("Action taken response")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/game/state", GameState),
            #(r"/game/actions", GameActions),
            (r"/reset", GameReset), #Technical alpha single game version only.
            (r"/game", GameTakeAction)
        ]
        settings = {
            "debug": True
        }
        tornado.web.Application.__init__(self, handlers, **settings)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/game", GameState)
    ])

if __name__ == "__main__":
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()