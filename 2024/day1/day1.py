import numpy as np
from utils.runtime import calculate_runtime


@calculate_runtime
def gen_list(filename):
    """
    Generates the list of numbers from the given file
    """
    return np.loadtxt(filename)


class Day1:
    def __init__(self, filename):
        self.input_list = gen_list(filename)
        self.solution_1 = self.solve_part_1(self.input_list)
        self.solution_2 = self.solve_part_2(self.input_list)

    @calculate_runtime
    def solve_part_1(self, input_list):
        input_list[:, 0].sort()
        input_list[:, 1].sort()
        diff_col = np.abs(input_list[:, 0] - input_list[:, 1])
        return np.sum(diff_col)

    def _count_frequency(self, list):
        unique_elements, counts = np.unique(list, return_counts=True)
        return dict(zip(unique_elements, counts))

    def _score_similarity(self, elements, count_freq_dict):
        vectorized_get = np.vectorize(lambda x: count_freq_dict.get(x, 0))
        count_freq = vectorized_get(elements)
        return np.sum(elements * count_freq)

    @calculate_runtime
    def solve_part_2(self, input_list):
        column2 = input_list[:, 1].astype(int)
        count_freq_dict = self._count_frequency(column2)
        return self._score_similarity(column2, count_freq_dict)


@calculate_runtime
def run():
    ld = Day1('input.txt')
    print("Solution 1:", ld.solution_1)
    print("Solution 2:", ld.solution_2)


if __name__ == '__main__':
    run()
