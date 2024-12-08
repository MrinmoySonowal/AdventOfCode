from utils.grid import Grid
from utils.grid import Coord

class Day8:
    def __init__(self, filename):
        self.grid = Grid(filename)
        self.antennas = self.get_antennas()
        self.solve1()
        self.solve2()

    def get_antennas(self):
        antennas = dict()
        for point in self.grid.points():
            if (freq := self.grid.at(point)) != '.':
                if freq in antennas:
                    antennas[freq].append(point)
                else:
                    antennas[freq] = [point]
        return antennas

    def solve1(self):
        antinodes = set()
        for freq in self.antennas:
            antennaListForFreq = self.antennas[freq]
            for i in range(len(antennaListForFreq) - 1):
                firstAntennaPoint = antennaListForFreq[i]
                for secondAntennaPoint in antennaListForFreq[i + 1:]:
                    p1 = Coord(2 * firstAntennaPoint.x - secondAntennaPoint.x, 2 * firstAntennaPoint.y - secondAntennaPoint.y)
                    if self.grid.inbounds(p1): antinodes.add(p1)
                    p2 = Coord(2 * secondAntennaPoint.x - firstAntennaPoint.x, 2 * secondAntennaPoint.y - firstAntennaPoint.y)
                    if self.grid.inbounds(p2): antinodes.add(p2)
        print(len(antinodes))

    def solve2(self):
        antinodes = set()
        for freq in self.antennas:
            antennaListForFreq = self.antennas[freq]
            for i in range(len(antennaListForFreq) - 1):
                firstAntennaPoint = antennaListForFreq[i]
                for secondAntennaPoint in antennaListForFreq[i + 1:]:
                    diff = Coord(secondAntennaPoint.x - firstAntennaPoint.x, secondAntennaPoint.y - firstAntennaPoint.y)
                    dist = 0
                    while True:
                        p1 = Coord(secondAntennaPoint.x + dist * diff.x, secondAntennaPoint.y + dist * diff.y)
                        p2 = Coord(firstAntennaPoint.x - dist * diff.x, firstAntennaPoint.y - dist * diff.y)
                        if self.grid.inbounds(p1):
                            antinodes.add(p1)
                        if self.grid.inbounds(p2):
                            antinodes.add(p2)
                        if not self.grid.inbounds(p1) and not self.grid.inbounds(p2):
                            break
                        dist += 1
        print(len(antinodes))


if __name__ == '__main__':
    d8 = Day8('input.txt')
