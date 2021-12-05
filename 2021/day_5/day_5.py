import numpy as np


class day_5:
    def __init__(self, file_name):
        self.line_segments = []
        self.mat = []
        self.assign_input(file_name)

    def assign_input(self, file_name):
        mat_size = 0
        with open(file_name) as f:
            line_segments = [inp_line.strip().split(' -> ') for inp_line in f.readlines()]
        max_rows, max_cols = 0, 0
        for line in line_segments:
            x1, y1 = map(int, line[0].split(','))
            x2, y2 = map(int, line[1].split(','))
            max_cols = max(max_cols, x1, x2)
            max_rows = max(max_rows, y1, y2)
            self.line_segments.append((x1, y1, x2, y2))
        self.mat = np.zeros((max_rows + 1, max_cols + 1))

    def part_1(self):
        for line_pts in self.line_segments:
            x1, y1, x2, y2 = line_pts
            if x1 == x2:
                row_idx_1 = min(y1, y2)
                row_idx_2 = max(y1, y2)
                self.mat[row_idx_1:row_idx_2 + 1, x1] += 1
            elif y1 == y2:
                col_idx_1 = min(x1, x2)
                col_idx_2 = max(x1, x2)
                self.mat[y1, col_idx_1:col_idx_2 + 1] += 1
        return np.sum(self.mat >= 2)

    def part_2(self):
        for line_pts in self.line_segments:
            x1, y1, x2, y2 = line_pts
            if x1 == x2:
                row_idx_1 = min(y1, y2)
                row_idx_2 = max(y1, y2)
                self.mat[row_idx_1:row_idx_2 + 1, x1] += 1
            elif y1 == y2:
                col_idx_1 = min(x1, x2)
                col_idx_2 = max(x1, x2)
                self.mat[y1, col_idx_1:col_idx_2 + 1] += 1
            elif abs(x1 - x2) == abs(y1 - y2):  # diagonal case for 45
                if x1 < x2 and y1 < y2:
                    for i in range(abs(x1 - x2) + 1):
                        self.mat[y1 + i][x1 + i] += 1
                elif x1 > x2 and y1 > y2:
                    for i in range(abs(x1 - x2) + 1):
                        self.mat[y2 + i][x2 + i] += 1
                elif x1 < x2 and y1 > y2:
                    for i in range(abs(x1 - x2) + 1):
                        self.mat[y1 - i][x1 + i] += 1
                elif x1 > x2 and y1 < y2:
                    for i in range(abs(x1 - x2) + 1):
                        self.mat[y2 - i][x2 + i] += 1

        return np.sum(self.mat >= 2)

    def print_mat(self):
        print(self.mat)


if __name__ == '__main__':
    d5 = day_5('test_input.txt')
    print(d5.part_1())
    d5 = day_5('test_input.txt')
    print(d5.part_2())
    d5.print_mat()
