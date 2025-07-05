from input_data import *


def fight(player: Unit, enemy: Unit):
    attack_unit = player
    defense_unit = enemy
    while defense_unit.hp > 0:
        defense_unit.defense(attack_unit)
        attack_unit, defense_unit = defense_unit, attack_unit
    return defense_unit.name


def solution():
    prices = []
    for weapon in weapons.values():
        for armor in armors.values():
            for left_ring in rings.values():
                for right_ring in rings.values():
                    if left_ring != right_ring:
                        player = Unit(name='player', **player_base)
                        enemy = Unit(name='enemy', **enemy_base)
                        items = (weapon, armor, left_ring, right_ring)
                        player.equip(items)
                        result = fight(player, enemy)
                        if result == 'player':
                            prices.append(sum([item.price for item in items]))
    return max(prices)


if __name__ == '__main__':
    print(solution())
