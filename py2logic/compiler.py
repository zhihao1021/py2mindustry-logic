import __main__
from os import urandom
from os.path import basename, splitext
from typing import Optional

from .swap import result


def compile(filename: Optional[str] = None):
    if filename is None:
        try:
            filename = splitext(basename(__main__.__file__))[0] + ".mlog"
        except ModuleNotFoundError:
            filename = urandom(8).hex() + ".mlog"
        

    with open(filename, "w", encoding="utf-8") as output_file:
        output_file.write(result.dump())
    
    print("Successfully compile script into `" + filename + "`.")
