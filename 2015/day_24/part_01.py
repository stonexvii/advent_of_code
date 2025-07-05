def read_data(path: str):
    with open(path, 'r') as file:
        return [int(line.strip()) for line in file]


def solution(path: str):
    print(read_data(path))


if __name__ == '__main__':
    solution('test_data.txt')
