def get_games(filename):
    f = open(filename, "r")
    return [game[5:-1] for game in f]


class PossibleGames:

    def __init__(self, filename):
        self.games = get_games(filename)
        self.bag_cubes = {"red": 12, "green": 13, "blue": 14}
        self.valid_game_ids = self.count_valid_games(self.games)
        print("Sum of valid game ids:", sum(self.valid_game_ids))

    def count_valid_games(self, games):
        valid_games = []
        for game in games:
            game_id, game_data = game.split(": ")
            if self.valid_game(game_data):
                valid_games.append(int(game_id))
        return valid_games

    def valid_game(self, game_data):
        game_sets = game_data.split("; ")
        for game_set in game_sets:
            if not self.valid_set(game_set):
                return False
        return True

    def valid_set(self, game_set):
        cubes = game_set.split(", ")
        for cube in cubes:
            num_balls, cube_colour = cube.split(" ")
            if self.bag_cubes[cube_colour] < int(num_balls):
                return False
        return True


class PowerSetGames:

    def __init__(self, filename):
        self.games = get_games(filename)
        self.power_of_set = self.find_power_of_set(self.games)
        print("Sum of power of sets:", self.power_of_set)

    def find_power_of_set(self, games):
        power_of_set = 0
        for game in games:
            game_id, game_data = game.split(": ")
            power_of_set += self.calculate_power_set(game_data)
        return power_of_set

    def calculate_power_set(self, game_data):
        game_sets = game_data.split("; ")
        red, green, blue = 0, 0, 0
        for game_set in game_sets:
            for cube in game_set.split(", "):
                num_balls, cube_colour = cube.split(" ")
                num_balls = int(num_balls)
                if cube_colour == "blue":
                    blue = max(blue, num_balls)
                if cube_colour == "green":
                    green = max(green, num_balls)
                if cube_colour == "red":
                    red = max(red, num_balls)
        return red * green * blue


if __name__ == "__main__":
    pg = PossibleGames("input.txt")
    ps = PowerSetGames("input.txt")
