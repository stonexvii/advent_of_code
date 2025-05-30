import itertools


def create_map(file_path: str) -> tuple[set, dict[str, dict[str, int]]]:
    data_map = {}
    point_set = set()
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file:
            path, distance = line.strip().split(' = ')
            from_point, to_point = path.split(' to ')
            point_set.update({from_point, to_point})
            data_map.setdefault(from_point, {})
            data_map.setdefault(to_point, {})
            data_map[from_point][to_point] = int(distance)
            data_map[to_point][from_point] = int(distance)

    return point_set, data_map


def solution(file_path: str) -> int:
    point_list, data_map = create_map(file_path)
    routes = list(itertools.permutations(point_list, len(point_list)))
    max_distance = 0
    for route in routes:
        current_distance = 0
        for idx in range(len(route) - 1):
            current_distance += data_map[route[idx]][route[idx + 1]]
        if current_distance > max_distance:
            max_distance = current_distance
    return max_distance


if __name__ == '__main__':
    print(solution('input_data.txt'))
