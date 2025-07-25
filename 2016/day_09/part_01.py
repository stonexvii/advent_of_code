def read_data(path: str):
    with open(path, 'r') as file:
        return file.read()


def split_marker(item: str):
    return tuple(map(int, item.split('x')))


def solution(path: str):
    data = read_data(path)
    uncompressed = ''
    i = 0
    while i < len(data):
        print(uncompressed[-80:], data[i], i)
        if data[i] != '(':
            uncompressed += data[i]
            i += 1
        else:
            idx_closed = data.index(')', i)
            slc, cnt = split_marker(data[i + 1:idx_closed])
            next_idx = idx_closed + 1
            uncompressed += data[next_idx:next_idx + slc] * cnt
            i = next_idx + slc
    return len(uncompressed)


if __name__ == '__main__':
    print(solution('input_data.txt'))
