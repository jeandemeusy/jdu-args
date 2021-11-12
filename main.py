import sys
from jduargs.parser import ArgumentParser
from typing import Tuple


def handle_args(path: str = "") -> Tuple:
    if path:
        p = ArgumentParser()
        p.from_file(path)
    else:
        p = ArgumentParser(
            description="Example use of the argument parser.",
            epilog="Have fun !",
        )
        p.owner("Jean Demeusy <jean.demeusy@heig-vd.ch>", "0.2")

        p.add("path", "p", required=False, description="path to database tree")
        p.add("flag", "f", bool)
        p.add("bias", "b", float, multiple=True, choices=[10, 20, 30])

    return p.compile(sys.argv[1:])


if __name__ == "__main__":
    results = handle_args("options.json")

    print(f"{results=}")
