from graphlib import TopologicalSorter
from typing import Dict, Set, Tuple, List


class Day5:
    def __init__(self, rules_filename: str, updates_filename: str):
        self.rules = self.get_rules(rules_filename)
        self.updates = self.get_updates(updates_filename)
        self.solution1, self.solution2  = self.solve()

    def get_rules(self, rules_filename: str) -> Dict[int, Set[int]]:
        rules_map = {}
        with open(rules_filename) as f:
            for line in f:
                num_before, num_after = line.split("|")
                if int(num_before) in rules_map:
                    rules_map[int(num_before)].add(int(num_after))
                else:
                    rules_map[int(num_before)] = {int(num_after)}
        return rules_map

    def get_updates(self, updates_filename: str) -> List[List[int]]:
        with open(updates_filename) as f:
            return list(map(lambda line: list(map(int, line[:-1].split(","))), f.readlines()))

    def solve(self) -> Tuple[int, int]:
        # Get the valid updates by summing the middle value of valid updates for pt1 and invalid (after sorting) for pt2
        middle_sum_1 = 0
        middle_sum_2 = 0
        for update in self.updates:
            middle_num = int(update[len(update) // 2])
            seen_before_num_set = set()
            for num in update:
                if num in seen_before_num_set:
                    break
                if num in self.rules:
                    # We have seen this number before, it should have come after
                    if seen_before_num_set.intersection(self.rules[num]):
                        break
                seen_before_num_set.add(num)
            if len(seen_before_num_set) == len(update):
                middle_sum_1 += middle_num
            else:
                exists = set(update)
                sorter = TopologicalSorter()
                for before_num, after_nums in self.rules.items():
                    for after_num in after_nums:
                        if before_num not in exists or after_num not in exists:
                            continue
                        sorter.add(before_num, after_num)
                order = list(number for number in sorter.static_order() if number in exists)
                middle_sum_2 += order[len(order) // 2]
        return middle_sum_1, middle_sum_2


if __name__ == '__main__':
    d5 = Day5('input-rules.txt', 'input-updates.csv')
    print(d5.rules)
    print(d5.solution1)
    print(d5.solution2)
