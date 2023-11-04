import pyxel

class Ressort:
    def __init__(self):
        self.position = [0, 0]  # variable de la position du ressort x et y
        self.hitbox = (32, 32)  # variable de la hitbox du ressort
        self.jumpHeight = 5  # variable de la hauteur de saut en plus de celle par défaut lors de la collision avec le ressort
        self.posInLstPlt = None  # variable de l'index du ressort dans la liste des platformes générées
        self.mustAnim = False  # variable booléenne pour savoir si le ressort doit s'animer
        self.animState = 0  # variable de l'état de l'animation en cours
        self.animFrame = 0  # variable de la frame de l'animation en cours
        self.timeAnim = 0  # variable du temps de l'animation en cours
        self.animEnd = False  # variable booléenne pour savoir si l'animation du ressort compressé s'est terminée
        self.type = 0  # type d'item, ici un ressort

    def anim(self):
        self.animFrame = (self.animState % 3) * 32  # met animFrame à la frame suivante
        if self.animState == 2:  # si le nombre de frame est de 2 -> animation terminée
            self.animEnd = True  # l'animation compression est terminée

        if self.animEnd and self.animState == 0:  # si l'animation compression est terminée et que animState = 0
            self.mustAnim = False  # fin de l'animation

        if self.animEnd:  # si l'animation compression est pas terminée
            self.animState -= 1  # mise en place des frames inverse pour l'extension du ressort
        else:
            self.animState += 1  # mise en place des frames pour la compression du ressort
        self.timeAnim = 0.1  # mise à jour du temps de l'animation

    def draw(self):
        if self.mustAnim:  # si le ressort doit s'animer
            self.timeAnim -= 0.1  # le temps d'attente de l'animation diminue à chaque frame
            if self.timeAnim <= 0:  # si le temps d'attente de l'animation est fini on anime le ressort
                self.anim()
        pyxel.blt(self.position[0], self.position[1], img=0, u=self.animFrame, v=128, w=32, h=32, colkey=7)  # affiche le ressort
