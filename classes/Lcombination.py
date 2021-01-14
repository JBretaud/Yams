"""Lcombination
"""
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QRadioButton, QGridLayout
from classes.score import Score
from classes.Bscore import Bscore

class Lcombination ():
    """Lcombination
    Attributes: 
    intitule, layout
    """
    
    def __init__(self, player):

        self.player = player
        
       
        self.layout = QGridLayout()
        for i in range(len(self.player.scoresheet.table)):
            self.name = self.layout.addWidget(QLabel(self.player.scoresheet.table[i].name),i,0,1,1) 
            square_text = 'X' if player.scoresheet.table[i].value == 0 else '' if player.scoresheet.table[i].value == -1 else str(player.scoresheet.table[i].value)
            self.button = self.layout.addWidget(Bscore(self.player.scoresheet.table[i], self.player, square_text ),i,1,1,1)
        self.disable_btns()
    
    def disable_btns(self):
        for i in range(self.layout.count()):
            print(self.layout.itemAt(i))
            if isinstance(self.layout.itemAt(i).widget(), Bscore):
                self.layout.itemAt(i).widget().setEnabled(False)
    
    def enable_btns(self):
        for i in range(self.layout.count()):
            print(self.layout.itemAt(i))
            if isinstance(self.layout.itemAt(i).widget(), Bscore):
                self.layout.itemAt(i).widget().setEnabled(True)
            
    

    

