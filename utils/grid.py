from collections import namedtuple
from typing import Any, Callable

Coord = namedtuple("Coord", ["x", "y"])

class Grid:
    def __init__(self, filename: str, convert_to_type: Callable = lambda x: str(x)):
        with open(filename, 'r') as f:
            raw = [list(map(convert_to_type, list(l.strip()))) for l in f]
            assert all(len(l) == len(raw[0]) for l in raw)
        self.bounds = Coord(len(raw), len(raw[0]))
        self.raw = raw

    def inbounds(self, point: Coord):
        return 0 <= point.x < self.bounds.x and 0 <= point.y < self.bounds.y

    def at(self, point: Coord):
        if self.inbounds(point):
            return self.raw[point.x][point.y]
        else: return None

    def set(self, point: Coord, value: Any):
        if self.inbounds(point):
            self.raw[point.x][point.y] = value
            return True
        else: return False

    def points(self):
        return (Coord(x,y) for x in range(self.bounds.x) for y in range(self.bounds.y))
