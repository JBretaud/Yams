from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from tkinter import messagebox as messageBox

class Button(QPushButton):
    def __init__ (self, name, lde, ee):
        super(Button,self).__init__(name)
        self.setObjectName(name)
        self.lde = lde
        self.ee = ee
        self.clicked.connect(self.test_click)
        self.setStyleSheet("color: #7a7b79; \
                            background-color:#ccdbd4;\
                            margin-top:0%;\
                            border:1px solid;\
                            border-radius: 5px;\
                            ")
        self.setFont(QFont('Calibri',20)) 
           
           
    def test_click(self,on_click):
        self.ee.emit("cast")
        try:
            self.lde.cast_dice_interface()
        except ValueError as error:
            messageBox.showerror('error', error.args)
        