def read_data(path: str):
    with open(path, 'r') as file:
        *rules, _, data = [line.strip().split(' => ') if '=>' in line else line.strip() for line in file.readlines()]
    print(rules, data)


if __name__ == '__main__':
    read_data('test_data.txt')