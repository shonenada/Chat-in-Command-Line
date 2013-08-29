import json

import requests


server = 'http://localhost:8000'


def init():
    global server
    address = raw_input('pls input the server\'s address: ')
    port = raw_input('pls input the server\'s port: ')
    server = ("http://%s:%s" %(address, port)) if address and port else server


def get_message():
    r = requests.get(server, timeout=3600*24)
    try:
        result = json.loads(r.text)
        print result['msg']
    except:
        pass
    finally:
        get_message()


def run():
    init()
    print "Now recieving the msg."
    get_message()


if __name__ == '__main__':
    run()
