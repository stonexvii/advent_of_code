from collections import namedtuple

Move = namedtuple('Move', ['x', 'y'])


def read_data(path: str):
    result = []
    with open(path, 'r') as file:
        while line := file.readline():
            direct, amount = line.strip().split()
            if direct.startswith('f'):
                result.append(Move(int(amount), 0))
            elif direct.startswith('d'):
                result.append(Move(0, int(amount)))
            else:
                result.append(Move(0, -int(amount)))
    return result


def solution(path: str):
    position = [0, 0]
    for move in read_data(path):
        position[0] += move.x
        position[1] += move.y
    return position[0] * position[1]


if __name__ == '__main__':
    print(solution('input_data.txt'))
