"""BD
Method: 
setDie, change_keep, refresh
"""

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QSizePolicy
from classes.die import Die
import os


class BD (QPushButton):
    def __init__(self,die,name):
        super(BD,self).__init__()
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ROOT_DIR = ROOT_DIR.replace('\\','/')[0:len(ROOT_DIR)-18]
        self.die = die
        self.path_img = "/pictures/D" + str(self.die.value) + ".png"

        self.refresh()
        self.resize(250,250)
        
        self.clicked.connect(self.change_keep)
        self.setObjectName(name)
        
    def set_die(self, die):  
    # Change les dés en fonction du joueur
        self.die = die
        self.path_img = "/pictures/D"+str(die.value)+".png"
        self.refresh()

    def change_keep(self):
    # Modifie la couleur des dés sélectionnés
        if not self.die.lockable: return
        self.die.keep = not self.die.keep
        self.die.keep = self.die.keep
        self.path_img = "/pictures/D"+str(self.die.value)+("-keep.png" if self.die.keep else ".png")
        self.refresh()

    def refresh(self):
        self.path_img = "/pictures/D"+str(self.die.value)+("-keep.png" if self.die.keep else ".png")
        self.setStyleSheet("margin: 10px; \
                            padding: 2ex; \
                            border-image: url('" + self.ROOT_DIR + self.path_img +"') 0 0 0 0 stretch stretch;\
                            height:  80px;\
                            width: 80px; ") 
