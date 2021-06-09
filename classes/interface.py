from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget,QVBoxLayout
from classes.Lde import Lde
from classes.player import Player
from classes.Bscore import Bscore
from classes.Lcombination import Lcombination
from classes.Lscore_players import Lscore_players
from PyQt5.QtGui import *
from tkinter import messagebox as messageBox

class Interface:
    def __init__(self, players, ee):
        self.players = players
        self.window = QWidget()
        self.window.resize(1250,500)
        
        self.layout_de = Lde(players[0], ee)
        self.layout_player = Lscore_players(players)
        self.layout_combinaisons = Lcombination(players[0], ee)
        self.main_layout = QGridLayout()

        self.main_layout.addWidget(self.layout_combinaisons.frame,0,0,2,1)
        self.main_layout.addLayout(self.layout_de.layout,0,1,1,1)
        self.main_layout.addWidget(self.layout_player.frame,1,1,1,1)

        self.window.setLayout(self.main_layout)

    def update_active_player(self):
        self.layout_combinaisons.disable_btns()
        for player in self.players:
            for die in player.dice:
                die.lockable = False
            self.layout_player.set_player(player)
            if player.is_active:
                self.layout_de.update_player(player)
                self.layout_combinaisons.set_player(player)

        