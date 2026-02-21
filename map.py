import random
import structs as s, items as i


class Map:
    def __init__(self):
        self.main = [[[s.Pond(0, 0)]]]

    def draw(self):
        structs_in_row = [struct[0].name for row in self.main for struct in row]
        print(structs_in_row)


    def gen_row(self, up, coord):
        ref = []
        for col in self.main[0]:
            ref.append([random.choice(s.structure1.all)(coord[0], coord[1])])
        if up:
            self.main.insert(0, ref)
        else:
            self.main.append(ref)

    def gen_col(self, right, coord):
        for col in range(len(self.main)):
            if right:
                self.main[col].append([random.choice(s.structure1.all)(coord[0], coord[1])])
            else:
                self.main[col].insert(0, [random.choice(s.structure1.all)(coord[0], coord[1])])

           

    def check_up(self, entity):
        if entity.y == 0:
            self.gen_row(True, (entity.x, 0))
        return True

    def check_down(self, entity):
        if entity.y == len(self.main) - 1:
            self.gen_row(False, (entity.x, entity.y + 1))
        return True

    def check_left(self, entity):
        if entity.x == 0:
            self.gen_col(False, (0, entity.y))
        return True

    def check_right(self, entity):
        if entity.x == len(self.main[0]) - 1:
            self.gen_col(True, (entity.x + 1, entity.y))
        return True



map1 = Map()