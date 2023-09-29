import pyxel
import random

class Platform:
    def __init__(self, typeP, imagesFilename, screenSize, x, y):
        '''
        :param typeP: Type de platforme (0 : normale, 1 : cassante, 2 : tombante, 3 : montante/descendante)
                    pyxel.blt(x=self.position[0], y=self.position[1], img=self.type, u=0, v=0, w=64, h=32, colkey=0)
            pyxel.blt(x=self.position[0] + 64, y=self.position[1], img=self.type, u=0, v=0, w=-16, h=32, colkey=0)
        '''

        pyxel.load(imagesFilename)

        self.screenSize = screenSize
        self.position = [x, y]
        self.type = typeP
        self.anim = False
        self.animIndice = 0
        self.fall = False


    def fallPlatform(self, speed=3):
        self.position[2] += speed

    def scrollPlatform(self, speed=1):
        self.position[2] += speed


    def breakPlatorm(self, i):
        # Animation de la platforme se cassant
        self.animIndice = i
        self.anim = True
        """for imgInt in range(2):
            pyxel.blt(x=self.platformGenerated[i][1], y=self.platformGenerated[i][2], img=imgInt, u=0, v=0, w=64, h=32, colkey=0)
            pyxel.blt(x=self.platformGenerated[i][1] + 64, y=self.platformGenerated[i][2], img=imgInt, u=0, v=0, w=-16, h=32, colkey=0)"""


    # =====================================================
    # == DRAW
    # =====================================================




#Platforms(1, "platforms.pyxres")


