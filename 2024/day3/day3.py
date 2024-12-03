import re
from typing import List


def read_file(filename: str) -> List[str]:
    with open(filename) as f:
        return f.readlines()


class Day3:
    def __init__(self, filename):
        self.instruction_string = read_file(filename)
        self.muls = self.find_mul_strs(self.instruction_string)
        self.solution1 = self.solve1(self.muls)
        self.do_muls = self.find_muls_and_dos(self.instruction_string)
        self.solution2 = self.solve2(self.do_muls)

    def find_mul_strs(self, instruction_string: List[str]) -> List[str]:
        mul_strs = []
        pattern = r"mul\((\d+),(\d+)\)"
        for text in instruction_string:
            matches = re.findall(pattern, text)
            mul_strs.extend(matches)
        return mul_strs

    def solve1(self, muls: List[str]) -> int:
        return sum(map(lambda x: int(x[0])*int(x[1]), muls))

    def find_muls_and_dos(self, instruction_string: List[str]) -> List[str]:
        """
        :param instruction_string: List of strings that are gotten from the input file
        :return: Something like ['mul(2,4)', "don't()", 'mul(5,5)', 'mul(11,8)', 'do()', 'mul(8,5)']
        """
        mul_strs = []
        # Regular expression pattern to match mul(), do(), and don't()
        pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"

        for text in instruction_string:
            matches = re.findall(pattern, text)
            mul_strs.extend(matches)
        return mul_strs

    def solve2(self, do_muls: List[str]) -> int:
        do_operate = True
        solution_sum = 0
        for text in do_muls:
            if text == "don't()":
                do_operate = False
                continue
            if text == "do()":
                do_operate = True
                continue
            if do_operate:
                solution_sum += self.get_product(text)
        return solution_sum

    def get_product(self, text: str) -> int:
        pattern = r"mul\((\d+),(\d+)\)"
        matches = re.findall(pattern, text)
        for nums in matches:
            return int(nums[0])*int(nums[1])


if __name__ == '__main__':
    d3 = Day3('input.txt')
    print(d3.solution1)
    print(d3.solution2)
