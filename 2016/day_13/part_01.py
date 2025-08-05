def read_data(path: str):
    with open(path, 'r') as file:
        pass


def solution(path: str):
    for x in range(10):
        for y in range(10):
            print('.' if sum(map(int, bin(x * x + 3 * x + 2 * x * y + y + y * y)[2:])) % 2 else '#', end='')
        print()


if __name__ == '__main__':
    solution('f')
