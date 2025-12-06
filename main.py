import os

solution_file = '''
def read_data(path: str):
    with open(path, 'r') as file:
        pass

def solution(path: str):
    pass


if __name__ == '__main__':
    solution()
'''


def create_file(path: str):
    data = solution_file if path.endswith('.py') else ''
    with open(path, 'w') as file:
        file.write(data)


def create_files(work_dir):
    work_dir = str(work_dir)
    if not os.path.exists(work_dir):
        os.mkdir(work_dir)
        for num in range(1, 26):
            dir_name = f'day_{str(num).zfill(2)}'
            path = os.path.join(work_dir, dir_name)
            if not os.path.exists(path):
                os.mkdir(path)
                files = [
                    'part_01.py',
                    'part_02.py',
                    'input_data.txt',
                    'test_data.txt',
                ]
                files = map(lambda x: os.path.join(path, x), files)
                for file in files:
                    create_file(file)
        print('Done!')
    else:
        print('Directory already exists')


if __name__ == '__main__':
    create_files(2020)
