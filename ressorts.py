import pyxel

class Ressort:
    def __init__(self):
        self.position = [0, 0]
        self.jumpHeight = 40
        self.posInLstPlt = None

    def draw(self):
        pyxel.blt(self.position[0], self.position[1], img=0, u=64, v=128, w=32, h=32, colkey=7)
