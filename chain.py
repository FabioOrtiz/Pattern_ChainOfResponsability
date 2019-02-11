from languages import EnglishHandler, SpanishHandler, JapaneseHandler, ItalianHandler, PortugueseHandler, ErrorHandler


class Chain:

    def set_chain(self, greetingenum):
        english_handler = EnglishHandler()
        spanish_handler = SpanishHandler()
        portuguese_handler = PortugueseHandler()
        japanese_handler = JapaneseHandler()
        italian_handler = ItalianHandler()
        error_handler = ErrorHandler()

        english_handler.next_handle(spanish_handler)
        spanish_handler.next_handle(portuguese_handler)
        portuguese_handler.next_handle(japanese_handler)
        japanese_handler.next_handle(italian_handler)
        italian_handler.next_handle(error_handler)

        english_handler.handle(greetingenum)