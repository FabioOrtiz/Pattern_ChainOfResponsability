import handler
from greetingEnum import greetingenum

# This package is composed of every language than is used


class EnglishHandler(handler.Handler):

    # The comprobation of the Enum

    def handle(self, request):
        if request is greetingenum.GoodMorning:
            print("Hi! How are you?")
        else:
            if self.nextHandler is not None:
                self.nextHandler.handle(request)


class ItalianHandler(handler.Handler):
    def handle(self, request):
        if request is greetingenum.Boungiorno:
            print("Ciao! ¿Come stai?")
        else:
            if self.nextHandler is not None:
                self.nextHandler.handle(request)


class JapaneseHandler(handler.Handler):
    def handle(self, request):
        if request is greetingenum.Ohayo:
            print("Konichiwa! Ogenkidesuka?")
        else:
            if self.nextHandler is not None:
                self.nextHandler.handle(request)


class PortugueseHandler(handler.Handler):
    def handle(self, request):
        if request is greetingenum.BomDia:
            print("Ola! ¿Como Vai?")
        else:
            if self.nextHandler is not None:
                self.nextHandler.handle(request)


class SpanishHandler(handler.Handler):
    def handle(self, request):
        if request is greetingenum.BuenosDias:
            print("Hola! ¿Como estas?")
        else:
            if self.nextHandler is not None:
                self.nextHandler.handle(request)


# This is the last handler, the last one of the chain

class ErrorHandler(handler.Handler):
    def handle(self, request):
        print("The Language was not found")
