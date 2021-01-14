from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont

class Button(QPushButton):
    def __init__ (self, name, lde):
        super(Button,self).__init__(name)
        self.setObjectName(name)
        self.lde = lde
        self.clicked.connect(self.test_click)
        self.setStyleSheet("color: #646665; \
                            background-color:#ccdbd4;\
                            border: none;\
                            border-radius: 5px;")
        self.setFont(QFont('Calibri',20)) 
           
           
    def test_click(self,on_click):
        print('click')  
        self.lde.cast_dice_interface()
        