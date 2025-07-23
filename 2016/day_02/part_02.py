import itertools
from collections import namedtuple

Direct = namedtuple('Direct', ['direct', 'count'])

KEYBOARD = (
    (' ', ' ', '1', ' ', ' '),
    (' ', '2', '3', '4', ' '),
    ('5', '6', '7', '8', '9'),
    (' ', 'A', 'B', 'C', ' '),
    (' ', ' ', 'D', ' ', ' '),
)
KEYBOARD_MAP = {
    0: (2, 2),
    1: (1, 3),
    2: (0, 4),
    3: (1, 3),
    4: (2, 2),
}

MOVEMENT = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}


def read_data(path: str):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def solution(path: str):
    data = []
    for line in read_data(path):
        line = itertools.groupby(line)
        data.append([Direct(entry[0], len(list(entry[1]))) for entry in line])
    code = []
    cur_x, cur_y = 2, 0
    for movement in data:
        for move in movement:
            for _ in range(move.count):
                next_x = cur_x + MOVEMENT[move.direct][0]
                next_y = cur_y + MOVEMENT[move.direct][1]
                if next_x in KEYBOARD_MAP and KEYBOARD_MAP[next_x][0] <= next_y <= KEYBOARD_MAP[next_x][1]:
                    cur_x, cur_y = next_x, next_y
        code.append(KEYBOARD[cur_x][cur_y])
    return ''.join(code)


if __name__ == '__main__':
    print(solution('input_data.txt'))
