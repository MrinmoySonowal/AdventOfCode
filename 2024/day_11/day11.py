from collections import defaultdict

from typing import Dict

from utils.math_utils import count_digits, is_even

from DailyAOCSolver import DailyAOCSolver
from utils.runtime import calculate_runtime


class Day11(DailyAOCSolver):
    def __init__(self, filename):
        super().__init__(filename)

    def get_input(self):
        with open(self.filename) as f:
            return f.read().strip()

    def parse_input(self):
        return self.input_data

    def _blink(self, stone_str: str):
        stones = stone_str.split(" ")
        new_stones = []
        for i in range(len(stones)):
            if stones[i] == '0':
                new_stones.append(1)
            elif is_even(len(stones[i])):
                new_stones.extend([int(stones[i][:len(stones[i])//2]), int(stones[i][len(stones[i])//2:])])
            else:
                new_stones.append(int(stones[i])*2024)
        return " ".join(map(str, new_stones))

    @calculate_runtime
    def solve1(self):
        stone_str = self.input_data
        for i in range(25):
            stone_str = self._blink(stone_str)
        print(len(stone_str.split(" ")))

    def _blink_optimised(self, stones: Dict[int, int]):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
            elif is_even(num_digits:=count_digits(stone)):
                divisor = (10 ** (num_digits / 2))
                lh, rh = stone // divisor, stone % divisor
                new_stones[int(lh)] += count
                new_stones[int(rh)] += count
            else:
                new_stones[stone * 2024] += count
        return new_stones

    def _blink_optimised_old(self, stones: Dict[int, int]):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                lh, rh = s[: len(s) // 2], s[len(s) // 2:]
                new_stones[int(lh)] += count
                new_stones[int(rh)] += count
            else:
                new_stones[stone * 2024] += count
        return new_stones

    @calculate_runtime
    def solve2(self):
        stones = {n: 1 for n in map(int, self.input_data.split(" "))}
        for i in range(75):
            stones = self._blink_optimised(stones)
        print(sum(stones.values()))


if __name__ == '__main__':
    d11 = Day11('input.txt')
    d11.run()
