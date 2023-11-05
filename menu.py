import pyxel

class Menu:
    def __init__(self, screenSize, is_first_game):
        self.screenSize = screenSize
        self.is_first_game = is_first_game
        self.mx = pyxel.mouse_x
        self.my = pyxel.mouse_y
        pyxel.mouse(True)

    def update(self):
        # Checks if the player clicks on the button, in which case the game is launched.
        if (self.screenSize[0] // 2 - 56 <= pyxel.mouse_x <= self.screenSize[0] // 2 + 56)\
           and (self.screenSize[1] // 2 - 24 <= pyxel.mouse_y <= self.screenSize[1] // 2 + 24)\
           and pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            return True
        else:
            return False

    def draw(self):
        # Displays "Play" button if it is the first game, "Retry" button otherwise.
        if not self.is_first_game:
            pyxel.blt(self.screenSize[0] // 2 - 56, self.screenSize[1] // 2 - 24,
                      2, 0, 48, 112, 48, colkey=7)
        else:
            pyxel.blt(self.screenSize[0] // 2 - 56, self.screenSize[1] // 2 - 24,
                      2, 0, 0, 112, 48, colkey=7)