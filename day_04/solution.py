import argparse
import os
from typing import Dict, Any, List

class Board:
    def __init__(self, rows: List[int]) -> None:
        self.data = rows
        self.matched = [[0] * 5 for _ in range(5)]
        return

    def display(self, matched: bool = False) -> None:
        lines = []
        for i, row in enumerate(self.data):
            line = []
            for j, num in enumerate(row):
                value = ""
                if len(str(num)) == 1:
                    value = " " + str(num)
                else:
                    value = str(num)
                if matched:
                    if self.matched[i][j] != 1:
                        value = " ."
                line.append(value)
            lines.append(" ".join(line))
        print("\n")
        print("\n".join(lines))
        return

    def display_matched(self) -> None:
        self.display(matched=True)
        return

    def check_number(self, number: int) -> None:
        for row in range(5):
            for col in range(5):
                if self.data[row][col] == number:
                    self.matched[row][col] = 1
        return

    @property
    def unmarked_sum(self) -> int:
        total = 0
        for row in range(5):
            for col in range(5):
                if self.matched[row][col] == 0:
                    total += self.data[row][col]
        return total

    @property
    def is_complete(self) -> bool:
        for row in self.matched:
            if sum(row) == 5:
                return True
        for i in range(5):
            if sum(self.matched[j][i] for j in range(5)) == 5:
                return True
        return False


def create_boards(raw_boards: List[str]) -> List[Board]:
    rows = []
    boards = []
    for line in raw_boards:
        row = [int(x) for x in line.split(" ") if x != ""]
        rows.append(row)
        if len(rows) == 5:
            boards.append(Board(rows=rows))
            rows = []
    return boards


def load_file(part: int, source: str) -> List[int]:
    filename = os.path.join("data", f"{source}_{part}.txt")
    with open(filename, "r") as f:
        data = f.read().splitlines()
        return [int(x) for x in data[0].split(",")], data[1:]


def main(part: int, source: str) -> None:
    numbers, raw_boards = load_file(1, source)

    boards = create_boards([x for x in raw_boards if len(x) > 1])
    found = False
    winners = []
    for number in numbers:
        if (found and part == 1) or len(winners) == len(boards):
            break
        print(number)
        for i, board in enumerate(boards):
            if i in winners:
                continue
            board.check_number(number)
            if board.is_complete:
                winner = board
                found = True
                winner.display()
                winner.display_matched()

                score = winner.unmarked_sum * number
                print(score)
                winners.append(i)
                if part == 1:
                    break
    
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