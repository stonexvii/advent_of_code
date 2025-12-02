def read_data(path: str):
    with open(path, 'r') as file:
        while line := file.readline():
            yield line[0], int(line[1:])


def solution(path: str):
    result = 0
    number = 50
    for direct, amount in read_data(path):
        for _ in range(amount):
            number = ((number + 1) if direct == 'R' else (number - 1)) % 100
            if not number:
                result += 1
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
