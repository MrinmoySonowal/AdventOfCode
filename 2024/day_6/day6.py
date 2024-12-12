from __future__ import annotations

import sys
from typing import List, Tuple

sys.setrecursionlimit(10 ** 6)


class Day6:
    def __init__(self, filename):
        self.puzzle_map = self.get_map_path(filename)
        self.rows, self.cols = len(self.puzzle_map), len(self.puzzle_map[0])
        self.start_guard_r, self.start_guard_c = self.get_start_pos_of_guard()
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
        self.solution1 = self.find_number_of_visited_places(self.puzzle_map)
        self.solution2 = self.find_number_of_loops()

    def get_map_path(self, filename: str) -> List[List[str]]:
        with open(filename) as f:
            return [list(line.strip()) for line in f.readlines()]

    def get_start_pos_of_guard(self) -> Tuple[int, int]:
        for i in range(self.rows):
            for j in range(self.cols):
                if self.puzzle_map[i][j] == "^":
                    return i, j

    def find_number_of_visited_places(self, puzzle_map) -> int | None:
        """
        This method will keep traversing the map until the guard reaches an edge of the map (row = 0 or col = 0).
        We will maintain a direction pointer that will change when the guard faces an obstacle
        """
        visited_map = [["" for _ in range(self.cols)] for _ in range(self.rows)]
        visited_map[self.start_guard_r][self.start_guard_c] = "X"
        guard_r, guard_c = self.start_guard_r, self.start_guard_c
        visited_places = 1
        dir_ptr = 0
        seen_map = set()
        while guard_c not in [0, self.cols - 1] and guard_r not in [0, self.rows - 1]:
            if (guard_r, guard_c, dir_ptr) in seen_map:
                return
            seen_map.add((guard_r, guard_c, dir_ptr))
            row_move, col_move = self.directions[dir_ptr]
            while puzzle_map[guard_r + row_move][guard_c + col_move] == "#":
                visited_map[guard_r + row_move][guard_c + col_move] = "#"
                dir_ptr = (dir_ptr + 1) % len(self.directions)
                row_move, col_move = self.directions[dir_ptr]

            guard_r += row_move
            guard_c += col_move

            if visited_map[guard_r][guard_c] != "X":
                visited_places += 1
                visited_map[guard_r][guard_c] = "X"
            # print(self.directions[dir_ptr], self.guard_r, self.guard_c)
        return visited_places

    def find_number_of_loops(self):
        ct = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.puzzle_map[i][j] == ".":
                    self.puzzle_map[i][j] = "#"
                    if self.find_number_of_visited_places(self.puzzle_map) is None:
                        ct += 1
                    self.puzzle_map[i][j] = "."
        return ct


if __name__ == '__main__':
    d6 = Day6("input.txt")
    print(d6.solution1)
    print(d6.solution2)
