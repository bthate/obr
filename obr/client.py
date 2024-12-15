# This file is placed in the Public Domain.
# pylint: disable=C,R,W0105,W0212,W0718


"client"


import queue


from .command import command
from .        import Reactor, launch


class Output:

    cache = {}

    def __init__(self):
        self.oqueue = queue.Queue()

    def dosay(self, channel, txt):
        raise NotImplementedError

    def oput(self, channel, txt):
        self.oqueue.put((channel, txt))

    def output(self):
        while True:
            (channel, txt) = self.oqueue.get()
            if channel is None and txt is None:
                self.oqueue.task_done()
                break
            self.dosay(channel, txt)
            self.oqueue.task_done()

    def start(self):
        launch(self.output)

    def stop(self):
        self.oqueue.put((None, None))

    def wait(self):
        self.oqueue.join()



class Client(Output, Reactor):

    def __init__(self):
        Output.__init__(self)
        Reactor.__init__(self)
        self.register("command", command)

    def display(self, evt):
        for txt in evt.result:
            self.raw(txt)

    def raw(self, txt):
        raise NotImplementedError
 
    def start(self):
        Output.start(self)
        Reactor.start(self)


def __dir__():
    return (
        'Client',
        'Output'
    )
