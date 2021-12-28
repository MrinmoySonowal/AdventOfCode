class day_10:
    def __init__(self, file_name):
        self.brackets_dict = {'}': '{', ']': '[', ')': '(', '>': '<'}
        self.opening_bracks_dict = {v: k for k,v in self.brackets_dict.items()}
        # self.opening_brackets = set(self.brackets_dict.values())
        self.points_syntax = {')': 3, ']': 57, '}': 1197, '>': 25137}
        self.points_autocorrect = {')': 1, ']': 2, '}': 3, '>': 4}
        assert len(self.points_syntax) == len(self.brackets_dict)
        self.navigation_syntax = self.__get_navigation_syntax(file_name)
        self.incomplete_lines = []

    def __get_navigation_syntax(self, file_name):
        with open(file_name) as f:
            mat = f.readlines()
            return mat

    def __score_error(self, chunks):
        stack = []
        for symb in chunks:
            if symb in self.opening_bracks_dict:  # opening bracket condition
                stack.append(symb)
            else:
                if stack == [] or (self.brackets_dict[symb] != stack[-1]):
                    return self.points_syntax[symb]
                else:
                    stack.pop(-1)
        return 0

    def part_1(self):
        syntax_err_score = 0
        for chunks in self.navigation_syntax:
            syntax_score = self.__score_error(chunks[:-1])
            syntax_err_score += syntax_score
            if syntax_score == 0:
                self.incomplete_lines.append(chunks[:-1])
        return syntax_err_score

    def __get_completion_string(self, chunks): # Method assumes chucks syntax score is 0
        stack = []
        for symb in chunks:
            if symb in self.opening_bracks_dict:  # opening bracket condition
                stack.append(symb)
            else:
                stack.pop(-1)
        return ''.join([self.opening_bracks_dict[open_brack] for open_brack in stack[::-1]])

    def __score_autocorrect(self, completion_string):
        autocomplete_score = 0
        for symb in completion_string:
            autocomplete_score *= 5
            autocomplete_score += self.points_autocorrect[symb]
        return autocomplete_score

    def part_2(self):
        autocomplete_scores = []
        for chunks in self.incomplete_lines:
            completion_string = self.__get_completion_string(chunks)
            autocomplete_scores.append(self.__score_autocorrect(completion_string))
        autocomplete_scores.sort()
        return autocomplete_scores[len(autocomplete_scores)//2]


if __name__ == '__main__':
    day_10 = day_10('input.txt')
    print("Syntax error score part 1: %d" % day_10.part_1())
    print("Autocorrect score part 2 : %d" % day_10.part_2())
