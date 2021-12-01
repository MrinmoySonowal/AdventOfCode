if __name__ == '__main__':
    with open('input.txt') as f:
        lines = list(map(int,f.readlines()))
        ct = 0
        for i in range(1,len(lines)):
            ct += lines[i]>lines[i-1]
        print(ct)

        ct = 0
        for i in range(1, len(lines) - 2):
            print(lines[i:i + 3])
            ct += sum(lines[i:i + 3]) > sum(lines[i - 1:i + 2])
        print(ct)
