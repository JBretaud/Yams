class ScoreLineRecord:
        

    def __init__(self, rawData: tuple):
        
        self.NomJoueur = rawData[4]
        self.Aces      = rawData[5]
        self.Twos      = rawData[6]
        self.Threes    = rawData[7]
        self.Fours     = rawData[8]
        self.Fives     = rawData[9]
        self.Sixes     = rawData[10]
        self.Bonus     = rawData[11]
        self.Brelan    = rawData[12]
        self.Carre     = rawData[13]
        self.Full      = rawData[14]
        self.PSuite    = rawData[15]
        self.GSuite    = rawData[16]
        self.Yams      = rawData[17]
        self.Chance    = rawData[18]
        self.IsActif   = rawData[19]
        self.Tries     = rawData[20]
        self.IdScore   = rawData[21]
        self.Table     = "score"
        self.IdPartie  = rawData[0]
        self.fields, self.values = self.getFieldsValues()

    def getFieldsValues(self):
        fields = []
        values = []
        for attr, value in self.__dict__.items():
            if not attr.lower() in ["fields", "values", "table"]:
                fields.append(attr)
                values.append(value)
        return fields, values
    def setIdPartie(self, IdPartie):
        self.IdPartie = IdPartie
        self.fields, self.values = self.getFieldsValues()
    
    def setIdScore(self, IdScore):
        self.IdScore = IdScore
        self.fields, self.values = self.getFieldsValues()

    def __str__(self):
        result = ""
        for attr, value in self.__dict__.items():
            if attr != "fields" and attr != "values":
                if type(value) is int :
                    result += attr+" : "+str(value)+",\n"
                elif type(value) is list:
                    for val in value:
                        result += "   "+str(val)+",\n"
                else :
                    result += attr+" : "+value+",\n"
        return result
    def getScoreDict(self) -> dict:
        
        result = {}
        result["Aces"] = self.Aces
        result["Twos"] = self.Twos
        result["Threes"] = self.Threes
        result["Fours"] = self.Fours
        result["Fives"] = self.Fives
        result["Sixes"] = self.Sixes
        result["Bonus"] = self.Bonus
        result["3 of a kind"] = self.Brelan
        result['4 of a kind'] = self.Carre
        result['Full House'] = self.Full
        result['Small Straight'] = self.PSuite
        result['Long Straight'] = self.GSuite
        result['Yahtzee'] = self.Yams
        result['Chance'] = self.Chance
        return result


