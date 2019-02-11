from languages import EnglishHandler, SpanishHandler, JapaneseHandler, ItalianHandler, PortugueseHandler, ErrorHandler


class Chain:

    def set_chain(self, greetingenum):

        # Here i create every handler than i use

        english_handler = EnglishHandler()
        spanish_handler = SpanishHandler()
        portuguese_handler = PortugueseHandler()
        japanese_handler = JapaneseHandler()
        italian_handler = ItalianHandler()
        error_handler = ErrorHandler()

        # Assign the next one handler to each handler

        english_handler.next_handle(spanish_handler)
        spanish_handler.next_handle(portuguese_handler)
        portuguese_handler.next_handle(japanese_handler)
        japanese_handler.next_handle(italian_handler)

        # Italian is the last one of the chain, by that i assigned to Error Handler

        italian_handler.next_handle(error_handler)

        # This is the start of the responsibility chain

        english_handler.handle(greetingenum)
