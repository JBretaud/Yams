import mysql.connector
class BDD:
    def __init__(self, DB):
        self.user = "root"
        self.password = ""
        self.host = "localhost"
        self.DB = DB
        self.connection = mysql.connector.connect(
            host="localhost",
            user=self.user,
            password=self.password,
            database = self.DB
        )
        self.cursor = self.connection.cursor()
        
    def execute(self, request):
        print(request)
        result = ''
        try:
            self.cursor.execute(request)
            if request.find("INSERT INTO") >= 0:
                self.connection.commit()
                result = self.cursor.lastrowid
                
            elif request.find("SELECT") >= 0:
                result =  self.cursor.fetchall()
                
            elif request.find("UPDATE") >= 0:
                self.connection.commit()
                
            print("connection close")
            return result 
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)     
        
    def getFieldType(self,  field : str, table: str) -> str:
        """
        Retourne si le type de champs de la table est string ou int
        """
        print("i")
        try:
            self.cursor.close()
            self.cursor = self.connection.cursor()
            print("i1")
            self.cursor.execute("DESCRIBE "+table)
            print("i2")
            result = self.cursor.fetchall()
            print("i3")
            print("connection close")
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            for params in result:
                if params[0] == field:
                    if params[1].find("varchar") >= 0:
                        return 'string'
                    elif params[1].find("int") >= 0:
                        return 'int'
    def insert(self, table: str, fields : list[str], values : list[str]) -> int:
        """
        insert dynamiquement un objet en base de données
        """
        print(values)
        (QueryFields, QueryValues) = self.setParams(fields, values)
        request = "INSERT INTO "+table+" ("+QueryFields+") VALUES("+QueryValues+")"
        return self.execute(request)

    def setParams(self, fields : list[str], values : list[str]) -> tuple:
        """
        Retourne sous forme de tuple les strings à insérer dans les insert
        """
        table = "score" if len(fields) > 15 else "partie"
        ResFields = ''
        ResValues = ''
        for i in range(len(fields)):
            if not ( fields[i] == "IdScore" and values[i] == -1):
                ResValues += "," if ResValues != '' else ""
                ResFields += "," if ResFields != '' else ""

                ResFields += fields[i]   
                try:
                    if self.getFieldType(fields[i], table) == "string":
                        ResValues+= "'" + str(values[i]) + "'"
                    elif self.getFieldType(fields[i], table) == "int":
                        ResValues+= str(values[i])
                except mysql.connector.Error as e:
                    print(e)

        return ResFields, ResValues
    
    def getAll(self):
        return self.execute("SELECT partie.IdPartie, Nom, COUNT(*) as NbJoueurs \
                               FROM partie \
                           GROUP BY partie.IdPartie, Nom")
    
    def getPartie(self, idPartie):
        return self.execute("SELECT score.IdPartie, Nom, NbJoueurs, Tour, NomJoueur, Aces, Twos, Threes, Fours, Fives,\
                                    Sixes, Bonus, Brelan, Carre, Full, PSuite, Gsuite, Yams, Chance, IsActif, Tries, IdScore \
                               FROM partie\
                                    inner join score on score.IdPartie = partie.IdPartie\
                                    inner join (SELECT IdPartie, count(*) as NbJoueurs \
                                                  FROM score GROUP BY IdPartie\
                                                )Nb on Nb.IdPartie = score.IdPartie\
                              WHERE score.IdPartie = "+str(idPartie)
                            )
    def update(self, id, table, fields, values):
        params = self.setUpdateParams(table, fields, values)
        return self.execute("UPDATE "+table+" SET "+params+ " WHERE Id"+table.capitalize()+" = "+str(id))
    
    def setUpdateParams(self, table: str,  fields: list, values: list) -> str:
        print("e")
        result = ''
        if len(fields) != len(values): raise AttributeError("Il doit y avoir autant de champs que de valeurs")
        for i in range(len(fields)):
            print("f")
            if fields[i] != "IdScore" \
               and not (table == "score" and fields[i] == "IdPartie")\
            :
                print(fields[i]+" "+table + " "+str(values[i]))
                if result != '' : result+=","
                if self.getFieldType(fields[i], table) == "string":
                    print("g")
                    result += fields[i]+" = '" + str(values[i]) + "'"
                elif self.getFieldType(fields[i], table) == "int":
                    print("h")
                    result += fields[i]+" = "+str(values[i])
        return result



        
    