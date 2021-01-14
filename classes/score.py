"""Fiche des résultats
"""

from collections import Counter
from classes.case import Case

class Score:
    """Scoreboard
    Attributes:
    table: Array of Cases
    """

    
    def __init__(self, player_name):
        self.player_name = player_name
        self.table=[]
        self.combinations = [
            'Aces',
            'Twos',
            'Threes',
            'Fours',
            'Fives',
            'Sixes',
            'Bonus',
            '3 of a kind',
            '4 of a kind',
            'Full House',
            'Small Straight',
            'Long Straight',
            'Yahtzee',
            'Chance'
        ]

        for i in range(14):
            self.table.append(Case(self.combinations[i],-1,i))

    
    
    
    def calcScore(self, caseNumber, diceValues):
        """ VERIFICATION DE LA COMBINAISON ET CALCUL DES SCORES
        """
        score = 0
        count = Counter(diceValues)   
        # --- RESULTAT SOMME DES NOMBRES POUR 1 VALEUR (1,2,3,4,5,6)
        if caseNumber < 6:
            for value in diceValues:
                if value == caseNumber + 1:
                    score += value
        # --- 3 OF KIND
        elif caseNumber == 7:
            for key in '123456':
                if count[int(key)] >= 3:
                    score = 3 * int(key)
        # --- 4 OF A KIND
        elif caseNumber == 8:
            for key in '123456':
                if count[int(key)] >= 4:
                    score = 4 * int(key)
        # --- FULL HOUSE
        elif caseNumber == 9:
            three = False
            two = False
            for key in '123456': 
                if count[int(key)] == 3: three = True
                if count[int(key)] == 2: two   = True
            if three and two: score = 25
        # --- SMALL STRAIGHT
        elif caseNumber == 10:
            Str = ''.join(str(i) for i in diceValues)
            if '1234' in Str or '2345' in Str or '3456' in Str:
                score = 30
        # --- LONG STRAIGHT        
        elif caseNumber == 11:
            Str = ''.join(str(i) for i in diceValues)
            if '12345' in Str or '23456' in Str:
                score = 40
        # --- YAHTZEE
        elif caseNumber == 12:
            for key in '123456':                
                if count[int(key)] == 5: 
                    score = 50
        # --- CHANCE
        elif caseNumber == 13:
            score += sum(diceValues)
            
        return score

    def get_current_score(self):
        """
        Return(int): Total of the score
        """

        score = 0 
        for case in self.table:
            if case.value != -1 : score += case.value
        return score
