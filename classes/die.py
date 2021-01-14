"""Un dé à 6 faces
"""

from random import randint

class Die:
    """Die
    Attributes:
    value(int): valeur entre 1 et 6 affichée par le dé
    keep(boolean): determines if the die will be thrown on player's next throw
    """

    def __init__(self):
        self.value = 6
        self.keep  = False
    
    def cast(self):
        """Throws the die
        Return(int): Random number between 1 and 6
        """
        self.value = randint(1,6)

    