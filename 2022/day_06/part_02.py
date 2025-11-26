AMOUNT = 14


def read_data(path: str):
    with open(path, 'r') as file:
        return file.read()


def solution(path: str):
    data = read_data(path)
    for i in range(len(data) - AMOUNT):
        if len(set(data[i:i + AMOUNT])) == AMOUNT:
            return i + AMOUNT


if __name__ == '__main__':
    print(solution('input_data.txt'))
