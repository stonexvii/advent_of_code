from collections import namedtuple

Path = namedtuple('Path', ('right', 'down'))

routes = (
    Path(1, 1),
    Path(3, 1),
    Path(5, 1),
    Path(7, 1),
    Path(1, 2),
)


def read_data(path: str):
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def solution(path: str):
    total = 1
    road_map = read_data(path)
    line_len = len(road_map[0])
    for route in routes:
        result, idx = 0, 0
        for line_idx in range(0, len(road_map), route.down):
            if line_idx:
                if road_map[line_idx][idx] == '#':
                    result += 1
            idx = (idx + route.right) % line_len
        total *= result
    return total


if __name__ == '__main__':
    print(solution('input_data.txt'))
