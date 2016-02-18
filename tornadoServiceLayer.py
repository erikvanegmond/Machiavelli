from game import game_state_controller
import tornado.web
import tornado.websocket
import mimetypes
import os

mimetypes.init()
mimetypes.add_type("font/woff2", ".woff2")
mimetypes.add_type("font/woff", ".woff")
mimetypes.add_type("font/ttf", ".ttf")


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


class GSCHandler(tornado.web.RequestHandler):
    def initialize(self, state):
        self.state = state

    def get(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write({'state':{'test':'er'}})  # Game.execute(self.state))


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
        self.gsc = game_state_controller.GameStateController(4, game_name="My Game")
        self.gsc.add_player("Erik")
        self.gsc.add_player("Justin")
        self.gsc.add_player("Abigail")
        self.gsc.add_player("Sabrina")

        handlers = [
            (r"/", HTMLHandler, dict(file='site/main.html')),
            (r"/game/state", GSCHandler, dict(state='GET_STATE')),
            (r"/game/connect", WSHandler),
            (r"/static/(.*)", FileHandler)
        ]
        settings = {
            "debug": True
        }
        tornado.web.Application.__init__(self, handlers, **settings)
