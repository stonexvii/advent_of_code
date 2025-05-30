from collections import namedtuple

Light = namedtuple('Light', ['x', 'y'])
Instruction = namedtuple('Instruction', ['switch', 'start', 'finish'])


def read_data(path: str):
    oper = {
        'turn on': 1,
        'turn off': -1,
        'toggle': 2,
    }
    data = []
    with open(path, 'r', encoding='UTF-8') as file:
        for line in file:
            prefix, second = line.strip().split(' through ')
            operation, first = prefix.rsplit(' ', 1)
            data.append(
                Instruction(
                    switch=oper[operation],
                    start=Light(*map(int, first.split(','))),
                    finish=Light(*map(int, second.split(',')))),
            )
    return data


def solution(path: str):
    light_map = [[0 for _ in range(1000)] for _ in range(1000)]
    data = read_data(path)
    for instruction in data:
        for x in range(instruction.start.x, instruction.finish.x + 1):
            for y in range(instruction.start.y, instruction.finish.y + 1):
                light_map[x][y] += instruction.switch
                if light_map[x][y] < 0:
                    light_map[x][y] = 0

    return sum(map(sum, light_map))


if __name__ == '__main__':
    print(solution('input_data.txt'))
