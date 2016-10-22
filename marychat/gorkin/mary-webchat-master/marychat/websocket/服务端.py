class MessageBuffer(object):
    def __init__(self, cache_size=200):
        self.cache = []
        self.cache_size = cache_size
        self.clients = []

    def new_message(self, msg):
        self.cache.append(msg)
        if len(self.cache) > self.cache_size:
            self.cache = self.cache[-self.cache_size:]

    def update_clients(self, msg):
        for client in self.clients:
            client.send(msg)