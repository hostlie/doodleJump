import math
from managePlatforms import ManagePlatforms
from manageRessorts import ManageRessorts
from manageJetpacks import ManageJetpacks
from player import Player
import random
import pyxel


screenSize = (456, 576)

pyxel.init(screenSize[0], screenSize[1], title="Doodle Jump", fps=60)

pyxel.load("ressources.pyxres")


class Game:
    def __init__(self):
        self.platformFall = []
        self.is_generatedMap = False
        self.platforms = ManagePlatforms(screenSize)
        self.ressorts = ManageRessorts()
        self.jetpacks = ManageJetpacks()
        self.player = Player(screenSize)

        pyxel.run(self.update, self.draw)





    def update(self):

        self.player.moves()

        if not self.is_generatedMap:
            self.platforms.generatePlatforms(100)
            self.ressorts.generateRessorts(self.platforms.platformGenerated)
            self.platforms.putItem(self.ressorts.ressortsGenerated)
            self.jetpacks.generateJetpacks(self.platforms.platformGenerated)
            print(self.jetpacks.jetpacksGenerated)



            print(self.platforms.platformGenerated)

            print(self.ressorts.ressortsGenerated)
            self.is_generatedMap = True

        if pyxel.btnr(pyxel.KEY_SPACE):
            self.platforms.up = False
            self.platforms.down = False


        self.platforms.mustJump(self.player)
        self.platforms.update()

        if self.platforms.platformGenerated[0][0].position[1] < 0:
            pass#print("End")





    def draw(self):
        pyxel.cls(7)
        self.platforms.draw()
        self.ressorts.draw(self.platforms.platformGenerated)
        self.player.draw()

Game()