def gen_list(fileName):
    """
    Generates the list of numbers from the given file
    """
    f = open(fileName, "r")
    return [line for line in f]


class Day1:
    def __init__(self, filename):
        lines = gen_list(filename)
        self.calibration_values = self.get_calibration_values(lines)
        self.calibration_values_2 = self.get_calibration_values_2(lines)
        self.sum = sum(self.calibration_values)

    def get_calibration_values(self, lines):
        calibration_values = []
        for line in lines:
            i, j = 0, len(line) - 1
            while i < len(line) and not line[i].isnumeric(): i += 1
            while j >= 0 and not line[j].isnumeric(): j -= 1
            calibration_values.append(int(line[i] + line[j]))
        return calibration_values

    def get_calibration_values_2(self, lines):
        calibration_values = []
        for line in lines:
            digits = []
            for i, ch in enumerate(line):
                if ch.isdigit():
                    digits.append(line[i])
                for d, val in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                    if line[i:].startswith(val):
                        digits.append(str(d+1))
            calibration_values.append(int(digits[0] + digits[-1]))
        return calibration_values

    def get_sum(self):
        return self.sum
