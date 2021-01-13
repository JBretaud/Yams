"""ABC
"""

from classes.player import Player

class Scoreboard:
    """
    """
    def __init__(self,players):
        self.scores = []
        for player in players:
            scores.append(player.score)