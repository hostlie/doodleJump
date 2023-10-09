import pyxel
from managePlatforms import ManagePlatforms
from manageRessorts import ManageRessorts
import random
import numpy as np
import pyxel
from player import Player



screenSize = (456, 576)

pyxel.init(screenSize[0], screenSize[1], title="Doodle Jump", fps=60)

pyxel.load("ressources.pyxres")


class Game:
    def __init__(self):
        self.platformFall = []
        self.is_generatedMap = False
        self.platforms = ManagePlatforms(screenSize)
        self.ressorts = ManageRessorts()
        self.player = Player(screenSize)

        pyxel.run(self.update, self.draw)





    def update(self):

        self.player.moves()

        if not self.is_generatedMap:
            self.platforms.generatePlatforms(100)
            self.ressorts.generateRessorts(self.platforms.platformGenerated)
            self.platforms.putItem(self.ressorts.ressortsGenerated)


            print(self.platforms.platformGenerated)

            print(self.ressorts.ressortsGenerated)
            self.is_generatedMap = True

        if pyxel.btnr(pyxel.KEY_SPACE):
            self.platforms.up = False
            self.platforms.down = False


        self.platforms.mustJump(self.player)

        if self.platforms.up and len(self.platforms.platformGenerated) > 0:
            # print(fonctionVitesse)
            self.platforms.vitesse += self.platforms.heightJump / self.platforms.jumpEtatY - self.platforms.vitesse
            print(self.platforms.vitesse)
            for plt, item in self.platforms.platformGenerated:
                if 1 <= self.platforms.jumpEtatY < self.platforms.heightJump:
                    plt.position[1] += self.platforms.vitesse

                if plt.position[1] - 52 > screenSize[1]:
                    self.platforms.platformGenerated.remove([plt, item])
                    #self.platforms.platformGenerated = [plt, item for plt, item in self.platforms.platformGenerated]



            self.platforms.jumpEtatY += 1



            """if len(self.platforms.platformGenerated) < 30:
                self.platforms.generatePlatforms(100)"""

            if self.platforms.jumpEtatY > self.platforms.heightJump:
                self.platforms.up = False
                self.platforms.down = True
                self.platforms.jumpEtatY = 1
                self.platforms.vitesse = 1

        if self.platforms.down and len(self.platforms.platformGenerated) > 0:
            self.platforms.vitesse += 0.3
            for plt in self.platforms.platformGenerated:
                if 1 <= self.platforms.jumpEtatY < self.platforms.heightJump:
                    plt[0].position[1] -= self.platforms.vitesse

        if self.platforms.platformGenerated[0][0].position[1] < 0:
            print("End")





    def draw(self):
        pyxel.cls(7)
        self.platforms.draw()
        self.ressorts.draw(self.platforms.platformGenerated)
        self.player.draw()

Game()