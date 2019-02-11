from greetingEnum import greetingenum
from chain import Chain

if __name__ == '__main__':

    # Inicialization of the chain

    chain = Chain()

    # Set of some examples

    chain.set_chain(greetingenum.BuenosDias)
    chain.set_chain(greetingenum.GoodMorning)
    chain.set_chain(greetingenum.BomDia)
    chain.set_chain(greetingenum.Boungiorno)
    chain.set_chain(greetingenum.Ohayo)

    # The next one doesnt belong to any module

    chain.set_chain(greetingenum.GutenMorgen)
