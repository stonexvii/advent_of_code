class Ingredient:

    def __init__(self, data: str):
        data = data.strip().split(': ')[-1]
        values = list(map(lambda x: int(x[1]), data.split(', ')))


    # def value(self, multiply: int):
    #     return self.capacity * multiply + self.durability * multiply + self.flavor * multiply
    #
    # def __repr__(self):
    #     return f'C={self.capacity} D={self.durability} F={self.flavor} T={self.texture} CAL={self.calories}'


class Cookie:
    INGREDIENTS = []

    @classmethod
    def init_ingredients(cls, list_ingredients: list[str]):
        for ingredient in list_ingredients:
            cls.INGREDIENTS.append(Ingredient(ingredient))

    def __init__(self, *args):
        for ingredient in self.INGREDIENTS:
            for amount in args:
                ingredient



    def quality(self, *args):
        total = 0
        for idx in range(len(args)):
            value = self.ingredients[idx]*args[idx]
            if value > 0:

            self.capacity += i * ingredient.capacity
            self.durability += i * ingredient.durability
            self.flavor += i * ingredient.flavor
            self.texture += i * ingredient.texture
        if self.capacity > 0 and self.durability > 0 and self.flavor > 0 and self.texture > 0:
            return self.capacity * self.durability * self.flavor * self.texture
        return 0


def read_data(path: str) -> list[str]:
    with open(path, 'r') as file:
        return file.readlines()


def solution(path: str):
    Cookie.init_ingredients(read_data(path))
    best_results = 0
    cookie = read_data(path)
    # for a in range(100):
    #     for b in range(100 - a):
    #         for c in range(100 - b - a):

    for a in range(100):
        ready_cookie = cookie.quality(a, 100 - a)
        if ready_cookie > best_results:
            best_results = ready_cookie
    return best_results


if __name__ == '__main__':
    # for item in read_data('input_data.txt'):
    #     print(item)
    print(solution('test_data.txt'))
