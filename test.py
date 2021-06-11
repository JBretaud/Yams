from PyQt5.QtWidgets import QApplication
from classes.loader import Loader
# from classes.BDD import BDD
# from classes.models.PartieRecord import PartieRecord
# from classes.models.ScoreLineRecord import ScoreLineRecord

app = QApplication([])
loader = Loader()

party = loader.loadPartie(41)

party.interface.window.show()
app.exec_()
# DataBase = BDD("yams")
# print(DataBase.getAll())
# partie = PartieRecord("test")
# score = ScoreLineRecord(1,2,3,4,5,6,9,8,7,4,5,6,3,1,2)
# partie.scores = [score]
# partie.persist()

