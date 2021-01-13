from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from stylesheet import style

app = QApplication([])
app.setStyleSheet(style)
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QLabel('Hello World!'))
button = QPushButton("&Download")
layout.addWidget(button)
window.setLayout(layout)

window.show()
app.exec_()
# from classes.party import Party
# party = Party()
# https://build-system.fman.io/pyqt5-tutorial

