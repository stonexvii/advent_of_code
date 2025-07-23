from collections import Counter


def read_data(path: str):
    with open(path, 'r') as file:
        return list(map(lambda x: x.strip(), file))


def solution(path: str):
    messages = [Counter(message).most_common() for message in zip(*read_data(path))]
    result = ''
    for message in messages:
        result += sorted(message, key=lambda x: x[1])[0][0]
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
