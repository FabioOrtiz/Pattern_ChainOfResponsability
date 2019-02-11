import abc

class Handler(object):
    def __init__(self):
        self.nextHandler = None

    @abc.abstractmethod
    def handle(self, request):
        pass

    def next_handle(self, handler):
        self.nextHandler = handler