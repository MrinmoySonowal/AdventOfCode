def part1(commands):
    sol = [0, 0]
    for command in commands:
        cmd, dist = command.split(' ')
        if cmd == 'forward':
            sol[0] += int(dist)
        elif cmd == 'up':
            sol[1] -= int(dist)
        else:
            sol[1] += int(dist)
    print("Part 1 solution: {}".format(sol[0] * sol[1]))


def part2(commands):
    sol = [0, 0]
    aim = 0
    for command in commands:
        cmd, dist = command.split(' ')
        if cmd == 'forward':
            sol[0] += int(dist)
            sol[1] += aim * int(dist)
        elif cmd == 'up':
            aim -= int(dist)
        else:
            aim += int(dist)
    print("Part 2 solution: {}".format(sol[0] * sol[1]))


if __name__ == '__main__':
    with open('input.txt') as f:
        commands = f.readlines()
        part1(commands)
        part2(commands)
