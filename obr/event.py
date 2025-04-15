# This file is placed in the Public Domain.


"event"


import threading
import time


class Event:

    """ event """

    def __init__(self):
        self._ready = threading.Event()
        self._thr   = None
        self.ctime  = time.time()
        self.result = {}
        self.type   = "event"
        self.txt    = ""

    def __contains__(self, key):
        return key in dir(self)

    def __getattr__(self, key):
        return self.__dict__.get(key, "")

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

    def done(self) -> None:
        "event is done."
        self.reply("ok")

    def ready(self) -> None:
        "event is ready."
        self._ready.set()

    def reply(self, txt) -> None:
        "add text to result."
        self.result[time.time()] = txt

    def wait(self) -> None:
        "wait for result."
        self._ready.wait()
        if self._thr:
            self._thr.join()


def __dir__():
    return (
        'Event',
    )
