"""Lscore_players
Method: 
"""
from classes.Lscore_player import Lscore_player
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget, QFrame

class Lscore_players:
    def __init__(self, players):
        self.layout = QGridLayout()
        self.player_layouts = []
        self.layout.addWidget(QLabel('Scores'),0,1,1,1)

        for i in range(len(players)):
            self.player_layouts.append(Lscore_player(players[i]))
            self.layout.addLayout(self.player_layouts[i].layout,i+1,1,1,1)

           
        self.frame = QFrame()
        self.frame.setLayout(self.layout)

        self.frame.setStyleSheet("QFrame{max-height:200px;margin:auto;text-align:centre;}\
                                  QLabel{color:#7a7b79;\
                                  border:none;\
                                  margin:auto;\
                                  border: 3px solid #7a7b79;\
                                  border-radius:0%;\
                                  max-width:500px;\
                                  font-size:20px;\
                                  margin-bottom:5px; \
                                  margin-top:5px; \
                                  padding:5px;\
                                  } \
                                    ")
       
            
        
        