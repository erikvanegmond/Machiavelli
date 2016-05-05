from tornado import web
from tornado import ioloop
import pprint

# Configuration Handling.
# TODO Use ConfigParser to handle configurations.
PORT = 8080


class GameHandler(web.RequestHandler):
    def get(self, gameid):
        print(gameid)

    def post(self, gameid):
        print(gameid)


class FileHandler(web.StaticFileHandler):
    def initialize(self, path, default_filename=None, error_message="site/html/errors/defaultError.html"):
        self.root = path
        self.default_filename = default_filename
        self.error_message = error_message

    def write_error(self, status_code, **kwargs):
        self.write(self.error_message)


class NotFoundHandler(web.RequestHandler):
    def get(self):
        self.set_status(404)
        self.set_header("Content-Type", "text/plain")
        self.write("Not Found")


class Application(web.Application):
    def __init__(self):
        handlers = [
            # (r"/game/(.*)", GSCHandler),
            # (r"/()", FileHandler, {"path": "site/static/html/main.html"}),
            # (r"/login", LoginHandler),
            (r"/game/([a-z]+)", GameHandler),
            (r"/image/((?:[a-z]+\/)*[a-z0-9]+\.[a-z0-9]+)", FileHandler,
                {"path": "images", "error_message": "Image not found."}),
            (r".*", NotFoundHandler)
        ]
        settings = {
            "debug": True,
            "cookie_secret": "__TODO:_GENERATassd@#$@#($&!@KDF*YROIHE_YOUR_OWN_RANDOM_VALUE_HERE__",
            "login_url": "/login"
        }
        web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    app = Application()
    app.listen(PORT)
    print("Server running on http://localhost:{0}".format(PORT))
    ioloop.IOLoop.current().start()
