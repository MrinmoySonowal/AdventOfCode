import numpy as np


class day_4:
    def __init__(self):
        with open('input.txt') as f:
            lines = f.readlines()
            self.calls = list(map(int, lines[0][:-1].split(',')))
        board_line = np.array([])
        ct = 0
        for line in lines[2:]:
            if line == '\n':
                ct += 1
                continue
            board_line = np.append(board_line, list(map(int, filter(lambda x: x != '', line.strip().split(' ')))))
        self.boards = board_line.reshape(100, 5, 5)
        # print(self.boards[99])
        # print(self.boards.shape)

    def part1(self):
        for call in self.calls:
            for i in range(100):
                self.board_call(i, call)
                if self.rows_check(i) or self.columns_check(i):
                    return np.sum(self.boards[i][self.boards[i] > 0]) * call

    def part2(self):
        winning_boards = set()
        for call in self.calls:
            for i in range(100):
                if i in winning_boards:
                    continue
                self.board_call(i, call)
                if self.rows_check(i) or self.columns_check(i):
                    winning_boards.add(i)
                    if len(winning_boards) == 100:
                        return np.sum(self.boards[i][self.boards[i] > 0]) * call

    def board_call(self, i, call):
        self.boards[i] = np.where(self.boards[i] == call, -1, self.boards[i])

    def rows_check(self, i):
        for row in self.boards[i]:
            if np.array_equal(row, [-1] * 5):
                return True
        return False

    def columns_check(self, i):
        for col in self.boards[i].T:
            if np.array_equal(col, [-1] * 5):
                return True
        return False


if __name__ == '__main__':
    day_4 = day_4()
    print(day_4.part1())
    print(day_4.part2())
