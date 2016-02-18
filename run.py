import tornado.ioloop
import mainApp

PORT = 8888

if __name__ == "__main__":
    app = mainApp.Application()
    app.listen(PORT)
    print("Server running on http://localhost:{0}".format(PORT))
    tornado.ioloop.IOLoop.current().start()
