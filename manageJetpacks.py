import pyxel
from jetpack import Jetpack
import random

class ManageJetpacks:
    def __init__(self):
        self.jetpacksGenerated = []


    def generateJetpacks(self, platformes):
        for i in range(len(platformes)):
            rng = random.randint(1,17)
            if rng == 1:
                j = Jetpack()
                j.position[0] = platformes[i][0].position[0] + 48
                j.position[1] = platformes[i][0].position[1] + 32
                j.posInLstPlt = i
                self.jetpacksGenerated.append(j)

    def draw(self):
        for jetpack in self.jetpacksGenerated:
            jetpack.draw()