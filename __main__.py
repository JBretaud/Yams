from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget,QVBoxLayout
from classes.BD import BD
from classes.interface import Interface




app = QApplication([])
interface = Interface()
interface.window.show()
app.exec_()
# from classes.party import Party
# party = Party()
# https://build-system.fman.io/pyqt5-tutorial

