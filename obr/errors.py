# This file is placed in the Public Domain.


"errors"


import traceback


class Errors:

    name = __file__.rsplit(".", maxsplit=2)[-2]
    errors = []

    @staticmethod
    def format(exc) -> str:
        exctype, excvalue, trb = type(exc), exc, exc.__traceback__
        trace = traceback.extract_tb(trb)
        result = ""
        for i in trace:
            fname = i[0]
            if not Errors.name in fname:
                continue
            linenr = i[1]
            plugfile = fname[:-3].split("/")
            mod = []
            for i in plugfile[::-1]:
                mod.append(i)
                if Errors.name == i:
                    break
            ownname = '.'.join(mod[::-1])
            result += f"{ownname}:{linenr} "
        del trace
        res = f"{exctype} {result[:-1]} {excvalue}"
        return res

    @staticmethod
    def full(exc) -> str:
        return traceback.format_exception(
            type(exc),
            exc,
            exc.__traceback__
        )


def errors() -> []:
    return Errors.errors


def later(exc) -> None:
    excp = exc.with_traceback(exc.__traceback__)
    fmt = Errors.format(excp)
    if fmt not in Errors.errors:
        Errors.errors.append(fmt)


def __dir__():
    return (
        "Errors",
        "errors",
        "later"
    )
