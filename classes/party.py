"""déroulement d'une partie
"""

from classes.player import Player
from classes.interface import Interface
from tkinter import messagebox as messageBox

class Party:
    """Party

    Attributes:
    nb_players(int): Number of players
    players(Array of Player)
    round(int): Number of current round

    """

    def __init__(self,players,ee):
        # self.nb_players = self.ask_nb_players()
        self.round = 1
        self.players = players
        self.interface = Interface(players, ee)
        self.players[0].in_activate()

        @ee.on("points scored")
        def next_turn():
            self.next_player()

        # generates an array of player according to the number of players
        # for i in range(nb_players):
        #     self.players.append(Player(i+1))
    
    def start(self):
        while self.round <= 13:
            for player in self.players:
                player.play()
    
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
       
    

        


