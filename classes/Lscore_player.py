"""Lscore_player
Method: 
"""
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget
from PyQt5.QtGui import QFont, QPalette, QColor
from tkinter import messagebox as messageBox

class Lscore_player:
    def __init__(self, player):
        self.player = player
        self.layout = QGridLayout()
        self.label_player = QLabel(player.name)
        self.label_score = QLabel(str(player.scoresheet.get_current_score()))
        self.layout.addWidget(self.label_player,0,0,1,1)
        self.layout.addWidget(self.label_score,0,1,1,1)
        self.refresh()
        
    def set_player(self, player):
        self.player = player
        self.refresh()

    def refresh(self):
        palette = self.label_player.palette() 
        if self.player.is_active :
            palette.setColor(QPalette.Window, QColor(204, 219, 212))
        else:
            palette.setColor(QPalette.Window, QColor(240, 240, 240))

        self.label_player.setPalette(palette)
        self.label_player.setAutoFillBackground(True)
        self.label_player.update()
            
        self.label_score.setText(str(self.player.scoresheet.get_current_score()))

        
        