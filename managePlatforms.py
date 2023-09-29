import pyxel
import numpy as np
import random
from platforms import Platform


class ManagePlatforms:
    def __init__(self, screenSize):
        self.up = False
        self.down = False
        self.platformGenerated = np.array([])
        self.screenSize = screenSize
        self.uniformePositions = [-40] + [i*60 for i in range(screenSize[0] // 60)] + [screenSize[0] - 40]
        self.jumpEtatY = 1
        self.heightJump = 20 # / 30 en seconde exemple 60 / 30 = 2 secondes
        self.vitesse = 0


    def generatePlatforms(self, nb_plt):
        if self.platformGenerated.size > 0:
            if self.platformGenerated:
                y_total = self.platformGenerated[-1].position[1]
            else:
                y_total = self.screenSize[1]
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
            self.platformGenerated = np.append(self.platformGenerated, [Platform(0, "platforms.pyxres", self.screenSize, x_gen, y_gen)])