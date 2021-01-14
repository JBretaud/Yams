"""Lscore_players
Method: 
"""
from classes.Lscore_player import Lscore_player
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget, QFrame

class Lscore_players:
    def __init__(self, players):
        self.layout = QGridLayout()
        self.player_layouts = []
        for i in range(len(players)):
            self.player_layouts.append(Lscore_player(players[i]))
            self.layout.addLayout(self.player_layouts[i].layout,i,0,1,1)
        self.frame = QFrame()
        self.frame.setLayout(self.layout)
        self.frame.setStyleSheet("QLabel { color:red; }")
            
        
        