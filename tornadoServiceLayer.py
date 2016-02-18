from game import game_state_controller
import tornado.web
import tornado.websocket
import mimetypes
import os
import json

mimetypes.init()
mimetypes.add_type("font/woff2", ".woff2")
mimetypes.add_type("font/woff", ".woff")
mimetypes.add_type("font/ttf", ".ttf")

gsc = game_state_controller.GameStateController(4, game_name="My Game")


class HTMLHandler(tornado.web.RequestHandler):
    def initialize(self, file):
        self.fileName = file

    def get(self):
        self.render(self.fileName)


class FileHandler(tornado.web.RequestHandler):
    def get(self, uri):
        root_path = "site/static/"
        path = root_path + uri
        _, file_extension = os.path.splitext(path)
        try:
            with open(path, 'rb') as f:
                type = mimetypes.types_map[file_extension]
                self.set_header("Content-Type", type + '; charset="utf-8"')
                self.write(f.read())
        except (EnvironmentError, KeyError):
            self.clear()
            self.set_status(404)
            self.finish("<html><body>MEEH</body></html>")


class GSCGetHandler(tornado.web.RequestHandler):
    def initialize(self, state):
        self.state = state

    def get(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        method = getattr(gsc, self.state)
        result = method()
        self.write(result)  # Game.execute(self.state))


class GSCPostHandler(tornado.web.RequestHandler):
    def initialize(self, state):
        self.state = state

    def post(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        method = getattr(gsc, self.state)
        result = method()
        self.write("Done")


class GSCPostArgHandler(tornado.web.RequestHandler):
    def initialize(self, state):
        self.state = state

    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))
        method = getattr(gsc, self.state)
        result = method(data)
        self.write("Done")


class WSHandler(tornado.websocket.WebSocketHandler):
    clients = []

    def open(self):
        self.clients.append(self)
        print('new connection')
        self.write_message("Hello World")

    def on_message(self, message):
        print('message received %s' % message)

    def on_close(self):
        self.clients.remove(self)
        print('closed connection')


class Application(tornado.web.Application):
    def __init__(self):
        gsc.add_player("Erik")
        gsc.add_player("Justin")
        gsc.add_player("Abigail")
        gsc.add_player("Sabrina")

        handlers = [
            (r"/", HTMLHandler, dict(file='site/main.html')),
            (r"/game/state", GSCGetHandler, dict(state='get_state')),
            (r"/game/update", GSCPostHandler, dict(state='update_state')),
            (r"/reset", GSCPostHandler, dict(state='reset')),
            (r"/game/action", GSCPostArgHandler, dict(state='take_action')),
            (r"/game/connect", WSHandler),
            (r"/static/(.*)", FileHandler)
        ]
        settings = {
            "debug": True
        }
        tornado.web.Application.__init__(self, handlers, **settings)
