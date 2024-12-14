import re

import numpy as np
from Demos.mmapfile_demo import offset

from DailyAOCSolver import DailyAOCSolver


class Day13(DailyAOCSolver):
    def __init__(self,filename):
        super().__init__(filename)

    def get_input(self):
        return open(self.filename,'r').read()

    def parse_input(self):
        return [machine for machine in self.input_data.split('\n\n')]

    def solve1(self):
        total = 0
        tolerance = 0.0001
        for machine in self.parsed_input:
            ax, ay, bx, by, x, y = map(int, re.findall(r'(\d+)', machine))
            A, B = np.linalg.solve([[ax,bx],[ay,by]],[x,y])
            if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
                total += 3 * A + B
        print("Solution of part 1", total)

    def solve2(self):
        total = 0
        tolerance = 0.0001
        offset = 10000000000000
        for machine in self.parsed_input:
            ax, ay, bx, by, x, y = map(int, re.findall(r'(\d+)', machine))
            x+=offset
            y+=offset
            A, B = np.linalg.solve([[ax, bx], [ay, by]], [x, y])
            if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
                total += 3 * A + B
        print("Solution of part 1", total)

if __name__ == '__main__':
    d13 = Day13('input.txt')
    d13.run()