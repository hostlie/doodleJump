import pyxel

class Jetpack:
    def __init__(self):
        self.position = [0, 0]  # variable de la position x et y du jetpack
        self.hitbox = (24, 36)  # varible de la hitbox du jetpack
        self.jumpHeight = 25  # hauteur du saut qui sera ajouter au player si il y a une collision entre le player et le jetpack
        self.posInLstPlt = None  # index de la position du jetpack dans la liste des platformes générées
        self.active = False  # variable booléenne pour activer ou non le vole du jetpack sur le player
        self.type = 1  # type d'item, ici jetpack, 1 = jetpack


    def draw(self, rotationRJetpack=False):
        '''
        :param rotationRJetpack: si True alors le jetpack changera de côté car le player a aussi changer de côté
        '''
        if self.active:  # si le jetpack s'envole
            if rotationRJetpack:
                pyxel.blt(self.position[0], self.position[1], 0, u=0, v=160, w=12, h=43)  # jetpack côté gauche
            else:
                pyxel.blt(self.position[0], self.position[1], 0, u=0, v=160, w=-12, h=43)  # jetpack côté droit
        else:
            pyxel.blt(self.position[0], self.position[1], 0, u=16, v=160, w=24, h=36)  # affiche le jetpack
