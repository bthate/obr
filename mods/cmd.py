# This file is placed in the Public Domain.
# pylint: disable=C,W0105,E0402


"commands"


from obr.object import keys
from obr import Commands


def cmd(event):
    event.reply(",".join(sorted(keys(Commands.cmds))))