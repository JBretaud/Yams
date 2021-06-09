"""Lcombination
"""
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QRadioButton, QGridLayout, QFrame
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
        self.ee = ee
        self.layout = QGridLayout()

        self.Lcombi = QLabel('POSSIBLE COMBINATIONS')
        self.Lcombi.setObjectName("Lcombi")
        self.layout.addWidget(self.Lcombi,0,0,1,2)
        
        self.update_buttons()

        self.frame = QFrame()
        self.frame.setLayout(self.layout)

        self.frame.setStyleSheet("QFrame{max-height:700px;margin:auto;text-align:centre;}\
                                  QLabel{color:#7a7b79;\
                                    border:none;\
                                    margin:auto;\
                                    border-bottom: 2px solid #7a7b79;\
                                    border-radius:0%;\
                                    min-width:200px;\
                                    font-size:20px;\
                                    margin-bottom:5px; \
                                    margin-top:5px; \
                                    padding:5px;\
                                  } \
                                  Bscore{color:black;\
                                    background-color:#fbfcf9;\
                                    border:none;\
                                    height:40px;\
                                  } \
                                   QLabel#Lcombi{\
                                    border:none;\
                                    margin-left:120px;\
                                    color :#8c9083;\
                                    font-size:25px;\
                                    margin-top:-20px;\
                                  }\
                                    ")
  
        self.disable_btns()

        @ee.on("cast")
        def enable_btns():
            for button in self.buttons:
                button.setEnabled(not button.square.value >= 0)
        
    def disable_btns(self):
        for button in self.buttons:
            button.setEnabled(False)

    def set_player(self, player):
        self.player = player
        self.buttons = []
        self.update_buttons()
    
    def update_buttons(self):
      for i in range(len(self.player.scoresheet.table)):
            self.layout.addWidget(QLabel(self.player.scoresheet.table[i].name),i+1,0,1,1)  
            
            square_text = 'X' if self.player.scoresheet.table[i].value == 0 else '' if self.player.scoresheet.table[i].value == -1 else str(self.player.scoresheet.table[i].value)
            
            btn = Bscore(self.player.scoresheet.table[i], self.player, square_text, self.ee )
            btn.setEnabled(False)
            self.buttons.append(btn)
            self.layout.addWidget(btn,i+1,1,1,1)
          
      

    
    
            
    

    

