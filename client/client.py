import json
import time
from threading import Thread

import requests


server = 'http://localhost:8000'
name = 'guest'


def get_message():
    r = requests.get(server, timeout=3600*24)
    try:
        result = json.loads(r.text)
        print ("%s%s" %("--> ", result['msg']))
    except:
        pass
    finally:
        get_message()


def send_message(msg):
    requests.post(server, data={'name': name, 'msg': msg})


def send():
    msg = raw_input('say: ',)
    send_message(msg)
    send()


def init():
    global server, name
    address = raw_input('pls input the server\'s address: ')
    port = raw_input('pls input the server\'s port: ')
    server = ("http://%s:%s" %(address, port)) if address and port else server
    input_name = raw_input('pls input your name: ')
    name = input_name if input_name else name


class Operator(Thread):

    def __init__(self, func):
        Thread.__init__(self)
        self.isrunning = True
        self.callback = func

    def run(self):
        while self.isrunning:
            self.callback()

    def stop(self):
        self.isrunning = False


def main():
    init()
    reciever = Operator(get_message)
    reciever.start()
    sender = Operator(send)
    sender.start()


if __name__ == "__main__":
    main()
