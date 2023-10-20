import pyxel

class Jetpack:
    def __init__(self):
        self.position = [0, 0]
        self.jumpHeight = 100
        self.posInLstPlt = None

    def draw(self):
        pyxel.rect(self.position[0], self.position[1], 48, 48, 2)