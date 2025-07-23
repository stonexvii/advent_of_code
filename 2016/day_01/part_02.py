DIRECTIONS = {
    'N': {
        'L': 'W',
        'R': 'E',
    },
    'E': {
        'L': 'N',
        'R': 'S',
    },
    'S': {
        'L': 'E',
        'R': 'W',
    },
    'W': {
        'L': 'S',
        'R': 'N',
    },
}
MOVEMENTS = {
    'N': {
        'L': (-1, 0),
        'R': (1, 0),
    },
    'E': {
        'L': (0, -1),
        'R': (0, 1),
    },
    'S': {
        'L': (1, 0),
        'R': (-1, 0),
    },
    'W': {
        'L': (0, 1),
        'R': (0, -1),
    },
}


def read_data(path: str):
    with open(path, 'r') as file:
        data = file.read().split(', ')
    return tuple(map(lambda x: (x[0], int(x[1:])), data))


def solution(path: str):
    visited = {(0, 0)}
    road_map = read_data(path)
    cur_dir, cur_x, cur_y = 'N', 0, 0
    for direct, distance in road_map:
        for i in range(distance):
            cur_x += MOVEMENTS[cur_dir][direct][0]
            cur_y += MOVEMENTS[cur_dir][direct][1]
            if (cur_x, cur_y) in visited:
                return abs(cur_x) + abs(cur_y)
            visited.add((cur_x, cur_y))
        cur_dir = DIRECTIONS[cur_dir][direct]



if __name__ == '__main__':
    print(solution('input_data.txt'))
