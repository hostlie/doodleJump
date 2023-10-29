import pyxel

class Ressort:
    def __init__(self):
        self.position = [0, 0]
        self.hitbox = (32, 32)
        self.jumpHeight = 5
        self.posInLstPlt = None
        self.mustAnim = False
        self.animState = 0
        self.animFrame = 0
        self.timeAnim = 0
        self.animEnd = False

    def anim(self):
        self.animFrame = (self.animState % 3) * 32
        if self.animState == 2:
            self.animEnd = True

        if self.animEnd and self.animState == 0:
            self.mustAnim = False

        if self.animEnd:
            self.animState -= 1
        else:
            self.animState += 1
        self.timeAnim = 0.1

    def draw(self):
        if self.mustAnim:
            self.timeAnim -= 0.1
            if self.timeAnim <= 0:
                self.anim()
        pyxel.blt(self.position[0], self.position[1], img=0, u=self.animFrame, v=128, w=32, h=32, colkey=7)
