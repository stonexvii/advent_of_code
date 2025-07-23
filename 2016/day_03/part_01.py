def read_data(path: str):
    with open(path, 'r') as file:
        return [list(map(int, line.strip().split())) for line in file.readlines()]


def solution(path: str):
    triangles = read_data(path)
    count = 0
    for triangle in triangles:
        max_side = max(triangle)
        triangle.remove(max_side)
        if sum(triangle) > max_side:
            count += 1
    return count


if __name__ == '__main__':
    print(solution('input_data.txt'))
