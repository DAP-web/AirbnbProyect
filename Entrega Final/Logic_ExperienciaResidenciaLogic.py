from Core_dx_logic import Logic
from Objects_ExperienciaResidenciaObj import ExperienciaResidenciaObj


class ExperienciaResidenciaLogic(Logic):
    def __init__(self):
        super().__init__("experienciaresidencia")
        self.idName = "idER"

    def getExperienciaResidencias(self):
        experienciaResidenciaList = super().getAllRows(self.tableName)
        experienciaResidenciaObjList = []
        for experienciaResidencia in experienciaResidenciaList:
            newExperienciaResidencia = self.createExperienciaResidenciaObj(
                experienciaResidencia
            )
            experienciaResidenciaObjList.append(newExperienciaResidencia)
        return experienciaResidenciaObjList

    def createExperienciaResidenciaObj(self, experienciaResidenciaDict):
        experienciaResidenciaObj = ExperienciaResidenciaObj(
            experienciaResidenciaDict["IdExp"],
            experienciaResidenciaDict["IdResidencia"],
            experienciaResidenciaDict["idER"],
        )
        return experienciaResidenciaObj

    def insertExperienciaResidencias(self, IdExp, IdResidencia):
        database = self.database
        sql = f"""INSERT INTO airbnb.experienciaresidencia
            (IdExp,
            IdResidencia)
            VALUES
            ('{IdExp}',
            {IdResidencia});"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def searchExperienciaResidenciasById(self, idER):
        rowDict = super().getRowById(self.idName, idER, self.tableName)
        newUser = self.createExperienciaResidenciaObj(rowDict)
        return newUser

    def updateExperienciaResidenciaBD(self, id, idExp, idResidencia):
        database = self.database
        sql = f"""UPDATE airbnb.experienciaresidencia SET 
        IdExp = {idExp}, IdResidencia = {idResidencia} 
        WHERE idER = {id};"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def traerIDExperienciaResidencia(self, IdExp, idResidencia):
        database = self.database
        sql = f"""SELECT idER
        FROM experienciaresidencia
        WHERE IdExp = {IdExp} AND IdResidencia = {idResidencia};"""
        id = database.executeQueryOneRow(sql)
        return id["idER"]

    def deleteExperienciaResidenciaDB(self, id):
        super().deleteRowById(self.idName, id, self.tableName)
