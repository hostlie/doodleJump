import pyxel
from managePlatforms import ManagePlatforms
from manageRessorts import ManageRessorts
import random
import numpy as np
import pyxel
from player import Player



screenSize = (456, 576)

pyxel.init(screenSize[0], screenSize[1], title="Doodle Jump")

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
            #print(self.platforms.platformGenerated)
            self.ressorts.generateRessorts(len(self.platforms.platformGenerated))
            print(self.ressorts.ressortsGenerated)
            self.is_generatedMap = True

        if pyxel.btnr(pyxel.KEY_SPACE):
            #self.platformGenerated[2].fall = True
            #self.platforms.up = True
            #self.platforms.animtionBreakPlatform(1)
            #platform.breakPlatorm(1)
            pass

        self.platforms.mustJump(self.player)

        if self.platforms.up and self.platforms.platformGenerated.size > 0:
            # print(fonctionVitesse)
            self.platforms.vitesse = ((self.platforms.heightJump - 20) / self.platforms.jumpEtatY + 0.2) * 10
            for plt in self.platforms.platformGenerated:
                if 1 <= self.platforms.jumpEtatY < self.platforms.heightJump:
                    plt.position[1] += self.platforms.vitesse

            self.platforms.jumpEtatY += 1



        if self.platforms.platformGenerated.size > 0:
            if self.platforms.platformGenerated.size < 30:
                self.platforms.generatePlatforms(100)

            if self.platforms.jumpEtatY > self.platforms.heightJump:
                self.platforms.up = False
                self.platforms.down = True
                self.platforms.jumpEtatY = 1
                self.platforms.vitesse = 1

        if self.platforms.down and self.platforms.platformGenerated.size > 0:
            self.platforms.vitesse += 1
            for plt in self.platforms.platformGenerated:
                if 1 <= self.platforms.jumpEtatY < self.platforms.heightJump:
                    plt.position[1] -= self.platforms.vitesse

        if self.platforms.platformGenerated.size > 0:
            if self.platforms.platformGenerated[0].position[1] < 0:
                pass #print("End")



    def draw(self):
        pyxel.cls(7)
        self.platforms.draw()
        self.player.draw()

Game()