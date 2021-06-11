from mysql.connector.errors import Error
from classes.models.ScoreLineRecord import ScoreLineRecord


class PartieRecord:
    def __init__(self, nom: str = '',  IdPartie : int = -1, nbJoueurs: int = 0, scores: list[ScoreLineRecord] = [], tour = 1, rawData: list = None):
        self.scores = []
        try:
            
            for i in range(len(rawData)) :
                try:
                    self.IdPartie
                except AttributeError:
                    self.IdPartie = rawData[i][0]
                    self.nom = rawData[i][1]
                    self.NbJoueurs = rawData[i][2]
                    self.Tour = rawData[i][3]
                self.scores.append(ScoreLineRecord(rawData[i]))
        except AttributeError or TypeError:
            self.nom = nom
            self.IdPartie = IdPartie
            self.tour = tour
            self.scores = scores
            self.Table = "partie"
            self.NbJoueurs = nbJoueurs
            self.fields = ["Nom", "Tour"]
            self.values = [self.nom, self.tour]

        
    
    def persist(self, DataBase) -> tuple:
        result = []
        
        if self.IdPartie == -1:
            print("c")
            try:
                IdPartie = DataBase.insert(self.Table, self.fields, self.values)
            except Error as e:
                IdPartie = -1
                print(e)
            self.IdPartie = IdPartie
            result.append(IdPartie)
            for score in self.scores:
                score.setIdPartie(self.IdPartie)
                IdScore = DataBase.insert(score.Table, score.fields, score.values)
                score.setIdScore(IdScore)
                result.append(IdScore)
        else:
            print("d")
            DataBase.update(self.IdPartie, self.Table, self.fields, self.values)
            for score in self.scores:
                DataBase.update(score.IdScore, score.Table, score.fields, score.values)
        return tuple(result)


        
    def __str__(self):
        result = ""
        for attr, value in self.__dict__.items():
            if type(value) is list:
                for val in value:
                    result += str(val)+",\n"
            else :
                result += attr+" : "+str(value)+",\n"
        return result
        


