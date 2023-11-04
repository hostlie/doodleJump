import pyxel

class Jetpack:
    def __init__(self):
        self.position = [0, 0]
        self.hitbox = (24, 36)
        self.jumpHeight = 25
        self.posInLstPlt = None
        self.active = False
        self.type = 1


    def draw(self, rotationRJetpack=False):
        if self.active:
            if rotationRJetpack:
                pyxel.blt(self.position[0], self.position[1], 0, u=0, v=160, w=12, h=43)
            else:
                pyxel.blt(self.position[0], self.position[1], 0, u=0, v=160, w=-12, h=43)
        else:
            pyxel.blt(self.position[0], self.position[1], 0, u=16, v=160, w=24, h=36)
