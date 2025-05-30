def read_data(path: str):
    with open(path, 'r') as file:
        return file.read().strip()


def solution(path: str):
    data = read_data(path)
    print(data)
    result = []
    number = ''
    for i in data:

        if i.isdigit() or (not number and i == '-'):
            number += i
        else:
            result.append(int(number) if number else 0)
            number = ''
    return sum(result)


if __name__ == '__main__':
    print(solution('input_data.txt'))
