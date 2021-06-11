from PyQt5.QtWidgets import QApplication
from classes.interface.BD import BD
from classes.interface.interface import Interface
from classes.party import Party
from classes.player import Player
from pymitter import EventEmitter

ee = EventEmitter()
app = QApplication([])

players = []
players.append(Player('Sonia'))
players.append(Player('Jean'))

party = Party(players, ee)
party.interface.window.show()
app.exec_()
# from classes.party import Party
# party = Party()
# https://build-system.fman.io/pyqt5-tutorial

