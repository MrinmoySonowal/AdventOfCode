from utils.grid import Grid, Coord
from utils.runtime import calculate_runtime


class Day10:
    def __init__(self, filename):
        self.grid = Grid(filename, int)
        self.solve1()
        self.solve2()

    @calculate_runtime
    def solve1(self):
        score = 0
        for coord in self.grid.points():
            if self.grid.at(coord) == 0:
                visited_set = set()
                up_path_score    = self.count_score(Coord(coord.x, coord.y - 1), 1, visited_set)
                down_path_score  = self.count_score(Coord(coord.x, coord.y + 1), 1, visited_set)
                left_path_score  = self.count_score(Coord(coord.x - 1, coord.y), 1, visited_set)
                right_path_score = self.count_score(Coord(coord.x + 1, coord.y), 1, visited_set)
                score += up_path_score + down_path_score + left_path_score + right_path_score
        print(score)

    def count_score(self, coord: Coord, level: int, visited_set: set) -> int:
        if not self.grid.inbounds(coord) or self.grid.at(coord)!=level or coord in visited_set:
            return 0
        visited_set.add(coord)
        if self.grid.at(coord) == 9 and level == 9:
            return 1
        up_path_score = self.count_score(Coord(coord.x, coord.y - 1), level + 1, visited_set)
        down_path_score = self.count_score(Coord(coord.x, coord.y + 1), level + 1, visited_set)
        left_path_score = self.count_score(Coord(coord.x - 1, coord.y), level + 1, visited_set)
        right_path_score = self.count_score(Coord(coord.x + 1, coord.y), level + 1, visited_set)
        return up_path_score + down_path_score + left_path_score + right_path_score

    @calculate_runtime
    def solve2(self):
        score = 0
        for coord in self.grid.points():
            if self.grid.at(coord) == 0:
                up_path_score    = self.count_score_2(Coord(coord.x, coord.y - 1), 1)
                down_path_score  = self.count_score_2(Coord(coord.x, coord.y + 1), 1)
                left_path_score  = self.count_score_2(Coord(coord.x - 1, coord.y), 1)
                right_path_score = self.count_score_2(Coord(coord.x + 1, coord.y), 1)
                score += up_path_score + down_path_score + left_path_score + right_path_score
        print(score)

    def count_score_2(self, coord: Coord, level: int) -> int:
        if not self.grid.inbounds(coord) or self.grid.at(coord)!=level:
            return 0
        if self.grid.at(coord) == 9 and level == 9:
            return 1
        up_path_score = self.count_score_2(Coord(coord.x, coord.y - 1), level + 1)
        down_path_score = self.count_score_2(Coord(coord.x, coord.y + 1), level + 1)
        left_path_score = self.count_score_2(Coord(coord.x - 1, coord.y), level + 1)
        right_path_score = self.count_score_2(Coord(coord.x + 1, coord.y), level + 1)
        return up_path_score + down_path_score + left_path_score + right_path_score

if __name__ == '__main__':
    d10 = Day10('input.txt')