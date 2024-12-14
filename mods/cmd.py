# This file is placed in the Public Domain.
# pylint: disable=C,W0105,E0402


"commands"


from obr.command import Commands
from obr.object import keys


def cmd(event):
    event.reply(",".join(sorted(keys(Commands.cmds))))
