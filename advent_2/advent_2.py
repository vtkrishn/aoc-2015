def part_2():
    pass

def part_1():
    pass


def parse(data):
    return [int(i) for i in data.split('x')]

with open('inputs.txt', 'r') as fh:
    data = fh.read().splitlines()
    total = 0
    ribbon = 0
    for i in data:
        l,w,b = parse(i)
        total += (2*l*w + 2*w*b + 2*b*l) + min(l*w,w*b,b*l)
        ribbon += (l*w*b) + min ((2*l + 2*w), (2*w + 2*b), (2*b + 2*l))
    print(total,ribbon)
