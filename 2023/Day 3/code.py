from math import prod
from typing import List, Union, Optional, Tuple


def get_engine_schematic(filename: str) -> List[List[str]]:
    with open(filename) as file:
        return [[ch for ch in line[:-1]] for line in file.readlines()]


class AdjacentNumbersFromSchematic:
    def __init__(self, filename: str):
        self.schematic = get_engine_schematic(filename)
        self.num_rows = len(self.schematic)
        self.num_cols = len(self.schematic[0])
        print("Size of schematic:", self.num_rows, "x", self.num_cols)
        self.adjacent_numbers = self.find_valid_adjacent_numbers()
        print("Sum of adjacent numbers:", sum(self.adjacent_numbers))
        self.gear_map = self.get_gear_ratios()
        print("Gear map sum:", sum(self.gear_map.values()))

    def find_valid_adjacent_numbers(self):
        adjacent_numbers = []
        for row in range(self.num_rows):
            k = 0
            for col in range(self.num_cols):
                if k > 0:
                    k -= 1
                elif self.schematic[row][col].isdigit():
                    is_symbol_nearby = False
                    while col + k < self.num_cols and self.schematic[row][col + k].isdigit():
                        if not is_symbol_nearby and self.is_symbol_near(row, col + k):
                            is_symbol_nearby = True
                        k += 1
                    number = int("".join(self.schematic[row][col:col + k]))
                    if is_symbol_nearby:
                        adjacent_numbers.append(number)
        return adjacent_numbers

    def get_gear_ratios(self):
        gear_map = {}
        for row in range(self.num_rows):
            k = 0
            for col in range(self.num_cols):
                if k > 0:
                    k -= 1
                elif self.schematic[row][col].isdigit():
                    gears = set()
                    while col + k < self.num_cols and self.schematic[row][col + k].isdigit():
                        symb_pos = self.is_symbol_near(row, col + k)
                        if symb_pos:
                            symb_row, symb_col = symb_pos
                            if self.schematic[symb_row][symb_col] == "*":
                                gears.add((symb_row, symb_col))
                        k += 1
                    number = int("".join(self.schematic[row][col:col + k]))
                    for gear_pos in gears:
                        if gear_pos not in gear_map:
                            gear_map[gear_pos] = [number]
                        else:
                            gear_map[gear_pos].append(number)
        for key, value in gear_map.items():
            value = value if len(value) > 1 else [0]
            gear_map[key] = prod(value)
        print(gear_map)
        return gear_map

    def is_symbol_near(self, row: int, col: int) -> Optional[Tuple[int, int]]:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if 0 <= row + i < len(self.schematic) and 0 <= col + j < len(self.schematic[row]):
                    symbol = self.schematic[row + i][col + j]
                    if not symbol.isdigit() and symbol != '.':  # if symbol is not alphanumeric and not a dot
                        return row+i, col+j
        return None


if __name__ == "__main__":
    print("## EXAMPLE ##")
    AdjacentNumbersFromSchematic("example.txt")
    print("\n## ACTUAL ##")
    AdjacentNumbersFromSchematic("input.txt")
