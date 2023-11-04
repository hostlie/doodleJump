import pyxel
import random

class Platform:
    def __init__(self, platformType, screenSize, x, y):
        '''
        :param platformType: type de la platforme : 0 = normale / 32 = cassante
        :param screenSize: variable de la taille de l'écran de jeu
        :param x: variable de la position x de la platforme
        :param y: variable de la position y de la platforme
        '''

        self.screenSize = screenSize  # mise à jour de la taille de l'écran de jeu
        self.position = [x, y]  # mise à jour de la position x et y de la platforme
        self.hitbox = (75, 32)  # variable de la hitbox de la platforme
        self.platformType = platformType  # mise à jour du type de platforme
        self.anim = False  # variable booléenne pour l'animation de la platforme si elle est cassante
        self.vitesse = 2  # variable de la vitesse de l'animation de la platforme si elle est cassante et cassée

    def breakPlatorm(self):
        # Animation de la platforme se cassant
        pyxel.blt(x=self.position[0], y=self.position[1] + self.vitesse * 8, img=0, u=0, v=32 + self.platformType, w=64,
                  h=32, colkey=0)

        pyxel.blt(x=self.position[0] + 32 + self.vitesse, y=self.position[1] + self.vitesse * 8, img=0, u=0,
                  v=64 + self.platformType, w=58, h=32, colkey=0)
        pyxel.blt(x=self.position[0] + 64 + self.vitesse, y=self.position[1] + self.vitesse * 8, img=0, u=0,
                  v=32 + self.platformType, w=-16, h=32, colkey=0)


    def draw(self):
        if self.anim:  # si la platforme se casse -> animation
            self.breakPlatorm()
        else:
            # affiche la platforme normale ou cassante (non cassée)
            pyxel.blt(x=self.position[0], y=self.position[1], img=0, u=0, v=self.platformType, w=64, h=32, colkey=0)
            pyxel.blt(x=self.position[0] + 64, y=self.position[1], img=0, u=0, v=self.platformType, w=-16, h=32, colkey=0)