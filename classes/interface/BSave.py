from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from classes.case import Case

class BSave(QPushButton):
    def __init__ (self, ee):
        super(BSave,self).__init__()
        self.setText("Save")
        self.clicked.connect(self.save)
        self.ee = ee

    def save(self):      
        self.ee.emit("save")

     


