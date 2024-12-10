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

    def inbounds(self, p: Coord):
        return 0 <= p.x < self.bounds.x and 0 <= p.y < self.bounds.y

    def at(self, p: Coord):
        if self.inbounds(p):
            return self.raw[p.x][p.y]
        else: return None

    def set(self, p: Coord, c: Any):
        if self.inbounds(p):
            self.raw[p.x][p.y] = c
            return True
        else: return False

    def points(self):
        return (Coord(x,y) for x in range(self.bounds.x) for y in range(self.bounds.y))
