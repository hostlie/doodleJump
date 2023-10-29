import pyxel
import random

class Platform:
    def __init__(self, platformType, screenSize, x, y):
        '''
        :param typeP: Type de platforme (0 : normale, 1 : cassante, 2 : tombante, 3 : montante/descendante)
        '''

        self.screenSize = screenSize
        self.position = [x, y]
        self.hitbox = (75, 32)
        self.platformType = platformType
        self.anim = False
        self.fall = False
        self.vitesse = 2


    def fallPlatform(self, speed=3):
        self.position[2] += speed

    def breakPlatorm(self, i):
        # Animation de la platforme se cassant
        pass


    def draw(self):
        if self.anim:
            pyxel.blt(x=self.position[0], y=self.position[1] + self.vitesse * 8, img=0, u=0, v=32 + self.platformType, w=64, h=32, colkey=0)

            pyxel.blt(x=self.position[0] + 32 + self.vitesse, y=self.position[1] + self.vitesse * 8, img=0, u=0, v=64 + self.platformType, w=58, h=32, colkey=0)
            pyxel.blt(x=self.position[0] + 64 + self.vitesse, y=self.position[1] + self.vitesse * 8, img=0, u=0, v=32 + self.platformType, w=-16, h=32, colkey=0)

        else:
            pyxel.blt(x=self.position[0], y=self.position[1], img=0, u=0, v=self.platformType, w=64, h=32, colkey=0)
            pyxel.blt(x=self.position[0] + 64, y=self.position[1], img=0, u=0, v=self.platformType, w=-16, h=32, colkey=0)