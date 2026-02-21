import random


class Item:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.all = [Apple, BasicAxe, BasicGun, BasicSword]
        
        

class Food(Item):
    def __init__(self, healValue, name, rarity):
        super().__init__(name = name, rarity = rarity)
        self.healValue = healValue

    def eat(self, user):
        user.health += self.healValue
        if user.health > user.tier * 20:
            user.health = user.tier * 20
        user.inventory.remove(self)

class Apple(Food):
    def __init__(self, healValue = 2, name = 'Apple', rarity = 'common'):
        super().__init__(healValue, name, rarity = rarity)

class Weapon(Item):
    def __init__(self, damage, durability, name, rarity):
        super().__init__(name = name, rarity = rarity)
        self.damage = damage
        self.durability = durability
        
    
    def attack(self, target):
        if target.armor <= self.damage + random.randint(1,10):
            target.health -= self.damage
            target.armor -= 1
            self.durability -= 1
        else:
            pass

class Ranged(Weapon):
    def __init__(self, damage, durability, name, rarity, ammo, maxAmmo):
        super().__init__(name = name, rarity = rarity, damage = damage, durability = durability)
        self.ammo = ammo
        self.maxAmmo = maxAmmo

    def attack(self, target):
        if target.armor <= self.damage + random.randint(1,10) and self.ammo > 0 and self.ammo <= self.maxAmmo:
            target.health -= self.damage
            target.armor -= 1
            self.durability -= 1
            self.ammo -= 1
        else:
            pass



class BasicSword(Weapon):
    def __init__(self):
        super().__init__(name = 'sword', rarity = 'common', damage = 5, durability = 15)

    def attack(self, user, target):
        if user.dex + random.randint(1, 10) >= target.armour:
            target.health -= self.damage - target.armour + random.randint(1, user.str)
            target.armour -= 1
            self.durability-= 1
        else:
            pass

class BasicAxe(Weapon):
    def __init__(self):
        super().__init__(name = 'axe', rarity = 'common', damage = 10, durability = 20)

    def attack(self, user, target):
        if user.str + random.randint(1, 10) >= target.armour:
            target.health -= self.damage - target.armour + random.randint(1, user.str)
            target.armour -= 1
            self.durability-= 1
        else:
            pass

class BasicGun(Ranged):
    def __init__(self):
        super().__init__(name = 'gun', rarity = 'uncommon', damage = 20, durability = 35, ammo = random.randint(1, 14), maxAmmo = 14)

    def attack(self, user, target):
        if user.dex + 2 + random.randint(1, 10) >= target.armour:
            target.health -= self.damage - target.armour + random.randint(1, user.dex)
            target.armour -= 1
            self.durability-= 1
            self.ammo -= 1
        else:
            pass

class all_items:
    def __init__(self):
        self.items = [BasicSword(), BasicAxe(), BasicGun(), Apple()]
        self.weapons = [BasicSword(), BasicAxe(), BasicGun()]
        self.non_weapon_items = [Apple()]
all = all_items()