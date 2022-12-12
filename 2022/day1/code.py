class CalorieCounter:
    def __init__(self, filename):
        self.filename = filename
        self.calories = []

    def read_file(self):
        self.calories = []
        with open(self.filename, "r") as f:
            calorie = 0
            for line in f:
                if line != '\n':
                    calorie += int(line.strip())
                else:
                    self.calories.append(calorie)
                    calorie = 0

    def get_calories(self):
        return self.calories


if __name__ == '__main__':
    calCounter = CalorieCounter('input.txt')
    calCounter.read_file()
    ### TASK 1
    print(max(calCounter.get_calories()))

    ### TASK 2
    print(sum(sorted(calCounter.get_calories(), reverse=True)[0:3]))