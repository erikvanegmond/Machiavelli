import tornado.ioloop
import tornado.web
import json
import GSC

PORT = 8080

gsc = GSC.GameStateController()


class HTMLHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('site/main.html')


class GSCPostHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            print(data)
        except json.JSONDecodeError:
            self.set_status(422)
            self.write("Invalid JSON data")
        else:
            result = gsc.preform_action(data)
            self.set_header("Content-Type", "application/json; charset=UTF-8")
            self.write(result)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HTMLHandler),
            (r"/game/action", GSCPostHandler)
        ]
        settings = {
            "debug": True
        }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    app = Application()
    app.listen(PORT)
    print("Server running on http://localhost:{0}".format(PORT))
    tornado.ioloop.IOLoop.current().start()
