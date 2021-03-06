import json
import tornado.web
import mimetypes
import os

mimetypes.init()
mimetypes.add_type("font/woff2", ".woff2")
mimetypes.add_type("font/woff", ".woff")
mimetypes.add_type("font/ttf", ".ttf")

from game import game_state_controller


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("site/main.html")


class StaticFiles(tornado.web.RequestHandler):
    def get(self, uri):
        root_path = "site/static/"
        path = root_path + uri
        _, file_extension = os.path.splitext(path)
        try:
            with open(path, 'rb') as f:
                mime_type = mimetypes.types_map[file_extension]
                self.set_header("Content-Type", mime_type + '; charset="utf-8"')
                self.write(f.read())
        except (OSError, IOError, KeyError):
            self.clear()
            self.set_status(404)
            self.finish("<html><body>404!</body></html>")


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

    def initialize(self, gsc: game_state_controller.GameStateController):
        self.gsc = gsc

    def get(self):
        response = self.gsc.take_action("hi")
        self.write(response)  # TODO: Post action taken to game controller.

    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))
        response = self.gsc.take_action(data)
        self.write(response)  # TODO: Post action taken to game controller.

    def parse_data_string(self, string):
        l = string.split("&")
        result = {}
        for i in l:
            s = i.split("=")
            result[s[0]] = s[1]
        return result


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
            (r"/game/action", GameTakeAction, dict(gsc=self.gsc)),
            (r"/game/update", GameUpdate, dict(gsc=self.gsc)),
            (r"/static/(.*)", StaticFiles)
        ]
        settings = {
            "debug": True
        }
        tornado.web.Application.__init__(self, handlers, **settings)
