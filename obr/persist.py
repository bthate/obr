# This file is placed in the Public Domain.


"persistence"


import threading


from .caching import Cache
from .objects import Object, dumps, fqn, items, loads, update
from .workdir import Workdir, store


p    = os.path.join
lock = threading.RLock()


class DecodeError(Exception):

    pass


def cdir(pth):
    path = pathlib.Path(pth)
    path.parent.mkdir(parents=True, exist_ok=True)


def ident(obj):
    return p(fqn(obj),*str(datetime.datetime.now()).split())


def read(obj, pth):
    with lock:
        with open(pth, 'r', encoding='utf-8') as ofile:
            try:
                obj2 = loads(ofile.read())
                update(obj, obj2)
            except json.decoder.JSONDecodeError as ex:
                raise DecodeError(pth) from ex
    return pth


def write(obj, pth=None):
    with lock:
        if pth is None:
            pth = store(ident(obj))
        cdir(pth)
        txt = dumps(obj, indent=4)
        with open(pth, 'w', encoding='utf-8') as ofile:
            ofile.write(txt)
    return pth


def __dir__():
    return (
        'cdir',
        'ident',
        'read',
        'write'
    )
