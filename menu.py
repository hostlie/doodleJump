import pyxel

class Menu:
    def __init__(self, screenSize):
        self.screenSize = screenSize
        self.mx = pyxel.mouse_x
        self.my = pyxel.mouse_y

    def update(self):
        pyxel.mouse(True)
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pass

    def draw(self):
        pyxel.blt(self.screenSize[0] // 2 - 56, self.screenSize[1] // 2 - 24,
                  2, 0, 0, 112, 48)