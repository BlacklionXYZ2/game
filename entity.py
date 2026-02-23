import random, items
from map import map1


class Entity:
    def __init__(self, tier, x, y):
        self.tier = tier
        self.x = x
        self.y = y
        self.str = random.randint(1, 10)
        self.int = random.randint(1, 10)
        self.wis = random.randint(1, 10)
        self.con = random.randint(1, 10)
        self.chr = random.randint(1, 10)
        self.dex = random.randint(1, 10)
        self.armor = random.randint(1, 10)
        self.inventory = []
        self.max_health = random.randint((tier - 1) * 20, tier * 20)
        self.health = self.max_health
        self.max_mana = random.randint((tier - 1) * 10, tier * 10)
        self.mana = self.max_mana

    def show_inventory(self):
        show_inv = []
        for item in self.inventory:
            show_inv.append(item.name)
        print(show_inv)

    def show_entity(self):
        print(f'Position: ({self.x}, {self.y})')
        print(f'Biome: {map1.main[self.y][self.x][0].name}')
        print('')
        print('Stats:')
        print(f'     Strength: {self.str}  Dexterity: {self.dex}')
        print(f'     Intelligence: {self.int}  Wisdom: {self.wis}')
        print(f'     Charisma: {self.cha}  Constitution: {self.con}')
        print('')
        self.show_inventory()
        print('')
        print(f'Armour: {self.armor}')
        print(f'Health: {self.health}/{self.max_health}')
        print(f'Mana: {self.mana}/{self.max_mana}')

    def show_necessary(self):
        print('')
        print(f'Armour: {self.armor}')
        print(f'Health: {self.health}/{self.max_health}')
        print(f'Mana: {self.mana}/{self.max_mana}')


class Enemy(Entity):
    def __init__(self, tier, x, y):
        super().__init__(tier, x, y)
        self.inventory.append(random.choice(items.all.weapons))

class Skeleton(Enemy):
    def __init__(self, x, y, name = 'skeleton', tier = 1):
        super().__init__(tier, x, y)
        self.name = name

class Zombie(Enemy):
    def __init__(self, x, y, name = 'zombie', tier = 1):
        super().__init__(tier, x, y)
        self.name = name
        
class all_entities:
    def __init__(self):
        self.enemies = [Skeleton, Zombie]
all = all_entities()