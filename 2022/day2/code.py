class RockPaperScissors:
    def __init__(self, filename):
        self.filename = filename
        self.moves = self.read_file(filename)
        self.oppn_moves_map = {
            'A': 'rock',
            'B': 'paper',
            'C': 'scissors'
        }
        self.your_moves_map = {
            'X': 'rock',
            'Y': 'paper',
            'Z': 'scissors'
        }
        self.losing_moves = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        self.winning_moves = dict(zip(self.losing_moves.values(), self.losing_moves.keys()))
        self.move_score = {
            "rock": 1,
            "paper": 2,
            "scissors": 3
        }
        self.DRAW_SCORE = 3
        self.WIN_SCORE = 6

    def read_file(self, filename):
        moves = []
        with open(filename, 'r') as f:
            for line in f:
                moves.append(line.strip().split(' '))
        return moves

    def score_move(self, opponent_move, your_move):
        your_move = self.your_moves_map[your_move]
        opponent_move = self.oppn_moves_map[opponent_move]
        score = self.move_score[your_move]
        if your_move == opponent_move:
            return score + self.DRAW_SCORE
        if self.losing_moves[your_move] == opponent_move:
            return score + self.WIN_SCORE
        return score

    def get_score_strat_guide(self):
        return sum(map(lambda moves: self.score_move(moves[0], moves[1]), self.moves))

    def score_move_pt2(self, opponent_move, result):
        opponent_move = self.oppn_moves_map[opponent_move]
        if result == "Y":  # DRAW
            return self.move_score[opponent_move] + self.DRAW_SCORE
        elif result == "X":  # LOSE
            your_move = self.losing_moves[opponent_move]
            return self.move_score[your_move]
        your_move = self.winning_moves[opponent_move]
        return self.move_score[your_move] + self.WIN_SCORE

    def get_score_strat_guide_pt2(self):
        return sum(map(lambda moves: self.score_move_pt2(moves[0], moves[1]), self.moves))


if __name__ == '__main__':
    rps = RockPaperScissors('test-input.txt')
    print("test input answer 1:", rps.get_score_strat_guide())
    print("test input answer 2:", rps.get_score_strat_guide_pt2())
    rps = RockPaperScissors('input.txt')
    print("TASK 1 answer:", rps.get_score_strat_guide())
    print("TASK 2 answer:", rps.get_score_strat_guide_pt2())
