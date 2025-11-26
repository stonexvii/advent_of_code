MAX_CAPACITY = 100_000


def read_data(path: str):
    def create_dir_path(data: dict, dir_list: list[str]):
        full_path = data
        for item in dir_list:
            full_path = full_path[item]
        return full_path

    files = {}
    dir_path = []
    current_dir = create_dir_path(files, dir_path)
    with open(path, 'r') as file:
        file.readline()
        while line := file.readline().strip():
            if line.startswith('$'):
                _, command = line.split(' ', 1)
                if command != 'ls':
                    _, dir_name = command.split()
                    if dir_name != '..':
                        dir_path.append(dir_name)
                    else:
                        dir_path.pop()
                    current_dir = create_dir_path(files, dir_path)

            else:
                first, second = line.split()
                if first.isdigit():
                    size = int(first)
                    file_name = second
                    current_dir[file_name] = size
                else:
                    current_dir[second] = {}
    return files


def solution(path: str):
    files_data = read_data(path)
    dir_list = []
    result = 0

    def walk(dir_name: str, directory: dict):
        current_dir_size = 0
        for key, value in directory.items():
            if isinstance(value, int):
                current_dir_size += value
            else:
                current_dir_size += walk(key, value)
        dir_list.append(current_dir_size)
        return current_dir_size

    walk('..', files_data)

    for dir_size in dir_list:
        if dir_size < MAX_CAPACITY:
            result += dir_size
    return result


if __name__ == '__main__':
    print(solution('input_data.txt'))
