import pyxel
from jetpack import Jetpack
import random
from copy import deepcopy

class ManageJetpacks:
    def __init__(self):
        self.jetpacksGenerated = []  # liste de la génération des jetpacks (provisoire)
        self.jetpackFly = None  # variable pour stocker le jetpack qui vole


    def generateJetpacks(self, platformes):
        '''

        :param platformes: platformes générées
        :return: met à jour la liste des jetpacks
        '''
        for i in range(len(platformes)):
            rng = random.randint(1,17)  # rng car il ne doit pas y avoir autant de jetpacks que de platform (1 chance sur 17)
            if rng == 1:
                j = Jetpack()  # génération d'un jetpack
                j.position[0] = platformes[i][0].position[0] + 48  # met la position du jetpack à la platfrorme
                j.position[1] = platformes[i][0].position[1] + 32  # met la position du jetpack à la platfrorme
                j.posInLstPlt = i  # met la variable posInLstPlt à l'index de la platforme dans la liste des platformes générées
                self.jetpacksGenerated.append(j)  # ajoute le jetpack à la liste des jetpacks générés

    def update(self):
        pass


    def draw(self, platformes, player):
        '''

        :param platformes: variable de la class ManagePlatforms
        :param player: variable de la class Player
        '''
        for plt, item in platformes.platformGenerated:
            if item:  # si il y a un item (ressort/jetpack)
                if item.type == 1:  # si cet item est de type 1 = jetpack (intrinsèque à la class jetpack)
                    jetpack = item
                    if not self.jetpackFly and jetpack.active:  # si le jetpack ne vole pas et est actif = sur une platforme et touché par le joueur
                        self.jetpackFly = deepcopy(jetpack)  # copie du jetpack
                    else:
                        jetpack.position[0] = plt.position[0] + 28  # mise à jour de la position du jetpacks avec le player
                        jetpack.position[1] = plt.position[1] - 36  # mise à jour de la position du jetpacks avec le player
                        jetpack.draw()  # Affiche le jetpack volant

            if self.jetpackFly:  # si le jetpack volant != None
                if platformes.vy < 1:  # si la vitesse des platformes < 1 (= si le player va tomber)
                    self.jetpackFly = None  # suppression du jetpack qui vole
                else:
                    if player.leftPress:  # si le player va à gauche -> on affiche le jetpack volant à droite du player
                        self.jetpackFly.position[0], self.jetpackFly.position[1] = player.x + player.hitbox[1] - 2, player.y + 3
                        self.jetpackFly.draw(rotationRJetpack=True)  # rotation à droite du jetpack volant
                    else:  # sinon le player va à droite -> on affiche le jetpack volant à gauche du player
                        self.jetpackFly.position[0], self.jetpackFly.position[1] = player.x - 9, player.y + 3
                        self.jetpackFly.draw()  # affiche le jetpack volant