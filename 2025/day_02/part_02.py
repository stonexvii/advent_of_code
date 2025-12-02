def read_data(path: str):
    with open(path, 'r') as file:
        return map(lambda x: sorted([int(x[0]), int(x[1])]),
                   (item.split('-') for item in file.read().strip().split(',')))


def check_mirror(item: int):
    item = str(item)
    item_len = len(item)
    if not item_len % 2:
        if item[:item_len // 2] == item[item_len // 2:]:
            return True
    for i in range(1, item_len // 2 + 1):
        item_slice = item[:i]
        count = item.count(item_slice)
        if count > 1 and item_slice * count == item:
            return True


def solution(path: str):
    result = 0
    for left, right in read_data(path):
        for item in range(left, right + 1):
            if check_mirror(item):
                result += item
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
