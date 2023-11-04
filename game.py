import math
from managePlatforms import ManagePlatforms
from manageRessorts import ManageRessorts
from manageJetpacks import ManageJetpacks
from player import Player
import pyxel


class Game:
    def __init__(self, screenSize):
        self.is_generatedMap = False # si la map doit se générer ou se régénérer
        self.platforms = ManagePlatforms(screenSize) # les platformes
        self.ressorts = ManageRessorts() # les ressorts
        self.jetpacks = ManageJetpacks() # les jetpacks
        self.player = Player(screenSize) # le player

        pyxel.run(self.update, self.draw)


    def update(self):

        self.player.moves() # methode du déplacement du joueur

        if not self.is_generatedMap: # Génération/Regénération de la map
            self.platforms.generatePlatforms(100)  #  creation de 100 platformes de tous types (cassantes/normales)
            self.jetpacks.generateJetpacks(self.platforms.platformGenerated) # génération des jetpacks
            self.ressorts.generateRessorts(self.platforms.platformGenerated) # génération des resorts
            self.platforms.putItem(self.ressorts.ressortsGenerated) # mise en place des ressorts sur les platformes normales
            self.platforms.putItem(self.jetpacks.jetpacksGenerated) # mise en place des jetpacks sur les platformes normales
            #self.jetpacks.generateJetpacks(self.platforms.platformGenerated)
            print(self.jetpacks.jetpacksGenerated)
            print(self.ressorts.ressortsGenerated)
            print(self.platforms.platformGenerated)

            self.is_generatedMap = True

        # NE MARCHE PAS A REVOIR
        if pyxel.btnr(pyxel.KEY_SPACE):  # mise en pause des sauts donc du jeu !!!!PAS LE DEPLACEMENT DU JOUEUR -> A CHANGER
            self.platforms.up = False
            self.platforms.down = False

        self.platforms.update(self.player) # mise a jour des réaction des platformes vis à vis du player

        if self.platforms.platformGenerated[0][0].position[1] < 0:  # Fin du jeu si vrai
            pass#print("End")

        if len(self.platforms.platformGenerated) < 30:  # regénération des platformes (génération à l'infini)
            self.is_generatedMap = False


    def draw(self):
        pyxel.cls(7) # afficher l'arrière plan en blanc
        self.platforms.draw() # afficher les platformes
        self.ressorts.draw(self.platforms.platformGenerated) # afficher les ressorts sur les platformes
        self.jetpacks.draw(self.platforms, self.player) # afficher les jetpacks sur les platformes
        self.player.draw() # afficher le player
