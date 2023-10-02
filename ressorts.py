import pyxel

class Ressort:
    def _init__(self):
        self.position = [0, 0]
        self.jumpHeight = 40

    def draw(self):
        pyxel.blt(self.position[0], self.position[1], img=2, u=0, v=0, w=16, h=16, colkey=7)
