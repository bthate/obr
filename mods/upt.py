# This file is placed in the Public Domain.


"uptime"


import time


from obr.runtime import STARTTIME
from obr.utility import elapsed


def upt(event):
    event.reply(elapsed(time.time()-STARTTIME))
