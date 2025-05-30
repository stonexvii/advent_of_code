def read_data(path: str):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.read().replace('\n', '')
    return data


def solution(path: str):
    data = read_data(path)
    return data.count('(') - data.count(')')


print(solution('input_data.txt'))
