from greetingEnum import greetingenum
from chain import Chain

if __name__ == '__main__':
    #chain = set_chain(GreetingEnum.GutenVag)
    chain = Chain()

    chain.set_chain(greetingenum.BuenosDias)
    chain.set_chain(greetingenum.GoodMorning)
    chain.set_chain(greetingenum.BomDia)
    chain.set_chain(greetingenum.Boungiorno)
    chain.set_chain(greetingenum.Ohayo)