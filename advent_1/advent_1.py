def part_2():
    pass

def part_1():
    pass


def parse(data):
    pass

with open('inputs.txt', 'r') as fh:
    data = fh.read().splitlines()
    count = 0
    position = 1
    for i in ''.join(data):
        print(i)
        if i == '(':
            count += 1
        else:
            count -= 1
        if count == -1:
            print(position)
            break
        position += 1
    print(count)
    print(position)

