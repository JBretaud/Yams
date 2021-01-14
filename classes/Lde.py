"""BD
Method: 
set_layout_dice, update_player, update_dice,cast_dice_interface
"""
from classes.player import Player
from classes.die import Die
from classes.BD import BD
from classes.buttons import Button
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget
from PyQt5.QtCore import  QRect

class Lde(QWidget):
    def __init__(self, player, ee):
        super(Lde,self).__init__()
        self.dice = []
        self.Die_btns = []
        self.layout = QGridLayout()
        self.update_player(player)
        self.cast_btn = Button("Cast",self, ee)
        self.layout.addWidget(self.cast_btn,1,0,1,0)
        for i in range(5):
            self.Die_btns.append(BD(player.dice[i],"D"+str(i)))
            self.layout.addWidget(self.Die_btns[i],0,i,1,1)
        self.disable_btns()
        @ee.on("cast")
        def enable_btns():
            for btn in self.Die_btns:
                btn.setEnabled(True)
        
        
    def set_layout_dice(self, dice = []):
        if dice == [] : dice = self.dice
        die_btns = self.layout.findChildren(QPushButton.BD)
        for i in range(len(die_btns)):
            die_btns[i].set_die(dice[i])

        launch_btn = self.layout.findChild(Button, "Cast")
     
    def update_player(self, player):
        self.player = player
        self.update_dice()

    def update_dice(self, dice = []):
        if not dice:
            self.dice = self.player.dice 
        else:
            self.dice = dice
        if len(self.Die_btns) > 0:
            for i in range(len(self.Die_btns)):
                self.Die_btns[i].set_die(self.dice[i])
                self.Die_btns[i].refresh()
        
    def cast_dice_interface(self):
        try:
            self.player.cast_dice()
            for btn in self.Die_btns:
                btn.refresh()
        except ValueError as error:
            raise error
    def disable_btns(self):
        for btn in self.Die_btns:
            btn.setEnabled(False)
        
        