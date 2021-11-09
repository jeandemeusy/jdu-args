import sys
from jduargs.parser import ArgumentParser
from typing import Tuple

INPUT_SOURCE = "manual"


def command_line_arguments() -> Tuple:
    p = ArgumentParser(
        description="Example use of the argument parser.",
        epilog="Have fun !",
    )

    p.owner("Jean Demeusy", "jean.demeusy@heig-vd.ch", version="0.2")

    if INPUT_SOURCE.lower() == "yaml":
        p.from_yaml("options.yaml")
    elif INPUT_SOURCE.lower() == "json":
        p.from_json("options.json")
    else:
        p.add("file", "f", description="file name without extension")
        p.add("path", "p", required=False, description="path to database tree")
        p.add("offset", "o", int, choices=[10, 20])
        p.add("flag", "d", bool)
        p.add("bias", "b", float, multiple=True, choices=[10, 20, 30])

    results = p.compile(sys.argv[1:])

    file = results["file"]
    path = results["path"]
    offset = results["offset"]
    flag = results["flag"]
    bias = results["bias"]

    return file, path, offset, flag, bias


if __name__ == "__main__":
    file, path, offset, flag, bias = command_line_arguments()

    print(f"{file=}")
    print(f"{path=}")
    print(f"{offset=}")
    print(f"{flag=}")
    print(f"{bias=}")
