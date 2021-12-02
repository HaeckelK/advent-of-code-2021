import argparse
import os
from typing import Dict, Any, List, Tuple


class Submarine:
    def __init__(self) -> None:
        self.depth = 0
        self.horizontal_pos = 0
        self.aim = 0
        return


def process_instructions_as_movment(sub: Submarine, instructions: List[Tuple[str, int]]) -> None:
    for instruction, amount in instructions:
        if instruction == "forward":
            sub.horizontal_pos += amount
        elif instruction == "up":
            sub.depth -= amount
        elif instruction == "down":
            sub.depth += amount
    return


def load_file(part: int, source: str) -> List[Tuple[str, int]]:
    filename = os.path.join("data", f"{source}_{part}.txt")
    with open(filename, "r") as f:
        return [tuple([x.split(" ")[0], int(x.split(" ")[1])]) for x in f.read().splitlines()]


def main(part: int, source: str) -> None:
    submarine = Submarine()
    instructions = load_file(part, source)

    process_func = process_instructions_as_movment

    process_func(submarine, instructions)

    result = submarine.horizontal_pos * submarine.depth
    print(result)

    if part == 1 and source == "sample":
        assert result == 150
    return


def cli() -> Dict[str, Any]:
    formatter_class = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=formatter_class)

    parser.add_argument("part", type=int, default=1)
    parser.add_argument("source", type=str, default="sample")

    args = parser.parse_args()

    return {"part": int(args.part),
            "source": args.source}


if __name__ == '__main__':
    args = cli()
    main(part=args["part"], source=args["source"])
