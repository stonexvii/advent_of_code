from functools import lru_cache


@lru_cache()
def calculation_of_divisors(number: int):
    divisors = {number}
    for div in range(1, number // 2 + 1):
        if not number % div:
            divisors.add(div)
    return divisors


def solution(target_presents: int):
    target = target_presents // 10
    house_number = 1
    while True:
        divisors = calculation_of_divisors(house_number)
        print(house_number, divisors)
        if sum(divisors) == target:
            return house_number
        house_number += 1


if __name__ == '__main__':
    print(solution(29000000))
