import pyxel
from platforms import Platform
from managePlatforms import ManagePlatforms
import random
import numpy as np

screenSize = (456, 576)

pyxel.init(screenSize[0], screenSize[1], title="Doodle Jump")



class Game:
    def __init__(self):
        self.platformFall = []
        self.movePlatform = False
        self.is_generatedMap = False
        self.platforms = ManagePlatforms(screenSize)


        pyxel.run(self.update, self.draw)





    def update(self):
        if not self.is_generatedMap:
            self.platforms.generatePlatforms(50)
            #print(len(self.platformGenerated), self.platformGenerated)
            self.is_generatedMap = True
        if pyxel.btnr(pyxel.KEY_SPACE):
            #self.platformGenerated[2].fall = True
            self.platforms.up  = True

            #platform.breakPlatorm(1)

        if self.platforms.up and self.platforms.platformGenerated.size > 0:
            # print(fonctionVitesse)
            for plt in self.platforms.platformGenerated:
                if 1 <= self.platforms.jumpEtatY < self.platforms.heightJump:
                    plt.vitesse = ((self.platforms.heightJump - 10) / self.platforms.jumpEtatY) * 12
                    plt.position[1] += plt.vitesse

                print(plt.vitesse, self.platforms.jumpEtatY)

            self.platforms.jumpEtatY += 1



        if self.platforms.platformGenerated.size > 0:
            if self.platforms.jumpEtatY > self.platforms.heightJump:
                self.platforms.up = False
                self.platforms.down = True
                self.platforms.jumpEtatY = 1

        if self.platforms.down and self.platforms.platformGenerated.size > 0:
            for plt in self.platforms.platformGenerated:
                if 1 <= self.platforms.jumpEtatY < self.platforms.heightJump:
                    self.vitesse = ((self.platforms.heightJump - 10) / self.platforms.jumpEtatY) * 12
                    plt.position[1] += plt.vitesse

        #print(len(self.platformGenerated))

        #print(platform.platformGenerated)
        """for pltIndex in self.platformFall:
            if platform.platformGenerated[pltIndex][2] < screenSize[1]:
                platform.fallPlatform(pltIndex, 10)
            else:
                platform.platformGenerated.remove(platform.platformGenerated[pltIndex])
                self.platformFall.remove(pltIndex)

        

        if platform.jumpEtatY >= platform.heightJump:
            platform.jumpEtatY = 0
            self.movePlatform = False


        if platform.anim:
            for imgInt in range(20):
                pyxel.blt(x=platform.platformGenerated[platform.animIndice][1], y=platform.platformGenerated[platform.animIndice][2], img=imgInt % 2, u=0, v=0,
                          w=64, h=32, colkey=0)
                pyxel.blt(x=platform.platformGenerated[platform.animIndice][1] + 64, y=platform.platformGenerated[platform.animIndice][2], img=imgInt % 2, u=0,
                          v=0, w=-16, h=32, colkey=0)
                self.draw()
                print("change Color")
            platform.anim = False"""



    def draw(self):
        pyxel.cls(7)
        for plt in self.platforms.platformGenerated:
            if plt.position[1] - 50 > screenSize[1]:
                self.platforms.platformGenerated = np.delete(self.platforms.platformGenerated, np.where(self.platforms.platformGenerated == plt))
            else:
                pyxel.blt(x=plt.position[0], y=plt.position[1], img=plt.type, u=0, v=0, w=64, h=32, colkey=0)
                pyxel.blt(x=plt.position[0] + 64, y=plt.position[1], img=plt.type, u=0, v=0, w=-16, h=32, colkey=0)

Game()