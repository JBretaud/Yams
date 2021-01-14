from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget,QVBoxLayout
from classes.Lde import Lde
from classes.player import Player
from classes.party import Party
from classes.Lcombination import Lcombination
from classes.Lscore_players import Lscore_players

class Interface:
    def __init__(self):
        self.window = QWidget()
        self.window.resize(1250,500)
        
        
        players=[]
        players.append(Player('Sonia'))
        players.append(Player('Jean'))

        self.party = Party(players)

        layout_de = Lde(players[0])
        layout_player = Lscore_players(players)
        layout_combinaisons = Lcombination(players[0])
        self.main_layout = QGridLayout()

        self.main_layout.addLayout(layout_combinaisons.layout,0,0,2,1)
        self.main_layout.addLayout(layout_de.layout,0,1,1,1)
        self.main_layout.addWidget(layout_player.frame,1,1,1,1)

        self.window.setLayout(self.main_layout)