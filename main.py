import sys

from jduargs.parser import ArgumentParser
from typing import Any, Tuple

INPUT_SOURCE = "manual"


def command_line_arguments() -> Tuple[Any]:
    p = ArgumentParser(
        description="Example use of the argument parser.",
        epilog="Have fun !",
    )

    if INPUT_SOURCE.lower() == "yaml":
        p.from_yaml("options.yaml")
    elif INPUT_SOURCE.lower() == "json":
        p.from_json("options.json")
    else:
        p.add("file", "f", description="file name without extension")
        p.add("path", "p", required=False, description="path to database tree")
        p.add(
            "offset",
            "o",
            int,
            description="offset in pixel to apply to the strip image",
            choices=[10, 20],
        )
        p.add("flag", "d", bool)

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
