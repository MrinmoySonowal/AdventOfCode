import numpy as np
from collections import Counter

class day_6:
    def __init__(self, file_name):
        self.inital_state = self.get_input(file_name)

    def get_input(self, file_name):
        with open(file_name) as f:
            return np.array(list(map(int, f.readline().split(','))))

    def update_state(self, state):
        count_zeros = np.count_nonzero(state == 0)
        if count_zeros != 0:
            state = np.append(state, [8] * count_zeros)
            state[:-count_zeros] -= 1
        else:
            state -= 1
        state[state < 0] = 6
        return state

    def part_1(self):
        state = self.inital_state.copy()
        for _ in range(80):
            state = self.update_state(state)
        return len(state)

    def part_2(self):
        ages = Counter(self.inital_state)
        for i in range(256):
            # -1 represents the newborns, it acts a temp variable
            ages = {n: ages[n + 1] for n in range(-1, 8)}
            # newborns assigned to timer 8
            ages[8] = ages[-1]
            # Since -1 holds the 0 values of the previous day, it gets added to the list of fishes with timer 6
            ages[6] += ages[-1]
            ages[-1] = 0
        return sum(ages.values())


if __name__ == '__main__':
    day_6 = day_6('input.txt')
    print(day_6.part_1())
    print(day_6.part_2())
