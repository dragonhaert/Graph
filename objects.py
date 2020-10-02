from gui import window
from vector import *


class OBJECT:
    def __init__(self, x, y):
        self.position = VECTOR(x, y)

    def show(self):
        pass


class GRAPH(OBJECT):
    def __init__(self, x, y):
        super().__init__(x, y)

    def point(self, x, y, c='black'):
        window.ellipse(self.position.X + x, self.position.Y - y, 3, 3, color=c)

    def seg(self, x1, y1, x2, y2, c='black', width=1):
        window.line(self.position.X + x1, (self.position.Y - y1),
                    self.position.X + x2, (self.position.Y - y2), color=c, width=width)

    def show(self):
        window.line(self.position.X, 0, self.position.X, window.height, width=1)
        window.line(0, self.position.Y, window.width, self.position.Y, width=1)
