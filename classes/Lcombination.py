"""Lcombination
"""
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QRadioButton, QGridLayout
from classes.score import Score

class Lcombination ():
    """Lcombination
    Attributes: 
    intitule, layout
    """
    
    def __init__(self, player):

        self.player = player
        self.intitule = [
            'Aces',
            'Twos',
            'Threes',
            'Fours',
            'Fives',
            'Sixes',
            'Bonus',
            '3 of a kind',
            '4 of a kind',
            'Full House',
            'Small Straight',
            'Long Straight',
            'Yahtzee',
            'Chance'
        ]
       
        self.layout = QGridLayout()
        self.layout.addWidget(QLabel('ok'),0,1,1,1)
        
        for i in range(len(self.intitule)):
            self.name = self.layout.addWidget(QPushButton(self.intitule[i]),i,0,1,1) 
            self.button = self.layout.addWidget(QLabel('ok'),i,1,1,1)

    

