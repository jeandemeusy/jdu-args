import sys

from jduargs.parser import ArgumentParser
from typing import Any, Tuple


def command_line_arguments() -> Tuple[Any]:
    p = ArgumentParser(
        description="Example use of the argument parser.",
        epilog="Have fun !",
    )

    p.from_json("options.json")

    results = p.compile(sys.argv[1:])

    file = results["file"]
    path = results["path"]
    offset = results["offset"]
    flag = results["flag"]

    return file, path, offset, flag


if __name__ == "__main__":
    file, path, offset, flag = command_line_arguments()

    print(f"{file=}")
    print(f"{path=}")
    print(f"{offset=}")
    print(f"{flag=}")
