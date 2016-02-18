import tornado.ioloop
import tornadoServiceLayer

PORT = 8888

if __name__ == "__main__":
    app = tornadoServiceLayer.Application()
    app.listen(PORT)
    print("Server running on http://localhost:{0}".format(PORT))
    tornado.ioloop.IOLoop.current().start()
