import sys

from jduargs.parser import ArgumentParser
from typing import Any, Tuple


def command_line_arguments() -> Tuple[Any]:
    p = ArgumentParser(
        description="Example use of the argument parser.",
        epilog="Have fun !",
    )

    p.from_json("options.json")

    p.compile(sys.argv[1:])

    file = p["file"]
    path = p["path"]
    offset = p["offset"]

    return file, path, offset


if __name__ == "__main__":
    file, path, offset = command_line_arguments()

    print(f"{file=}")
    print(f"{path=}")
    print(f"{offset=}")
