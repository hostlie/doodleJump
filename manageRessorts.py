import pyxel
import random
from ressorts import Ressort

class ManageRessorts:
    def __init__(self):
        self.ressortsGenerated = []  # liste des ressorts générés (provisoire)

    def generateRessorts(self, platformes):
        '''
        :param platformes: platformes générées
        '''
        for i in range(len(platformes)):
            rng = random.randint(1,10)  # rng, 1 chance sur 10 d'avoir un ressort sur la platforme
            if rng == 1:
                r = Ressort()  # création de l'objet ressort
                r.position[0] = platformes[i][0].position[0] + 48  # mise à jour de la position du ressort
                r.position[1] = platformes[i][0].position[1] + 32  # mise à jour de la position du ressort
                r.posInLstPlt = i  # met la variable posInLstPlt à l'index de la platforme dans la liste des platformes générées
                self.ressortsGenerated.append(r)  # ajoute le ressort à la liste des ressorts générés


    def draw(self, platformes):
        '''
        :param platformes: variable de la class ManagePlatforme
        '''
        for plt, item in platformes:
            if item:  # si il y a un item sur cette platforme (ressort/jetpack)
                if item.type == 0:  # si l'item est un ressort (0 = ressort)
                    ressort = item
                    ressort.position[0] = plt.position[0] + 28  # mise à jour de la position du ressort sur la platforme
                    ressort.position[1] = plt.position[1] - 32  # mise à jour de la position d uressort sur la platforme
                    ressort.draw()  # affiche le ressort
