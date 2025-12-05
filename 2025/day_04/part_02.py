from collections import namedtuple

Position = namedtuple('Position', ['line', 'idx'])


def read_data(path: str):
    with open(path, 'r') as file:
        data_map = [f'.{i.strip()}.' for i in file.readlines()]
        data_map.insert(0, '.' * len(data_map[0]))
        data_map.append('.' * len(data_map[0]))
    return data_map


def check_pepperz(data_map: list[list[str]], line: int, idx: int):
    positions = [
        Position(-1, -1),
        Position(-1, 0),
        Position(-1, 1),
        Position(0, -1),
        Position(0, 1),
        Position(1, -1),
        Position(1, 0),
        Position(1, 1),
    ]
    total = 0
    if data_map[line][idx] == '@':
        for position in positions:
            if data_map[line + position.line][idx + position.idx] != '.':
                total += 1
        if total < 4:
            data_map[line][idx] = 'x'
        return total < 4


def change_x_to_dot(data_map: list[list[str]]):
    for line in range(len(data_map)):
        for idx in range(len(data_map[0])):
            if data_map[line][idx] == 'x':
                data_map[line][idx] = '.'


def solution(path: str):
    total = 0
    data_map = [list(line) for line in read_data(path)]
    while True:
        result = 0
        for line in range(1, len(data_map) - 1):
            for idx in range(1, len(data_map[0]) - 1):
                if check_pepperz(data_map, line, idx):
                    result += 1
        if not result:
            break
        change_x_to_dot(data_map)
        total += result
    return total


if __name__ == '__main__':
    print(solution('input_data.txt'))
