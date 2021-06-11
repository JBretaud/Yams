from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from classes.case import Case

class Bscore(QPushButton):
    def __init__ (self, square, player, value, ee):
        super(Bscore,self).__init__()
        self.player = player
        self.setText(value)
        self.clicked.connect(self.score_in_square)
        self.square = square
        self.ee = ee

    def score_in_square(self):
        try:
            self.player.score(self.square)
            square_text = 'X' if self.square.value == 0 else '' if self.square.value == -1 else str(self.square.value)
            self.setText(square_text)
            self.refresh()
            self.ee.emit("points scored")
        except ValueError as error:
           print(error.args)

    def set_player(self,player):
        self.player = player
        self.refresh()
    
    def refresh(self):
        for square in self.player.scoresheet.table:
            if square.name == self.square.name:
                self.square = square
                break
     


