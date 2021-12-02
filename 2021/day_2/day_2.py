def part1(commands):
    horz_dist = 0
    depth = 0
    for command in commands:
        cmd, dist = command.split(' ')
        dist = int(dist)
        if cmd == 'forward':
            horz_dist += dist
        elif cmd == 'up':
            depth -= dist
        else:
            depth += dist
    print(f"Part 1 solution: {(horz_dist * depth)}")


def part2(commands):
    horz_dist, depth = 0, 0
    aim = 0
    for command in commands:
        cmd, dist = command.split(' ')
        dist = int(dist)
        if cmd == 'forward':
            horz_dist += dist
            depth += aim * dist
        elif cmd == 'up':
            aim -= dist
        else:
            aim += dist
    print(f"Part 2 solution: {(horz_dist * depth)}")


if __name__ == '__main__':
    with open('input.txt') as f:
        commands = f.readlines()
        part1(commands)
        part2(commands)
