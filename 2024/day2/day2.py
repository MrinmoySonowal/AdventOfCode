import numpy as np

from utils.runtime import calculate_runtime


class Day2:
    def __init__(self, filename):
        self.solution1 = self.solve_1(filename)
        self.solution2 = self.solve_2(filename)

    def _check_report_is_safe(self, report):
        diff = list(map(lambda x: x[0] - x[1], zip(report[0:], report[1:])))
        if diff[0] > 0:
            is_report_safe = self._check_diff(diff, lambda x: 1 <= x <= 3)
        else:
            is_report_safe = self._check_diff(diff, lambda x: -1 >= x >= -3)
        return is_report_safe

    def _check_diff(self, diff, condition):
        is_report_safe = True
        for i in diff:
            if not condition(i):
                is_report_safe = False
                break
        return is_report_safe

    @calculate_runtime
    def solve_1(self, filename):
        safe_report = 0
        with open(filename) as f:
            for report in f:
                report = list(map(int, report.split()))
                safe_report += self._check_report_is_safe(report)
        return safe_report

    @calculate_runtime
    def solve_2(self, filename):
        sum_safe = 0
        with open(filename) as f:
            for report in f:
                report = list(map(int, report.split()))
                if self._check_report_is_safe(report):
                    sum_safe += 1
                else:
                    for unsafe_index in range(len(report)):
                        new_numbers = report[0:unsafe_index] + report[unsafe_index + 1:]
                        if self._check_report_is_safe(new_numbers):
                            sum_safe += 1
                            break
        return sum_safe


if __name__ == '__main__':
    solver = Day2('input.txt')
    print(solver.solution1)
    print(solver.solution2)
