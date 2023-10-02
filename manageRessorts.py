import pyxel
import random
from ressorts import Ressort

class ManageRessorts:
    def __init__(self):
        self.ressortsGenerated = []

    def generateRessorts(self, lenPlatformes):
        for i in range(lenPlatformes):
            rng = random.randint(1,7)
            if rng == 1:
                self.ressortsGenerated.append((i, Ressort()))