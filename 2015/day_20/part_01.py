from functools import lru_cache


@lru_cache()
def calculation_of_divisors(number: int):
    divisors = {number}
    for div in range(1, number // 2 + 1):
        if not number % div:
            divisors.add(div)
    return divisors


def solution(target_presents: int):
    for i in range(2, target_presents):
        houses = [1, i]
        presents = i
        while presents < target_presents:
            presents += i
            houses.append(presents)
        print(houses)
        if sum(houses) == target_presents:

            return 'Solve'


if __name__ == '__main__':
    print(solution(15))
