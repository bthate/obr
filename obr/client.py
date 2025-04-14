# This file is placed in the Public Domain.


"clients"


from .fleet   import Fleet
from .handler import Handler
from .object  import Default


class Client(Handler):

    def __init__(self):
        Handler.__init__(self)
        self.state = Default()
        Fleet.add(self)

    def announce(self, txt) -> None:
        pass

    def raw(self, txt) -> None:
        raise NotImplementedError("raw")

    def say(self, channel, txt) -> None:
        self.raw(txt)


def __dir__():
    return (
        'Client',
        'Default'
    )
