from classes.BDD import BDD
from classes.party import Party
from classes.models.PartieRecord import PartieRecord
from pymitter import EventEmitter
class Loader:
    def __init__(self):
        self.DB = BDD("Yams")

    def getAllParties(self) -> list[PartieRecord]:
        lstParties = []
        rawresult = self.DB.getAll()
        for i in range(len(rawresult)):
            lstParties.append(rawresult[i])
        return lstParties
    
    def getPartie(self, id) -> PartieRecord:
        return PartieRecord('', -1, 0, [], 1, self.DB.getPartie(id))
    
    def loadPartie(self, id) -> Party:
        ee = EventEmitter()
        Rec = self.getPartie(id)
        party = Party([], ee, Rec) 
        return party


            

