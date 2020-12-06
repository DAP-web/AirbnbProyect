from Core_dx_logic import Logic
from Objects_TematicaObj import TematicaObj

class TematicaLogic(Logic):
    def __init__(self):
        super().__init__("tematica")
        self.idName="idTematica"

    def getTematicas(self):
        tematicaList = super().getAllRows(self.tableName)
        tematicaObjList = []
        for tematica in tematicaList:
            newTematica = self.createTematicaObj(tematica)
            tematicaObjList.append(newTematica)
        return tematicaObjList

    def insertTematica(self,tematicaname,description):
        database = self.database
        sql = f"""INSERT INTO airbnb.tematica
                (NombreTematica,
                Descripcion)
                VALUES
                ('{tematicaname}',
                '{description}');"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def searchTematicaById(self,id):
        rowDict = super().getRowById(self.idName,id,self.tableName)
        newTematic = self.createTematicaObj(rowDict)
        return newTematic

    def updateTematicaBD(self,id,tematicaname,description):
        database = self.database
        sql = f"""UPDATE airbnb.tematica SET 
        NombreTematica = '{tematicaname}', Descripcion = '{description}'
        WHERE idTematica = {id};"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def traerIDTematica(self,tematicaname, description):
        database = self.database
        sql = f"""SELECT idTematica
        FROM tematica
        WHERE NombreTematica = '{tematicaname}' AND Descripcion = '{description}';"""
        id = database.executeQueryOneRow(sql)
        return id["idTematica"]

    def deleteTematicaDB(self,id):
        super().deleteRowById(self.idName, id, self.tableName)