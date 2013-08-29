import requests


server = 'http://localhost:8000'
name = 'guest'


def init():
    global server, name
    address = raw_input('pls input the server\'s address: ')
    port = raw_input('pls input the server\'s port: ')
    server = ("http://%s:%s" %(address, port)) if address and port else server
    input_name = raw_input('pls input your name: ')
    name = input_name if input_name else name


def send_message(msg):
    requests.post(server, data={'name': name, 'msg': msg})


def send():
    msg = raw_input('msg: ')
    send_message(msg)
    send()


if __name__ == '__main__':
    init()
    send()
