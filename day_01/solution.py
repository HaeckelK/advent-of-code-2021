import argparse
import os
from typing import Dict, Any, List, Tuple


def load_file(part: int, source: str) -> List[int]:
    filename = os.path.join("data", f"{source}_{part}.txt")
    with open(filename, "r") as f:
        return [int(x) for x in f.read().splitlines()]


def get_movement_counts(data: List[int]) -> Tuple[int, int]:
    increase_count = 0
    decrease_count = 0
    prior = data[0]
    for num in data[1:]:
        if num > prior:
            increase_count += 1
        elif num < prior:
            decrease_count += 1
        
        prior = num
    return increase_count, decrease_count


def get_windowed(data: List[int], interval: int) -> List[int]:
    windowed = []
    for i in range(0, len(data) - interval + 1):
        windowed.append(sum(data[i:i+interval]))
    return windowed


def main(part: int, source: str) -> None:
    if part == 1 and source == "sample":
        data = load_file(part, source)
        increase_count, _ = get_movement_counts(data)
        result = increase_count
        print(increase_count)
        assert result == 7
    elif part == 1 and source == "actual":
        data = load_file(part, source)
        increase_count, _ = get_movement_counts(data)
        print(increase_count)
    elif part == 2 and source == "sample":
        data = load_file(1, source)
        windowed = get_windowed(data, 3)
        increase_count, _ = get_movement_counts(windowed)
        result = increase_count
        print(increase_count)
        assert result == 5
    elif part == 2 and source == "actual":
        data = load_file(1, source)
        increase_count, _ = get_movement_counts(get_windowed(data, 3))
        result = increase_count
        print(increase_count)

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
