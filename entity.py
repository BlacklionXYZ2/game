import random, items


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
        self.health = random.randint((tier - 1) * 20, tier * 20)
        self.all = [Skeleton, Zombie]



class Enemy(Entity):
    def __init__(self, tier, x, y):
        super().__init__(tier, x, y)
        self.inventory.append(random.choice(items.weapon1.all))

class Skeleton(Enemy):
    def __init__(self, x, y, name = 'skeleton', tier = 1):
        super().__init__(tier, x, y)
        self.name = name

class Zombie(Enemy):
    def __init__(self, x, y, name = 'zombie', tier = 1):
        super().__init__(tier, x, y)
        self.name = name
        
entity1 = Entity(1, 0, 0)