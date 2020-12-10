def part_2():
    pass

def part_1(data):
    s = set()
    horizontal, vertical = 0, 0
    for i in ''.join(data):
        if i == '^':
            vertical += 1
        elif i == 'v':
            vertical -= 1
        elif i == '>':
            horizontal += 1
        elif i == '<':
            horizontal -= 1

        position = (horizontal, vertical)
        s.add(position)
    return list(s)


def parse(data):
    pass

with open('inputs.txt', 'r') as fh:
    data = fh.read().splitlines()
    part1 = part_1(data)
    print(len(part1))

    count = 0
    santa, robot = [],[]
    for i in ''.join(data):
        if count % 2 == 0:
            santa.append(i)
        else:
            robot.append(i)
        count += 1

    s1,s2 = part_1(santa), part_1(robot)
    print(len(set(s1 + s2)))


