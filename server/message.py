class MessageServer(object):
    def __init__(self):
        self.observers = []
        self.messages = []

    def listen(self, callback):
        self.observers.append(func)

    def add_message(self, message):
        try:
            self.messages.append(message)
            [call(messaeg) for call in self.observers]
        finally:
           self.observers = []

