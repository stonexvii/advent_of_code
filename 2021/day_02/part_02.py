from collections import namedtuple

Move = namedtuple('Move', ['direct', 'amount'])


def read_data(path: str):
    result = []
    with open(path, 'r') as file:
        while line := file.readline():
            direct, amount = line.strip().split()
            result.append(Move(direct, amount))
    return result


def solution(path: str):
    position = [0, 0]
    aim = 0
    for move in read_data(path):
        if move.direct.startswith('f'):
            position[0] += int(move.amount)
            position[1] += int(move.amount) * aim
        elif move.direct.startswith('u'):
            aim -= int(move.amount)
        else:
            aim += int(move.amount)
    return position[0] * position[1]


if __name__ == '__main__':
    print(solution('input_data.txt'))
