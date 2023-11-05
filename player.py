import pyxel

class Player:
    def __init__(self, screenSize):
        self.screenSize = screenSize
        self.x = self.screenSize[0] // 2 - 14
        self.y = 300
        self.hitbox = [37, 48]
        self.speed = 7
        self.leftPress = False

    def moves(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.x < (-27):
                self.x = self.screenSize[0]
            self.x -= self.speed
            self.leftPress = True

        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.x > (self.screenSize[0] - 7):
                self.x = -21
            self.x += self.speed
            self.leftPress = False


    def update(self):
        self.moves()


    def draw(self):
        if self.leftPress:
            pyxel.blt(self.x, self.y, 1, u=0, v=0, w=48, h=48, colkey=7)
        else:
            pyxel.blt(self.x, self.y, 1, u=0, v=0, w=-48, h=48, colkey=7)