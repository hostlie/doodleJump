import pyxel
import numpy as np
import random
from platforms import Platform


class ManagePlatforms:
    def __init__(self, screenSize):
        '''
        :param screenSize: taille de l'écran de jeu
        '''
        #self.up = True  # variable d'état de la monté des platformes
        self.down = False  # variable d'état de la descente du player
        self.platformGenerated = []  # liste des platformes générées (non provisoire cette fois ci)
        self.screenSize = screenSize  # mise à jour de la taille de l'écran de jeu
        self.uniformePositions = [-40] + [i*60 for i in range(screenSize[0] // 60)] + [screenSize[0] - 40]   # toutes les positions différentes possibles pour les platformes (uniformisation des position x des platformes)
        self.heightJump = 13  # hauteur du saut de base si collision avec une platforme normale
        self.vy = self.heightJump  # vitesse y à l'intant t
        self.ay = 0.3  # accelération de la vitesse à l'intant t


    def generatePlatforms(self, nb_plt):
        '''
        :param nb_plt: variable du nombre de platformes à générer/regénérer
        '''
        densityPltBreak = 0  # si la variable = 3 alors il y a une trop forte densité de platformes cassantes (empêche l'inaccessibilité au platformes supérieur)
        if len(self.platformGenerated) > 0:  # si les platformes on déjà étaient générées une fois
            y_total = self.platformGenerated[-1][0].position[1]  # mise à jour de la position y de la platforme à générer (par rapport à la position de la dernière platforme générer)
        else:
            y_total = self.screenSize[1]  # mise à jour de la position y de la platforme à générer (tout en bas de l'écran)

        x_gen_before = -1  # variable pour éviter d'avoir 2 platformes côte-à-côte
        for i in range(nb_plt):
            x_gen = random.choice(self.uniformePositions)  # choisi aléatoirement une position x uniforme
            while x_gen_before == x_gen:  # éviter d'avoir 2 platformes côte-à-côte
                x_gen = random.choice(self.uniformePositions)  # choisi aléatoirement une position x uniforme
            x_gen_before = x_gen  # mise à jour de la position x de la platforme précédente
            y_gen = y_total - random.randint(70, 100)  # mise à jour de la position y par rapport aux platformes déjà générées
            y_total = y_gen  # variable y_total est mise à jour car la platforme à pris de la hauteur

            platformType = random.choice([0, 0, 0, 0, 32])  # choisi aléatoirement le type de la platforme (0 = normale / 32 = cassante)
            if platformType == 32:
                densityPltBreak += 1
                if densityPltBreak == 3:  # il y a une trop forte densité de platformes cassantes le type doit être de 0
                    platformType = 0
            else:
                densityPltBreak = 0
            self.platformGenerated.append([Platform(platformType, self.screenSize, x_gen, y_gen), None])  # ajoute la platforme générée à la liste des platformes, le None signifie qu'il n'y a pour l'instant pas d'item sur la platforme


    def putItem(self, lstItem):
        '''
        :param lstItem: liste des items (ressorts ou jetpacks)
        '''
        for pos, item in enumerate(lstItem):
            # vérifie que la platforme ne soit pas cassante et que la platforme n'a pas d'item sur elle (pour ne pas écraser l'item déjà présent)
            if self.platformGenerated[item.posInLstPlt][0].platformType != 32 and self.platformGenerated[item.posInLstPlt][1] is None:
                self.platformGenerated[item.posInLstPlt][1] = item  # met l'item à la place du None dans les platformes générées

    def collide(self, itemPos, itemHitbx, player, inObject=False):
        '''
        :param itemPos: variable de la position de l'item
        :param itemHitbx: variable de la hitbox de l'item
        :param player: variable de la class player
        :param inObject: variable booléenne pour savoir si le jour est en collision aussi à l'intérieur de l'objet (True) ou juste sur les côtés de l'objet (False), par defaut False
        :return True si le player est en collision avec les platformes sinon False
        '''
        if inObject:
            return ((itemPos[0] <= player.x <= itemPos[0] + itemHitbx[0]) or (itemPos[0] <= player.x + player.hitbox[0] <= itemPos[0] + itemHitbx[0])) and (itemPos[1] <= (player.y + player.hitbox[1])/2 <= itemPos[1] + itemHitbx[1] or itemPos[1] <= player.y + player.hitbox[1] <= itemPos[1] + itemHitbx[1])
        else:
            return ((itemPos[0] <= player.x <= itemPos[0] + itemHitbx[0]) or (itemPos[0] <= player.x + player.hitbox[0] <= itemPos[0] + itemHitbx[0])) and itemPos[1] <= player.y + player.hitbox[1] <= itemPos[1] + itemHitbx[1]


    def update(self, player):
        '''
        :param player: variable de la class player
        '''
        self.vy -= self.ay  # met à jour la vitesse y
        #print(self.vy)
        for plt, item in self.platformGenerated:
            plt.position[1] += self.vy  # met à jour la position y de chaque platforme

            if plt.position[1] - 52 > self.screenSize[1]:  # si la platforme est en bas de l'écran de jeu et non visible
                self.platformGenerated.remove([plt, item])  # suppression de la platforme et de l'item dessus
                #print(len(self.platformGenerated))

        if self.vy < 0:  # si la vitesse y est inférieur à 0 (= le player tombe)
            self.down = True  # mise à jour de la variable de chute du player


        if self.down:  # si le player tombe
            for plt, item in self.platformGenerated:
                if item:  # si il y a un item sur la platforme
                    if self.collide(item.position, item.hitbox, player, True):  # si il y a une collision du player dans l'item
                        self.down = False  # le player rebondi
                        self.vy = self.heightJump + item.jumpHeight  # mise à jour de la hauteur du player en fonction de l'item
                        item.mustAnim = True  # il doit y avoir une animation (pas pour le jetpack)
                        if item.type == 1:  # si l'item est un jetpack
                            item.active = True  # activation du jetpack sur le player

                if self.collide(plt.position, plt.hitbox, player):  # si il y a une collision du player sur une platforme
                    if plt.platformType == 32:  # si la platforme est cassante (32 = cassante)
                        plt.anim = True  # animation de la chute de la platforme cassante
                    else:
                        #print("Saut", len(self.platformGenerated))
                        self.down = False  # rebond le player monte -> down = False
                        self.vy = self.heightJump  # mise à jour de la hauteur normale de saut du player



    def draw(self):
        for plt, item in self.platformGenerated:
            if plt.anim:  # si la platforme s'anime -> cassante et a été touchée par le player
                plt.vitesse += 1  # augmentation de la vitesse de chute de la platforme -> simulation de gravité

            plt.draw()  # affiche la platforme