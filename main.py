import entity, items
from map import map1

def save():
    saveData = f'map1 = {map1}; player = {player}'
    with open('save.txt', 'w') as file:
        file.write(saveData)
        file.close()

def load():
    with open('save.txt', 'r') as file:
        exec(file.read())
        file.close()


class Player(entity.Entity):
    def __init__(self):
        super().__init__(5, 0 ,0)

    def check_coords(self):
        if self.x < 0:
            self.x = 0
        if self.y <0:
            self.y = 0

    def move(self, direction):
        if direction == 'up' and map1.check_up(self):
            self.y -= 1
        elif direction == 'down' and map1.check_down(self):
            self.y += 1
        elif direction == 'left' and map1.check_left(self):
            self.x -= 1
        elif direction == 'right' and map1.check_right(self):
            self.x += 1
        self.check_coords()

    def pick_up(self, item):
        item_moved = (object if object.name == item else None for object in items.weapon1.all)
        print(map1.main[self.y][self.x])
        map1.main[self.y][self.x].items.remove(item)
        self.inventory.append(item_moved)

    def drop(self, item):
        item_moved = (object if object.name == item else None for object in items.weapon1.all)
        self.inventory.remove(item_moved)
        map1.main[self.y][self.x].items.append(item)


player =  Player()
game = True

try:
    load()
except FileNotFoundError:
    pass

while game:
    nearbyEntities = [entity.name for entity in map1.main[player.y][player.x][0].entities]
    nearbyItems = [item.name for item in map1.main[player.y][player.x][0].items]


    print(f'you can see a {map1.main[player.y][player.x][0].name}, there is a {nearbyEntities} and on the floor you see {nearbyItems}.')

    cmd = input('what do you do > > > ')
    cmd = cmd.split()
    
    if cmd[0] == 'move':
        if cmd[1] == 'up':
            player.move('up')
        if cmd[1] == 'down':
            player.move('down')
        if cmd[1] == 'left':
            player.move('left')
        if cmd[1] == 'right':
            player.move('right')

    elif cmd[0] == 'save':
        save()

    elif cmd[0] == 'leave':
        save()
        game = False

    elif cmd[0] == 'map':
        map1.draw()
    
    elif cmd[0] == 'pick' and cmd[1] == 'up':
        player.pick_up(cmd[2])