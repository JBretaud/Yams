"""Player
"""

from classes.die import Die
from classes.score import Score

class Player:
    """Joueur

    Attributes:
    name(string) : player name
    number(int) : player number (1-5)
    score(Score): score

    """

    def __init__(self, name):
        # self.number = number
        self.name = name
        self.scoresheet = Score(self)
        self.dice = []
        self.active = False
        self.tries = 3
        for i in range(5):
            self.dice.append(Die())

    def cast_dice(self):
        """
        Lance les dés
        """
        if self.tries == 0 :
            raise ValueError("Can't cast dice more than 3 times")
        else :
            self.tries -= 1
            for die in self.dice:
                if not die.keep:
                    die.cast()

    def in_activate(self):
        self.tries = 3
        self.active = not self.active

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

    def score(self, chosen_case):
        """ Player chooses a case and scores in it. If the desired 
        """
        if chosen_case.number == 6 : raise ValueError("Can't score in the bonus square")
        if chosen_case.value != -1: raise ValueError("The square("+chosen_case.name+") can only be picked once")
        uppertable = 0
        for case in self.scoresheet.table:
            if case.name in self.scoresheet.combinations[0:5]: uppertable += case.value
            if case.name == chosen_case.name:
                case.value = chosen_case.value
        # Fills in the bonus if the uppertable score excedes 63
        if self.scoresheet.table[6].value == 0 and uppertable >= 63:
            self.scoresheet.table[6].value = 35
        chosen_case.value = self.scoresheet.calcScore(chosen_case.number, self.get_dice_values())    
        print(chosen_case.value)    
