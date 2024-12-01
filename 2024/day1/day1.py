import numpy as np


def gen_list(fileName):
    """
    Generates the list of numbers from the given file
    """
    return np.loadtxt(fileName)


class Day1:
    def __init__(self, fileName):
        self.input_list = gen_list(fileName)
        self.solution_1 = self.solve_part_1(self.input_list)
        self.solution_2 = self.solve_part_2(self.input_list)

    def solve_part_1(self, input_list):
        input_list[:, 0].sort()
        input_list[:, 1].sort()
        diff_col = np.abs(input_list[:, 0] - input_list[:, 1])
        return np.sum(diff_col)

    def _countFrequency(self, list):
        unique_elements, counts = np.unique(list, return_counts=True)
        return dict(zip(unique_elements, counts))

    def _score_similarity(self, elements, countFreqDict):
        vectorized_get = np.vectorize(lambda x: countFreqDict.get(x, 0))
        count_freq = vectorized_get(elements)
        return np.sum(elements * count_freq)

    def solve_part_2(self, input_list):
        column2 = input_list[:, 1].astype(int)
        count_freq_dict = self._countFrequency(column2)
        return self._score_similarity(column2, count_freq_dict)


if __name__ == '__main__':
    ld = Day1('input.txt')
    print(ld.solution_1)
    print(ld.solution_2)
