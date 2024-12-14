# This file is placed in the Public Domain.
# pylint: disable=C,R,W0105,W0212,W0718


"client"


from .command import command
from .reactor import Reactor


class Client(Reactor):

    def __init__(self):
        Reactor.__init__(self)
        self.register("command", command)

    def display(self, evt):
        for txt in evt.result:
            self.raw(txt)

    def raw(self, txt):
        raise NotImplementedError


def __dir__():
    return (
        'Client',
    )
