from functools import lru_cache

import numpy as np


class day_7:
    def __init__(self, file_name):
        self.pos = self.get_input(file_name)
        self.pos.sort()
        print(np.median(self.pos))

    def get_input(self, file_name):
        with open(file_name) as f:
            return list(map(int, f.readline().split(',')))

    def get_total_fuel_1(self):
        median = np.median(self.pos)
        pos = np.array(self.pos)
        return np.sum(np.abs(pos - median))

    def part_1(self):
        return self.get_total_fuel_1()

    """
    :param x: Location being considered as common point
    Function returns the total fuel required to travel  to x from all other points
    LRU cache is used to memoize the function as input may contain several repeated locations
    """
    @lru_cache
    def get_total_fuel_2(self, x):
        s = 0
        for loc in self.pos:
            diff = abs(loc - x)
            s += diff * (diff + 1) / 2
        return s

    def part_2(self):
        min_fuel = self.get_total_fuel_2(self.pos[0])
        for loc in range(self.pos[1], self.pos[-1]):
            min_fuel = min(min_fuel, self.get_total_fuel_2(loc))
        return min_fuel


if __name__ == '__main__':
    day_7 = day_7('input.txt')
    print(day_7.part_1())
    print(day_7.part_2())
