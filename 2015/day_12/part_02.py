def read_data(path: str):
    with open(path, 'r') as file:
        return file.read().strip()


result = []


def rec_walk(row):
    global result
    if isinstance(row, dict):
        for value in row.values():
            if isinstance(value, list):
                rec_walk(value)
            elif isinstance(value, dict):
                if 'red' not in value.values():
                    rec_walk(value)
            elif isinstance(value, int):
                result.append(value)
    elif isinstance(row, list):
        for item in row:
            if isinstance(item, int):
                result.append(item)
            elif isinstance(item, list):
                rec_walk(item)
            elif isinstance(item, dict):
                if 'red' not in item.values():
                    rec_walk(item)


def solution(path: str):
    data = eval(read_data(path))

    rec_walk(data)
    print(sum(result))


if __name__ == '__main__':
    solution('input_data.txt')
