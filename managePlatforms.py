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
        self.heightJump = 13
        self.vy = self.heightJump
        self.ay = 0.3
        self.vitesse = 0


    def computeVitesse(self):
        self.vitesse = self.jumpEtatY ** 2 + 5 * self.jumpEtatY + 0.3

    def animtionBreakPlatform(self, i):
        self.platformGenerated[i].anim = True



    def generatePlatforms(self, nb_plt):
        densityPltBreak = 0
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
            y_gen = y_total - random.randint(70, 100)
            y_total = y_gen

            platformType = random.choice([0, 0, 0, 0, 32])
            if platformType == 32:
                densityPltBreak += 1
                if densityPltBreak == 3:
                    platformType = 0
            else:
                densityPltBreak = 0
            self.platformGenerated.append([Platform(platformType, self.screenSize, x_gen, y_gen), None])


    def putItem(self, lstItem):
        for pos, item in enumerate(lstItem):
            if self.platformGenerated[item.posInLstPlt][0].platformType != 32 and self.platformGenerated[item.posInLstPlt][1] is None:
                print("Item PUT !!!")
                self.platformGenerated[item.posInLstPlt][1] = item

    def collide(self, itemPos, itemHitbx, player, inObject=False):
        if inObject:
            return ((itemPos[0] <= player.x <= itemPos[0] + itemHitbx[0]) or (itemPos[0] <= player.x + player.hitbox[0] <= itemPos[0] + itemHitbx[0])) and (itemPos[1] <= (player.y + player.hitbox[1])/2 <= itemPos[1] + itemHitbx[1] or itemPos[1] <= player.y + player.hitbox[1] <= itemPos[1] + itemHitbx[1])
        else:
            return ((itemPos[0] <= player.x <= itemPos[0] + itemHitbx[0]) or (itemPos[0] <= player.x + player.hitbox[0] <= itemPos[0] + itemHitbx[0])) and itemPos[1] <= player.y + player.hitbox[1] <= itemPos[1] + itemHitbx[1]


    def update(self, player):
        self.vy -= self.ay
        #print(self.vy)
        for plt, item in self.platformGenerated:
            plt.position[1] += self.vy

            if plt.position[1] - 52 > self.screenSize[1]:
                self.platformGenerated.remove([plt, item])

        if self.vy < 0:
            self.down = True


        if self.down:
            for plt, item in self.platformGenerated:
                if item:
                    if self.collide(item.position, item.hitbox, player, True):
                        self.down = False
                        self.vy = self.heightJump + item.jumpHeight
                        item.mustAnim = True

                if self.collide(plt.position, plt.hitbox, player):
                    if plt.platformType == 32:
                        plt.anim = True
                    else:
                        #print("Saut", len(self.platformGenerated))
                        self.down = False
                        self.vy = self.heightJump



    def draw(self):
        for plt, item in self.platformGenerated:
            if plt.anim:
                plt.vitesse += 1
                #plt.position[1] += plt.vitesse

            plt.draw()