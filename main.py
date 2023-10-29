import pyxel
from menu import Menu
from game import Game

screenSize = (456, 576)
pyxel.init(screenSize[0], screenSize[1], title="Doodle Jump", fps=60)
pyxel.load("ressources.pyxres")

class Main:
    def __init__(self):
        self.is_in_game = False
        self.menu = Menu(screenSize)
        self.game = Game(screenSize)
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.is_in_game:
            self.game.update()
        else:
            self.menu.update()

    def draw(self):
        pyxel.cls(7)
        if self.is_in_game:
            self.game.draw()
        else:
            self.menu.draw()


Main()