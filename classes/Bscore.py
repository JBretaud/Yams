from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from classes.case import Case

class Bscore(QPushButton):
    def __init__ (self, square, player, text):
        super(Bscore,self).__init__()
        self.player = player
        self.clicked.connect(self.score_in_square)
        self.square = square
        self.name = text
    def score_in_square(self):
        try:
            self.player.score(self.square)
            self.name = self.square.value
        except ValueError as error:
            print(error.args)


        
        # print (self.name)
