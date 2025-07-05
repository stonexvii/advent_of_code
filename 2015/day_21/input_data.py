from collections import namedtuple

Item = namedtuple('Item', ['price', 'damage', 'armor'])

weapons = {
    'Dagger': Item(8, 4, 0),
    'Shortsword': Item(10, 5, 0),
    'Warhammer': Item(25, 6, 0),
    'Longsword': Item(40, 7, 0),
    'Greataxe': Item(74, 8, 0),
}
armors = {
    'No armor': Item(0, 0, 0),
    'Leather': Item(13, 0, 1),
    'Chainmail': Item(31, 0, 2),
    'Splintmail': Item(53, 0, 3),
    'Bandedmail': Item(75, 0, 4),
    'Platemail': Item(102, 0, 5),
}
rings = {
    'No ring': Item(0, 0, 0),
    'Damage +1': Item(25, 1, 0),
    'Damage +2': Item(50, 2, 0),
    'Damage +3': Item(100, 3, 0),
    'Defense +1': Item(20, 0, 1),
    'Defense +2': Item(40, 0, 2),
    'Defense +3': Item(80, 0, 3),
}


class Unit:
    def __init__(self, name: str, hp: int, damage: int, armor: int):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def equip(self, items: tuple[Item, Item, Item, Item]):
        for item in items:
            self.armor += item.armor
            self.damage += item.damage

    def defense(self, other: 'Unit'):
        attack = other.damage - self.armor
        attack = attack if attack > 0 else 1
        self.hp -= attack


player_base = {
    'hp': 100,
    'damage': 0,
    'armor': 0,
}

enemy_base = {
    'hp': 109,
    'damage': 8,
    'armor': 2,
}
