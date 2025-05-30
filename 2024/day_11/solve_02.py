from datetime import datetime
from functools import cache

def read_data(path: str):
    with open(path, 'r') as file:
        return file.read().strip().split()


@cache
def calculate_stone(slot: str | int, depth: int, count_blinks: int):
    if slot == '0':
        data = ['1']
    elif not len(slot) % 2:
        len_stone = len(slot) // 2
        l_stone, r_stone = slot[:len_stone], slot[len_stone:]
        data = [l_stone, str(int(r_stone))]
    else:
        data = [str(int(slot) * 2024)]
    if depth < count_blinks:
        result = 0
        for slot in data:
            result += calculate_stone(slot, depth + 1, count_blinks)
        # print(result)
        return result
    else:
        return len(data)


def solution(path: str, blink_count: int):
    stones = read_data(path)
    max_len_stone = len(max(stones, key=len))
    # print(f'Камни: {stones}')
    total_stones = 0
    start_time = datetime.now()
    for stone in stones:
        current_start_time = datetime.now()
        total_stones += calculate_stone(stone, 1, blink_count)
        current_finish_time = datetime.now()
        print(f'Камень {stone:>{max_len_stone}}: {str(current_finish_time - current_start_time)}')
    finish_time = datetime.now()
    print(f'Время затраченное на все камни: {finish_time - start_time}')
    return total_stones


blinks = 75
print(f'Всего камней после {blinks} морганий: {solution('input_data.txt', blinks)}')
