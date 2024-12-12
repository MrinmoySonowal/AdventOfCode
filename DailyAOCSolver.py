from abc import abstractmethod

class DailyAOCSolver:
    def __init__(self, filename):
        self.filename = filename
        self.input_data = self.get_input()
        self.parsed_input = self.parse_input()

    @abstractmethod
    def get_input(self):
        pass

    @abstractmethod
    def parse_input(self):
        pass

    def run(self):
        self.parse_input()
        self.solve1()
        self.solve2()

    @abstractmethod
    def solve1(self):
        pass

    @abstractmethod
    def solve2(self):
        pass
