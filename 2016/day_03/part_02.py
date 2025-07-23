def read_data(path: str):
    with open(path, 'r') as file:
        result = []
        while True:
            data = []
            for _ in range(3):
                line = list(map(int, file.readline().strip().split()))
                data.append(line)
                if not line:
                    return result
            result += list(map(lambda x: list(x), zip(*data)))



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
