import pyxel
import numpy as np
import random
from platforms import Platform


class ManagePlatforms:
    def __init__(self, screenSize):
        self.up = True
        self.down = False
        self.platformGenerated = []
        self.screenSize = screenSize
        self.uniformePositions = [-40] + [i*60 for i in range(screenSize[0] // 60)] + [screenSize[0] - 40]
        self.jumpEtatY = 1
        self.heightJump = 100
        self.vitesse = 1

    def animtionBreakPlatform(self, i):
        self.platformGenerated[i].anim = True



    def generatePlatforms(self, nb_plt):
        if len(self.platformGenerated) > 0:
            y_total = self.platformGenerated[-1][0].position[1]
        else:
            y_total = self.screenSize[1]
        x_gen_before = -1

        for i in range(nb_plt):
            x_gen = random.choice(self.uniformePositions)
            while x_gen_before == x_gen:
                x_gen = random.choice(self.uniformePositions)
            x_gen_before = x_gen
            y_gen = y_total - random.randint(40, 60)
            y_total = y_gen
            #print("append")
            self.platformGenerated.append([Platform(random.choice([0, 0, 0, 0, 32]), self.screenSize, x_gen, y_gen), None])


    def putItem(self, lstItem):
        for pos, item in enumerate(lstItem):
            if self.platformGenerated[item.posInLstPlt][0].platformType != 32:
                self.platformGenerated[item.posInLstPlt][1] = item


    def mustJump(self, posPlayer):
        if self.down:
            for plt, item in self.platformGenerated:
                if plt.position[0] <= posPlayer.x + 14 <= plt.position[0] + 80 and plt.position[1] <= posPlayer.y + 25 <= plt.position[1] + 32:
                    if plt.platformType == 32:
                        plt.anim = True
                    else:
                        print("Saut", len(self.platformGenerated))
                        self.up = True
                        self.down = False

    def update(self):
        pass

    def draw(self):
        for plt, item in self.platformGenerated:
            if plt.anim:
                plt.vitesse += 2
                #plt.position[1] += plt.vitesse

            plt.draw()