from Core_dx_logic import Logic
from Objects_PaisesObj import CountryObj

class PaisesLogic(Logic):
    def __init__(self):
        super().__init__("paises")
        self.idCountry="idPaises"

    def getCountries(self):
        countryList = super().getAllRows(self.tableName)
        countryObjList = []
        for country in countryList:
            newCountry = self.createCountryObj(country)
            countryObjList.append(newCountry)
        return countryObjList

    def createCountryObj(self, countryDict):
        countryObj = CountryObj(
            countryDict["NombrePais"],
            countryDict["CodigoTelefonico"],
            countryDict["idPais"]
        )
        return countryObj

    def insertCountry(self, countryname,code):
        database = self.database
        sql = f"""INSERT INTO airbnb.paises
            (NombrePais, CodigoTelefonico)
            VALUES
            ('{countryname}', '{code}');"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def searchCountryById(self, idCountry):
        rowDict = super().getRowById(self.idName,id,self.tableName)
        newCountry = self.createCountryObj(rowDict)
        return newCountry

    def updateCountryBD(self, id,countryname,code):
        database = self.database
        sql = f"""UPDATE airbnb.paises SET
            NombrePais = '{countryname}', CodigoTelefonico = '{code}'
            WHERE idPais = {id};"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def traerIDCountry(self, countryname, code):
        database = self.database
        sql = f"""SELECT idPais
        FROM paises
        WHERE NombrePais = '{countryname}' AND CodigoTelefonico = '{code}';"""
        id = database.executeQueryOneRow(sql)
        return id["idPais"]

    def deleteCountryDB(self, idCountry):
        super().deleteRowById(self.idCountry, id, self.tableName)
            