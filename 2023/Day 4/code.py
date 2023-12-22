import functools
from typing import List


def get_card_data(filename: str):
    with open(filename, "r") as file:
        winning_numbers_mat = []
        our_numbers_mat = []
        for line in file:
            winning_numbers, our_numbers = line[:-1].split(":")[1].split("|")
            winning_numbers = [int(num) for num in winning_numbers.split(" ") if num != ""]
            our_numbers = [int(num) for num in our_numbers.split(" ") if num != ""]
            winning_numbers_mat.append(winning_numbers)
            our_numbers_mat.append(our_numbers)
        return winning_numbers_mat, our_numbers_mat


class ScoreColourfulCards:
    def __init__(self, filename: str):
        self.winning_numbers_mat, self.our_numbers_mat = get_card_data(filename)
        self.num_cards = len(self.winning_numbers_mat)
        self.score = self.get_score()
        print("Part 1 Score:", self.score)
        self.copies_cache = {}
        self.num_copies = self.get_num_copies()
        print("Part 2 Number of copies:", self.num_copies)

    def get_score(self) -> int:
        score = 0
        for i in range(self.num_cards):
            score += self.get_card_score(i)
        return score

    def get_card_score(self, i: int) -> int:
        card_win_set = set(self.winning_numbers_mat[i])
        card_our_set = set(self.our_numbers_mat[i])
        our_win_num = len(card_win_set.intersection(card_our_set))
        if our_win_num == 0:
            return 0
        else:
            return 2 ** (len(card_win_set.intersection(card_our_set)) - 1)

    def get_num_copies(self) -> int:
        cards = [1] * self.num_cards
        for i in range(self.num_cards):
            our_win_num = len(set(self.winning_numbers_mat[i]) & set(self.our_numbers_mat[i]))
            for j in range(i + 1, min(i + 1 + our_win_num, self.num_cards)):
                cards[j] += cards[i]
        return sum(cards)


if __name__ == "__main__":
    print("## EXAMPLE ##")
    ScoreColourfulCards("example.txt")

    print("\nInput")
    ScoreColourfulCards("input.txt")
