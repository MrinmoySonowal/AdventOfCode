import copy

class Day9:
    def __init__(self, filename):
        self.F, self.S = self.get_input(filename)
        print(self.F)
        print(self.S)
        self.solve1(copy.deepcopy(self.F), copy.deepcopy(self.S))
        self.solve2(copy.deepcopy(self.F), copy.deepcopy(self.S))

    def get_input(self, filename):
        F, S, p = [], [], 0
        for i, c in enumerate(open(filename).read().strip()):
            [F, S][i % 2] += [[*range(p, p := p + int(c))]]
        return F, S

    def solve1(self, F, S):
        S = sum(S, [])
        for f in reversed(F):
            for x in reversed(range(len(f))):
                if len(S) and f[x] > S[0]:
                    f[x] = S[0]
                    S = S[1:]
        print(sum((i * j) for i, f in enumerate(F) for j in f))

    def solve2(self, F, S):
        for y in reversed(range(len(F))):
            for x in range(len(S)):
                if len(S[x]) >= len(F[y]) and F[y][0] > S[x][0]:
                    F[y] = S[x][:len(F[y])]
                    S[x] = S[x][len(F[y]):]
        print(sum((i * j) for i, f in enumerate(F) for j in f))


if __name__ == '__main__':
    d9 = Day9('test-input.txt')
