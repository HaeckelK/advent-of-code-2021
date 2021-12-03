import argparse
import os
from typing import Dict, Any, List, Tuple


def load_file(part: int, source: str) -> List[str]:
    filename = os.path.join("data", f"{source}_{part}.txt")
    with open(filename, "r") as f:
        return f.read().splitlines()


def dummy(total: int, population: int) -> int:
    if total / population > 0.5:
        return '1'
    elif total / population < 0.5:
        return '0'
    else:
        assert 1 == 0


def most_common(nums: List[int]) -> int:
    count_0 = 0
    count_1 = 0
    for num in nums:
        if num == '1':
            count_1 += 1
        else:
            count_0 += 1

    if count_0 > count_1:
        return 0
    elif count_0 < count_1:
        return 1
    else:
        return 1


def least_common(nums: List[int]) -> int:
    count_0 = 0
    count_1 = 0
    for num in nums:
        if num == '1':
            count_1 += 1
        else:
            count_0 += 1

    if count_0 < count_1:
        return 0
    elif count_0 > count_1:
        return 1
    else:
        return 0


def main(part: int, source: str) -> None:
    data = load_file(1, source)
    if part == 1:

        totals = [0] * len(data[0])
        num = len(data)
        digits = len(data[0])
        for row in data:
            totals = [sum(x) for x in zip(totals, map(lambda x: int(x), row))]
        
        gamma_binary = "".join(map(lambda x: dummy(x, num), totals))
        gamma = int(gamma_binary, 2)
        epsilon = (2**digits - 1) - gamma

        print(gamma, epsilon, gamma * epsilon)
    if part == 2:
        oxygen = [x for x in data]
        carbon = [x for x in data]
        index = 0
        while index < len(data[0]):
            # Reduce
            if len(oxygen) > 1:
                oxygen = [x for x in oxygen if x[index] == str(most_common([x[index] for x in oxygen]))]

            if len(carbon) > 1:
                carbon = [x for x in carbon if x[index] == str(least_common([x[index] for x in carbon]))]
            index += 1

        print(oxygen, carbon)
        result = int(oxygen[0], 2) * int(carbon[0], 2)
        print(result)
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