# This file is placed in the Public Domain.


"timers"


import threading
import time


from .threads import launch


class Timer:

    def __init__(self, sleep, func, *args, thrname=None, **kwargs):
        self.args   = args
        self.func   = func
        self.kwargs = kwargs
        self.sleep  = sleep
        self.name   = thrname or kwargs.get("name", name(func))
        self.state  = {}
        self.timer  = None

    def run(self) -> None:
        self.state["latest"] = time.time()
        launch(self.func, *self.args)

    def start(self) -> None:
        timer = threading.Timer(self.sleep, self.run)
        timer.name   = self.name
        timer.sleep  = self.sleep
        timer.state  = self.state
        timer.func   = self.func
        timer.state["starttime"] = time.time()
        timer.state["latest"]    = time.time()
        timer.start()
        self.timer   = timer

    def stop(self) -> None:
        if self.timer:
            self.timer.cancel()


class Repeater(Timer):

    def run(self) -> None:
        launch(self.start)
        super().run()


def __dir__():
    return (
        'Repeater',
        'Timer'
    )
