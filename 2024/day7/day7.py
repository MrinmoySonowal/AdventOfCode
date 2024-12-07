from typing import List, Callable


class Day7:
    def __init__(self, filename: str):
        self.file = open(filename)
        self.solution1 = self.count_valid_numbers(self._is_valid_list)
        print(self.solution1)
        self.file.seek(0) # Go back to first line
        self.solution2 = self.count_valid_numbers(self._is_valid_list_2)
        print(self.solution2)

    def _is_valid_list(self, result: int, operands: List[int], acc: int):
        if len(operands) == 0:
            return acc == result
        if acc > result:
            return False
        return (self._is_valid_list(result, operands[1:], acc + operands[0]) or
                self._is_valid_list(result, operands[1:], acc * operands[0]))

    def _is_valid_list_2(self, result: int, operands: List[int], acc: int):
        if len(operands) == 0:
            return acc == result
        if acc > result:
            return False
        return (self._is_valid_list_2(result, operands[1:], acc + operands[0]) or
                self._is_valid_list_2(result, operands[1:], acc * operands[0]) or
                self._is_valid_list_2(result, operands[1:], int(str(acc) + str(operands[0]))))

    def count_valid_numbers(self, is_valid_list: Callable):
        valid_results = []
        for line in self.file:
            result, operands = line.split(':')
            result = int(result)
            operands = list(map(int, operands.strip().split(' ')))
            if is_valid_list(result, operands, 0):
                valid_results.append(result)
        return sum(valid_results)


if __name__ == '__main__':
    d7 = Day7('input.txt')


