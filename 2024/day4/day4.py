from typing import List

import numpy as np


class Day4:
    def __init__(self, filename):
        self.puzzle_input = np.array(self.get_puzzle_input(filename))
        self.num_of_rows = len(self.puzzle_input)
        self.num_of_cols = len(self.puzzle_input[0])
        self.solution1 = self.search_xmas_occurrences()
        self.solution2 = self.search_mas_in_x_shape_occurrence()

    def get_puzzle_input(self, filename) -> List[List[str]]:
        with open(filename) as f:
            lines = f.read().splitlines()
            return [list(line) for line in lines]

    def search_xmas_occurrences(self) -> int:
        occurrence_count = 0
        for i in range(self.num_of_rows):
            for j in range(self.num_of_cols):
                if self.puzzle_input[i][j] == "X":
                    occurrence_count += self.search_all_directions(i, j)
        print(occurrence_count)
        return occurrence_count

    def search_all_directions(self, i, j) -> int:
        occurrence_count = 0
        LOOK_UP_WORD = "XMAS"
        # Search up
        if (i - 3) >= 0:
            word = "".join(self.puzzle_input[i - 3:i + 1, j][::-1])
            if word == LOOK_UP_WORD:
                print(i, j, word, "UP")
                occurrence_count += 1
        if (i + 3) < self.num_of_rows:
            word = "".join(self.puzzle_input[i:i + 4, j])
            if word == LOOK_UP_WORD:
                print(i, j, word, "DOWN")
                occurrence_count += 1
        if (j - 3) >= 0:
            word = "".join(self.puzzle_input[i, j - 3:j + 1][::-1])
            if word == LOOK_UP_WORD:
                print(i, j, word, "LEFT")
                occurrence_count += 1
        if (j + 3) < self.num_of_cols:
            word = "".join(self.puzzle_input[i, j:j + 4])
            if word == LOOK_UP_WORD:
                print(i, j, word, "RIGHT")
                occurrence_count += 1

        for r in [-1, 1]:
            for c in [-1, 1]:
                word = ""
                for x in range(4):
                    if 0 <= (i + r * x) < self.num_of_rows and 0 <= (j + c * x) < self.num_of_cols:
                        word += self.puzzle_input[i + r * x][j + c * x]
                if word == LOOK_UP_WORD:
                    print(i, j, word, "DIAG")
                    occurrence_count += 1
        return occurrence_count

    def search_mas_in_x_shape_occurrence(self):
        occurrence_count = 0
        for i in range(self.num_of_rows):
            for j in range(self.num_of_cols):
                if self.puzzle_input[i][j] == "A":
                    occurrence_count += self.search_two_diags(i, j)
        print(occurrence_count)
        return occurrence_count

    def search_two_diags(self, i, j):
        if 0 <= (i - 1) and i + 1 < self.num_of_rows and 0 <= (j - 1) and j + 1 < self.num_of_cols:
            word_mat = self.puzzle_input[i - 1:i + 2, j - 1:j + 2]
            prim_diag_word = "".join(word_mat.diagonal())
            sec_diag_word = "".join(np.fliplr(word_mat).diagonal())
            if prim_diag_word in ["MAS", "SAM"] and sec_diag_word in ["MAS", "SAM"]:
                return True
        return False


if __name__ == '__main__':
    d4 = Day4('input.txt')
