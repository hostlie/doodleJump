import pyxel
import random
from ressorts import Ressort

class ManageRessorts:
    def __init__(self):
        self.ressortsGenerated = []

    def generateRessorts(self, platformes):
        for i in range(len(platformes)):
            rng = random.randint(1,10)
            if rng == 1:
                r = Ressort()
                r.position[0] = platformes[i][0].position[0] + 48
                r.position[1] = platformes[i][0].position[1] + 32
                r.posInLstPlt = i
                self.ressortsGenerated.append(r)


    def draw(self, platformes):
        for plt in platformes:
            if plt[1] != None:
                ressort = plt[1]
                ressort.position[0] = plt[0].position[0] + 28
                ressort.position[1] = plt[0].position[1] - 32
                ressort.draw()
