import numpy as np
from collections import Counter


def get_most_sig_bit(arr):
    most_common = Counter(arr).most_common()
    if len(most_common)==1:
        return most_common[0][0]
    else:
        if most_common[0][1] == most_common[1][1]:
            return '1'
        else:
            return most_common[0][0]


def get_least_sig_bit(arr):
    most_common = Counter(arr).most_common()
    if len(most_common) == 1:
        return most_common[0][0]
    else:
        if most_common[0][1] == most_common[1][1]:
            return '0'
        else:
            return most_common[1][0]


class day_3:
    def __init__(self):
        mat = np.loadtxt("input.txt", dtype=str)
        self.mat = np.array(list(map(lambda x: np.array(list(x)), mat)))
        self.gamma_str = ""
        self.elips_str = ""

    def part_1(self) -> int:
        mat = self.mat.T
        gamma_str = ""
        elips_str = ""
        for row in mat:
            gamma_str += get_most_sig_bit(row) # Row since we take transpose (hence column of self.mat)
            elips_str += get_least_sig_bit(row)
        self.gamma_str = gamma_str
        self.elips_str = elips_str
        return int(self.gamma_str, 2) * int(self.elips_str, 2)



    def part_2(self):
        temp_mat = self.mat
        no_of_col = len(self.mat[0])
        col = 0
        while len(temp_mat) != 1:
            most_sig_bit = get_most_sig_bit(temp_mat.T[col])
            temp_mat = temp_mat[temp_mat[:, col] == most_sig_bit, :]
            col = (col + 1) % no_of_col
        o2_rating = int("".join(temp_mat[0].tolist()), 2)

        temp_mat = self.mat
        no_of_col = len(self.mat[0])
        col = 0
        while len(temp_mat) != 1:
            least_sig_bit = get_least_sig_bit(temp_mat.T[col])
            temp_mat = temp_mat[temp_mat[:, col] == least_sig_bit, :]
            col = (col + 1) % no_of_col
        co2_rating = int("".join(temp_mat[0].tolist()), 2)

        return o2_rating * co2_rating


if __name__ == '__main__':
    day_3 = day_3()
    print(day_3.part_1())
    print(day_3.part_2())
