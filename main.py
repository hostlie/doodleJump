import pyxel
from menu import Menu
from game import Game

screenSize = (456, 576)
pyxel.init(screenSize[0], screenSize[1], title="Doodle Jump", fps=60)
pyxel.load("ressources.pyxres")

class Main:
    def __init__(self):
        """
        is_in_game          False: Menu is displayed
                            True: Game is displayed
        menu_instantiated   Helps avoiding instantiation loop
        game_instantiated   Helps avoiding instantiation loop
        is_first_game       Helps choosing between "Play" and "Retry" buttons
        """
        self.is_in_game = False
        self.menu_instantiated = False
        self.game_instantiated = False
        self.is_first_game = True
        self.menu = Menu(screenSize, self.is_first_game)
        self.game = Game(screenSize)
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.is_in_game:
            self.game_instantiated = False
            if self.menu_instantiated:
                self.is_in_game = self.menu.update()
            else:
                self.menu = Menu(screenSize, self.is_first_game)
                self.menu_instantiated = True
        else:
            self.menu_instantiated = False
            self.is_first_game = False
            if self.game_instantiated:
                self.is_in_game = self.game.update()
            else:
                self.game = self.game = Game(screenSize)
                self.game_instantiated = True

    def draw(self):
        pyxel.cls(7)
        if not self.is_in_game:
            self.menu.draw()
        else:
            self.game.draw()

Main()