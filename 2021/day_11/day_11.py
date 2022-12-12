import numpy as np
class day_11:
    def __init__(self, file_name):
        self.octupuses = mat = np.loadtxt(file_name, dtype=int)
        self.flashes = 0

    def update(self):
        self.octupuses += 1
        for i in range(10):
            for j in range(10):
                if self.octupuses[i][j]>9:
                    self.flashes += 1
                    self.dfs(i, j)
        
    def dfs(self, i, j):
        self.octupuses[i][j] += 1




    def part_1(self):
        for _ in range(100):
            self.update()
        return self.flashes




if __name__ == '__main__':
    day_11 = day_11('input.txt')
    print(day_11.part_1())

