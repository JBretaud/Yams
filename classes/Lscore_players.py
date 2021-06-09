"""Lscore_players
Method: 
"""
from classes.Lscore_player import Lscore_player
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget, QFrame
from PyQt5.QtGui import QPalette

class Lscore_players:
    def __init__(self, players):
        self.layout = QGridLayout()
        self.player_layouts = []

        self.Lscore = QLabel('Scores')
        self.Lscore.setObjectName("Lscore")
        self.layout.addWidget(self.Lscore,0,1,1,1)

        self.Lname = QLabel('Players')
        self.Lname.setObjectName("Lname")
        palette = self.Lname.palette()
        self.layout.addWidget(self.Lname,0,0,1,0)

        for i in range(len(players)):
            self.player_layouts.append(Lscore_player(players[i]))
            self.layout.addLayout(self.player_layouts[i].layout,i+1,0,1,0)
        
        self.frame = QFrame()
        self.frame.setLayout(self.layout)
        self.frame.setStyleSheet("QFrame{max-height:200px;margin:auto;text-align:centre;}\
                                QLabel{color:#7a7b79;\
                                    border:none;\
                                    margin:0px;\
                                    border: 3px solid #7a7b79;\
                                    border-radius:0%;\
                                    max-width:500px;\
                                    font-size:20px;\
                                }\
                                QLabel#Lscore{\
                                    border:none;\
                                    font-size:20px;\
                                    text-align:right;\
                                    }\
                                QLabel#Lname{\
                                    border:none;\
                                    font-size:20px;\
                                    margin-left:30px; }\
                                QLabel#LActive{\
                                    border:none;\
                                    font-size:30px;\
                                    margin-left:30px;\
                                    background-color:lightgreen}\
                                    ")
    def set_player(self, player):
        for layout in self.player_layouts:
            layout.refresh()
       
            
        
        