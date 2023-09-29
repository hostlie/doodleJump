import pyxel

class Player:
    def __init__(self):
        self.x = 160 - 14
        self.speed = 13

    def moves(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.x < (0 - 27):
                self.x = 320
            self.x -= self.speed
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.x > (320 - 7):
                self.x = 0 - 21
            self.x += self.speed


    def draw(self):
        pyxel.rect(self.x, 300, 28, 28, 10)