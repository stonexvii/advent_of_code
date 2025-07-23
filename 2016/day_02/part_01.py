import itertools
from collections import namedtuple

Diect = namedtuple('Direct', ['direct', 'count'])

KEYBOARD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

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
        data.append([Diect(entry[0], len(list(entry[1]))) for entry in line])
    code = []
    cur_button = [1, 1]
    for movement in data:
        for move in movement:
            for _ in range(move.count):
                next_button = [cur_button[0] + MOVEMENT[move.direct][0], cur_button[1] + MOVEMENT[move.direct][1]]
                if not (0 <= next_button[0] < len(KEYBOARD)) or not (0 <= next_button[1] < len(KEYBOARD[0])):
                    break
                cur_button = next_button

        code.append(KEYBOARD[cur_button[0]][cur_button[1]])
    return ''.join(list(map(str, code)))


if __name__ == '__main__':
    print(solution('input_data.txt'))
