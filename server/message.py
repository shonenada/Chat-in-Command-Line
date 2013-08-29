class MessageServer(object):
    def __init__(self):
        self.observers = []
        self.messages = []

    def listen(self, callback):
        self.observers.append(callback)

    def add_message(self, message):
        try:
            self.messages.append(message)
            [call(message) for call in self.observers]
        finally:
           self.observers = []
