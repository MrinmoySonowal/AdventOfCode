class RuckSack:
    def __init__(self, filename):
        self.lines = self.read_file(filename)
        self.items_pt1 = self.process_items_pt1(self.lines)
        self.items_pt2 = self.process_items_pt2(self.lines)

    def read_file(self, filename):
        lines = []
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                lines.append(line)
        return lines

    def process_items_pt1(self, lines):
        processed_items = []
        for item in lines:
            mid_len = len(item) // 2
            first_half = item[:mid_len]
            second_half = item[mid_len:]
            processed_items.append((first_half, second_half))
        return processed_items

    def process_items_pt2(self, lines):
        processed_items = []
        for i in range(0, len(lines) - 3 + 1, 3):
            processed_items.append(lines[i:i + 3])
        return processed_items

    def priority(self, items):
        common_items = list(set.intersection(*map(set, items)))
        assert len(common_items) == 1
        common_item = common_items[0]
        if common_item.islower():
            return (ord(common_item) - ord('a')) + 1
        return (ord(common_item) - ord('A')) + 27

    def get_sum_priority(self, items):
        return sum(map(self.priority, items))


if __name__ == '__main__':
    rs = RuckSack('test-input.txt')
    print("test input pt1", rs.get_sum_priority(rs.items_pt1))
    print("test input pt2", rs.get_sum_priority(rs.items_pt2))
    rs = RuckSack('input.txt')
    print("TASK 1 answer:", rs.get_sum_priority(rs.items_pt1))
    print("TASK 2 answer:", rs.get_sum_priority(rs.items_pt2))
