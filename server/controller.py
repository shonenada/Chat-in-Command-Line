import json

from tornado.web import RequestHandler, asynchronous

from message import MessageServer


msgsrv = MessageServer()


class HomeHandler(RequestHandler):
    @asynchronous
    def get(self):
        @msgsrv.listen
        def call(msg):
            msg = json.dumps({'msg': msg})
            try:
                self.finish(msg)
            except IOError:
                pass

    def post(self):
        name = self.get_argument('name')
        msg = self.get_argument('msg')
        msgsrv.add_message("%s say: %s" % (name, msg))

