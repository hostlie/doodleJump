import pyxel

class Player:
    def __init__(self, screenSize):
        self.screenSize = screenSize
        self.x = self.screenSize[0] // 2 - 14
        self.y = 300
        self.speed = 13

    def moves(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.x < (0 - 27):
                self.x = self.screenSize[0]
            self.x -= self.speed
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.x > (self.screenSize[0] - 7):
                self.x = 0 - 21
            self.x += self.speed


    def draw(self):
        pyxel.rect(self.x, self.y, 28, 28, 10)