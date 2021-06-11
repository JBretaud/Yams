"""Player
"""

from classes.models.ScoreLineRecord import ScoreLineRecord
from classes.die import Die
from classes.score import Score
from tkinter import messagebox as messageBox

class Player:
    """Joueur

    Attributes:
    name(string) : player name
    number(int) : player number (1-5)
    score(Score): score

    """

    def __init__(self, name: str, scoreRecord: ScoreLineRecord = None):
        
        self.scoresheet = Score(self)
        self.dice = []
        try:
            self.name = scoreRecord.NomJoueur
            self.is_active = scoreRecord.IsActif > 0
            self.tries = scoreRecord.Tries
            self.id = scoreRecord.IdScore
            points = scoreRecord.getScoreDict()
            
            # Alimente la feuille de score du joueur avec les infos de la base de donnée
            for attr, value in points.items():
                for i in range(len(self.scoresheet.table)):
                    if self.scoresheet.table[i].name == attr:
                        self.scoresheet.table[i].value = value

        except NameError or AttributeError:
            self.is_active = False
            self.name = name
            self.tries = 3
            self.id = -1

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
                    die.lockable = True

    def in_activate(self):
        self.tries = 3
        self.is_active = not self.is_active
        for die in self.dice:
            die.value = 6
            die.keep = False

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
            if case.name in self.scoresheet.combinations[0:6]: uppertable += case.value
        chosen_case.value = self.scoresheet.calcScore(chosen_case.number, self.get_dice_values()) 
        # Fills in the bonus if the uppertable score excedes 63
        if self.scoresheet.table[6].value == 0 and uppertable >= 63:
            self.scoresheet.table[6].value = 35
    
    def __str__(self):
        for attr, value in self.__dict__.items():
            result = ""
            result += attr+" : "+str(value)+",\n"
            
        return result
    
    def toScoreLineRecord(self) -> ScoreLineRecord:
        cases = []
        cases.append(-1)
        cases.append('')
        cases.append(0)
        cases.append(1)
        cases.append(self.name)
        for case in self.scoresheet.table:
            cases.append(str(case.value))
        if self.is_active : 
            cases.append(1) 
        else :
            cases.append(0)
        cases.append(self.tries)
        cases.append(self.id)
        return ScoreLineRecord(tuple(cases))
            
