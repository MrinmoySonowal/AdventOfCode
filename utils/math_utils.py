from math import floor, log10


def count_digits(number):
    if number == 0:
        return 1
    return floor(log10(abs(number))) + 1