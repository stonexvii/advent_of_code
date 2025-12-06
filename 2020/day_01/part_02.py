def read_data(path: str):
    with open(path, 'r') as file:
        return {int(line.strip()) for line in file.readlines()}


def solution(path: str):
    numbers = read_data(path)
    for number in numbers:
        for other_number in numbers:
            if 2020 - number - other_number in numbers:
                return number * other_number * (2020 - number - other_number)


if __name__ == '__main__':
    print(solution('input_data.txt'))
