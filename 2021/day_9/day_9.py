import numpy as np


class day_9:
    def __init__(self, file_name):
        self.low_points = []
        self.heightMap = self.__get_height_map(file_name)
        print(self.heightMap.shape)

    def __get_height_map(self, file_name):
        with open(file_name) as f:
            mat = f.readlines()
            mat = list(map(lambda x: list(x.strip()), mat))
            mat = np.array(mat).astype(int)
            return mat

    def is_low_point(self, i, j):
        top = True
        cellHeight = self.heightMap[i][j]
        if i > 0:
            top = self.heightMap[i - 1][j] > cellHeight
        bottom = True
        if i < 99:
            bottom = self.heightMap[i + 1][j] > cellHeight
        left = True
        if j > 0:
            left = self.heightMap[i][j - 1] > cellHeight
        right = True
        if j < 99:
            right = self.heightMap[i][j + 1] > cellHeight

        return all((left, right, top, bottom))

    def part1(self):
        sol = []
        for i in range(100):
            for j in range(100):
                if self.is_low_point(i, j):
                    sol.append(self.heightMap[i][j] + 1)
                    self.low_points.append((i, j))
        return sum(sol)

    def part2(self):
        sol = []
        for i, j in self.low_points:
            sol.append(self.size_of_basin(i, j))
        return np.prod(sorted(sol, reverse=True)[0:3])

    def size_of_basin(self, i, j):
        if not (0 <= i <= 99 and 0 <= j <= 99 and self.heightMap[i][j] < 9):
            return 0
        self.heightMap[i][j] = 9
        size = 1
        # if i + 1 <= 99 and self.heightMap[i + 1][j] < 9 and height == (self.heightMap[i + 1][j] - 1):
        size += self.size_of_basin(i + 1, j)
        # if i - 1 >= 0 and self.heightMap[i - 1][j] < 9 and height == (self.heightMap[i - 1][j] - 1):
        size += self.size_of_basin(i - 1, j)
        # if j - 1 >= 0 and self.heightMap[i][j-1] < 9 and height == (self.heightMap[i][j-1] - 1):
        size += self.size_of_basin(i, j - 1)
        # if j + 1 <= 99 and self.heightMap[i][j+1] < 9 and height == (self.heightMap[i][j+1] - 1):
        size += self.size_of_basin(i, j + 1)
        return size


if __name__ == '__main__':
    day_9 = day_9('input.txt')
    print(day_9.part1())
    print(day_9.part2())
