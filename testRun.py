import tornado.ioloop
import tornado.web
import tornado.escape
import json
import GSC

PORT = 8080

gsc = GSC.GameStateController()


class GSCHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

    def get(self, gameid):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        user = tornado.escape.xhtml_escape(self.current_user) if self.current_user else None
        result = gsc.get_state(gameid, user)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(result)

    def post(self, gameid):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
        except json.JSONDecodeError:
            self.set_status(422)
            self.write("Invalid JSON!")
        else:
            result = GSC.preform_action(data)
            self.set_header("Content-Type", "application/json; charset=UTF-8")
            self.write(result)

    def write_error(self, status_code, **kwargs):
        self.set_status(status_code)
        self.write("Something went wrong!")


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect("/")


class FileHandler(tornado.web.StaticFileHandler):
    def write_error(self, status_code, **kwargs):
        self.set_status(status_code)
        self.render("site/static/html/error/fileError.html", status=status_code)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/game/(.*)", GSCHandler),
            (r"/()", FileHandler, {"path": "site/static/html/main.html"}),
            (r"/login", LoginHandler),
            (r"/image/(.*)", FileHandler, {"path": "site/static/image/"}),
            (r"/(.*\.html)", FileHandler, {"path": "site/static/"}),
            (r"/(.*\.js)", FileHandler, {"path": "site/static/js/"}),
            (r"/(.*\.css)", FileHandler, {"path": "site/static/css/"}),
            (r"/static/(.*)", FileHandler, {"path": "site/static/"})
        ]
        settings = {
            "debug": True,
            "cookie_secret": "__TODO:_GENERATassd@#$@#($&!@KDF*YROIHE_YOUR_OWN_RANDOM_VALUE_HERE__",
            "login_url": "/login"
        }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    app = Application()
    app.listen(PORT)
    print("Server running on http://localhost:{0}".format(PORT))
    tornado.ioloop.IOLoop.current().start()
