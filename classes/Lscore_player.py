"""Lscore_player
Method: 
"""
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget
from PyQt5.QtGui import QFont

class Lscore_player:
    def __init__(self, player):
        self.player = player
        self.layout = QGridLayout()
        self.label_player = QLabel(player.name)
        self.label_score = QLabel(str(player.score.get_current_score()))
        self.layout.addWidget(self.label_player,0,0,1,1)
        self.layout.addWidget(self.label_score,0,1,1,1)
        self.refresh()
        
    def set_player(self, player):
        self.player = player
        self.refresh()

    def refresh(self):
        self.label_player = QLabel(self.player.name)
        self.label_score = QLabel(str(self.player.score.get_current_score()))
        