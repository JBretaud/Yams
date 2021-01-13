"""Joueur
"""

from classes.die import Die
from classes.score import Score

class Joueur:
    """Joueur

    Attributes:
    name(string) : player name
    number(int) : player number (1-5)
    score(Score): score

    """

    def __init__(self, number):
        self.number = number
        self.name = ask_name()
        self.score = Score(self)
        self.dice = []
        for i in range(5):
            self.dice.append(Die())
    
    def play(self):
        """Play a round
        """

        # Reinitializes the keep attribute of the players dices to false
        for die in self.dice:
            die.keep = False

        # Launches up to three rounds 
        for i in range(3):
            self.cast_dice()
            if i < 2:
                self.choose_dice()
        try:
            self.score.score(self.chooseCase)
        except ValueError as Err:
            print(Err.ofcorrecttype)

    def cast_dice(self):
        """
        Lance les dés
        """

        result = []
        for die in self.dice:
            if not die.keep:
                die.cast()

        print(result)
    
    def ask_name(self):
        """ Ask for player's name
        Return(str): name of the player
        """
    
    def choose_dice(self):
        """Choose the dices to keep and sets their 'keep' attribute to 'True'
        """
    def get_dice_values(self):
        """
        Return(Array of int)
        """

        result = []
        for die in self.dice:
            result.append(die.value)
        return sorted(result)
    
    def chooseCase(self):
        """
        Return(tuple): ('case name', 'score')
        """
        
