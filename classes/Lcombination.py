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
    
    def __init__(self, player, ee):

        self.player = player
        self.buttons = []  
        self.layout = QGridLayout()
        for i in range(len(self.player.scoresheet.table)):
            self.layout.addWidget(QLabel(self.player.scoresheet.table[i].name),i,0,1,1) 
            
            square_text = 'X' if player.scoresheet.table[i].value == 0 else '' if player.scoresheet.table[i].value == -1 else str(player.scoresheet.table[i].value)
            
            btn = Bscore(self.player.scoresheet.table[i], self.player, square_text, ee )
            self.buttons.append(btn)
            self.layout.addWidget(btn,i,1,1,1)
        self.disable_btns()

        @ee.on("cast")
        def enable_btns():
            for button in self.buttons:
                button.setEnabled(not button.square.value >= 0)
        
    def disable_btns(self):
        for button in self.buttons:
            button.setEnabled(False)
    def set_player(self,player):
        self.player = player
        self.buttons
    
    
            
    

    

