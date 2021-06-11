"""déroulement d'une partie
"""

from classes.models.ScoreLineRecord import ScoreLineRecord
from classes.player import Player
from classes.interface.interface import Interface
from classes.models.PartieRecord import PartieRecord
from tkinter import messagebox as messageBox
from classes.BDD import BDD

class Party:
    """Party

    Attributes:
    nb_players(int): Number of players
    players(Array of Player)
    round(int): Number of current round

    """

    def __init__(self,players: list[Player],ee, partieRecord: PartieRecord = None ):
        # self.nb_players = self.ask_nb_players()
        try:
            self.round = partieRecord.Tour
            self.IdPartie = partieRecord.IdPartie
            self.players = []
            for score in partieRecord.scores:
                self.players.append(Player('',score))
        except NameError or AttributeError:
            self.round = 1
            self.players = players
            self.IdPartie = -1
            self.players[0].in_activate()
            
            
        self.dataBase = BDD("yams")
        self.interface = Interface(self.players, ee)
        
        @ee.on("points scored")
        def next_turn():
            self.next_player()
        @ee.on("save")
        def save():
            self.saveGame()
    
    def start(self):
        while self.round <= 13:
            for player in self.players:
                if player.is_active : player.play()
    
    def next_player(self):
        
        for i in range(len(self.players)):
            if self.players[i].is_active :
                # print("Message", "Joueur actif : " + self.players[i].name)
                self.players[i].in_activate()
                if i == len(self.players)-1:
                    self.players[0].in_activate()
                    break
                else:    
                    self.players[i+1].in_activate()
                    break
        self.interface.update_active_player()
        
    def saveGame(self):
        rec = self.toPartyRecord()
        idPlayers = rec.persist(self.dataBase)
        if len(idPlayers) > 0 :
            self.IdPartie = idPlayers[0]
            for i in range(len(self.players)):
                self.players[i].id = idPlayers[i+1]
        

    def toPartyRecord(self) -> PartieRecord:
        result = PartieRecord("test1", self.IdPartie, len(self.players), [], self.round)
        for player in self.players:
            result.scores.append(player.toScoreLineRecord())
        return result
        

       
    

        


