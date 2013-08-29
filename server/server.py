from tornado.web import Application
import tornado.ioloop

import settings
from controller import HomeHandler


app = Application([
    (r'/', HomeHandler),
], **settings.settings)


if __name__ == '__main__':
    app.listen(settings.port)
    print ("Starting server at %s" % settings.port)
    tornado.ioloop.IOLoop.instance().start()
