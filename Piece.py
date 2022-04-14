# representing a piece as a tuple of colors on each axis (cx, cy, cz)

class Piece:
    def __init__(self, cx, cy, cz):
        self.colors = [cx, cy, cz]

    #     self.str_colors = self.parse()
    #
    # def parse(self):
    #     res = ['','','']
    #     for i in range(3):
    #         res[i] = self.to_color(self.colors[i])
    #     return res

    def xSwap(self):
        self.colors[0], self.colors[2] = self.colors[2], self.colors[0]

    def ySwap(self):
        self.colors[0], self.colors[1] = self.colors[1], self.colors[0]

    def zSwap(self):
        self.colors[1], self.colors[2] = self.colors[2], self.colors[1]

    def __str__(self):
        return f'[{self.to_color(self.colors[0])} {self.to_color(self.colors[1])} {self.to_color(self.colors[2])}]'

    @classmethod
    def to_color(self, c):
        match c:
            case 0:
                return 'W'
            case 1:
                return 'G'
            case 2:
                return 'O'
            case 3:
                return 'B'
            case 4:
                return 'R'
            case 5:
                return 'Y'
            case _:
                return '_'
