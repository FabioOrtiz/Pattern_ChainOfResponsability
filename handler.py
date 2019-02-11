import abc

# The abstract class for each handler


class Handler(object):

    def __init__(self):
        self.nextHandler = None

    @abc.abstractmethod
    def handle(self, request):
        pass

    # The method of assign the following handler

    def next_handle(self, handler):
        self.nextHandler = handler
