"""déroulement d'une partie
"""

from classes.player import Player

class Party:
    """Party

    Attributes:
    nb_players(int): Number of players
    players(Array of Player)
    round(int): Number of current round

    """

    def __init__(self,players):
        # self.nb_players = self.ask_nb_players()
        self.round = 1
        self.players = []

        # generates an array of player according to the number of players
        # for i in range(nb_players):
        #     self.players.append(Player(i+1))


    def ask_nb_players(self):
        """Ask user the number of players
        Return(int): number of players
        """

        while True:
            print("Combien de joueurs participeront à la partie (1-5)?")
            nb_players = int(input())
            if nb_players > 0 and nb_players < 6:
                return nb_players
            print("Veuillez renseigner un nombre entre 1 et 6")
    
    def start(self):
        while self.round <= 13:
            for player in self.players:
                player.play()
    
    def next_player(self):
        for i in range(len(self.players)):
            if players[i].active :
                players[i].in_activate
                if i == len(self.players):
                    players[0].in_activate
                else:    
                    players[i+1].in_activate
    

        


