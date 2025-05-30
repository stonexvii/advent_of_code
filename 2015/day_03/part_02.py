from part_01 import read_data


def solution(path: str):
    direction = {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0),
    }
    road_map = read_data(path)
    visited = {(0, 0)}
    real_santa, robo_santa = (0, 0), (0, 0)
    for idx in range(0, len(road_map), 2):
        santa_move = direction[road_map[idx]]
        robo_move = direction[road_map[idx + 1]]
        real_santa = (real_santa[0] + santa_move[0], real_santa[1] + santa_move[1])
        robo_santa = (robo_santa[0] + robo_move[0], robo_santa[1] + robo_move[1])
        visited.update({real_santa, robo_santa})
    return len(visited)


if __name__ == '__main__':
    print(solution('input_data.txt'))
