class CampCleanUp:
    def __init__(self, filename):
        self.ranges_pt = self.read_input(filename)

    def read_input(self, filename):
        inputs = []
        with open(filename, "r") as f:
            for line in f:
                inputs.append([tuple(map(int, i.split("-"))) for i in line.split(",")])
        return inputs

    def is_fully_overlapping_range(self, range_tuple):
        first_range, second_range = range_tuple
        assert first_range[0] <= first_range[1]
        assert second_range[0] <= second_range[1]
        if second_range[0] <= first_range[0] <= second_range[1] and second_range[0] <= first_range[1] <= second_range[1]:
            return True
        elif first_range[0]<=second_range[0]<=first_range[1] and first_range[0]<=second_range[1]<=first_range[1]:
            return True
        return False

    def is_overlapping_range(self, range_tuple):
        first_range, second_range = range_tuple
        assert first_range[0] <= first_range[1]
        assert second_range[0] <= second_range[1]
        if second_range[0] <= first_range[0] <= second_range[1]:
            return True
        if second_range[0] <= first_range[1] <= second_range[1]:
            return True
        if first_range[0] <= second_range[0] <= first_range[1]:
            return True
        if first_range[0] <= second_range[1] <= first_range[1]:
            return True
        return False

    def get_overlapping_ranges(self):
        return sum(map(self.is_fully_overlapping_range, self.ranges_pt))

    def get_overlapping_ranges_pt2(self):
        return sum(map(self.is_overlapping_range, self.ranges_pt))


if __name__ == '__main__':
    clu = CampCleanUp("test-input.txt")
    print("test task 1:", clu.get_overlapping_ranges())
    clu = CampCleanUp("input.txt")
    print("task 1 answer:", clu.get_overlapping_ranges())
    print("task 2 answer:", clu.get_overlapping_ranges_pt2())
