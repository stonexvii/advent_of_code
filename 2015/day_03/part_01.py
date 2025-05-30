def read_data(path: str):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.read().replace('/n', '')
    return data


def solution(path: str):
    direction = {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0),
    }
    road_map = read_data(path)
    visited = {(0, 0)}
    current_point = (0, 0)
    for next_move in road_map:
        move = direction[next_move]
        current_point = (current_point[0] + move[0], current_point[1] + move[1])
        visited.add(current_point)

    return len(visited)


if __name__ == '__main__':
    print(solution('input_data.txt'))
