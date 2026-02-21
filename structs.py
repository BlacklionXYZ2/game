import random, entity, items

class Structure:
    def __init__(self, name, x, y, encounterCoeff):
        self.name = name
        self.x = x
        self.y = y
        self.entities = []
        self.items = []
        self.encounterCoefficient = encounterCoeff

    def add_entities(self, entity):
        if type(entity) == list:
            for x in entity:
                self.entities.append(x)
        else:
            self.entities.append(entity)

    def add_items(self, item):
        if type(item) == list:
            for x in item:
                self.items.append(x)
        else:
            self.items.append(item)

    def spawn_entities(self, encounterCoeff):
        if random.randint(1, 10) / 10 >= encounterCoeff:
            ent = random.choice(entity.all.enemies)(random.randint(1, 2), self.x, self.y)
            self.add_entities(ent)

    def spawn_items(self, encounterCoeff):
        if random.randint(1, 10) / 10 >= encounterCoeff:
            item = random.choice(items.all.items)
            self.add_items(item)


class Pond(Structure):
    def __init__(self, x, y, encounterCoeff = 0.5):
        super().__init__(name = 'Pond', x = x, y = y, encounterCoeff = encounterCoeff)
        self.spawn_entities(encounterCoeff)
        self.spawn_items(encounterCoeff)

class Meadow(Structure):
    def __init__(self, x, y, encounterCoeff = 0.5):
        super().__init__(name = 'Meadow', x = x, y = y, encounterCoeff = encounterCoeff)
        self.spawn_entities(encounterCoeff)
        self.spawn_items(encounterCoeff)

class Field(Structure):
    def __init__(self, x, y, encounterCoeff = 0.3):
        super().__init__(name = 'Field', x = x, y = y, encounterCoeff = encounterCoeff)
        self.spawn_entities(encounterCoeff)
        self.spawn_items(encounterCoeff)

class Plains(Structure):
    def __init__(self, x, y, encounterCoeff = 0.7):
        super().__init__(name = 'Plains', x = x, y = y, encounterCoeff = encounterCoeff)
        self.spawn_entities(encounterCoeff)
        self.spawn_items(encounterCoeff)

class all_structs:
    def __init__(self):
        self.structs = [Pond, Meadow, Field, Plains]
all = all_structs()