from Core_dx_logic import Logic
from Objects_CiudadesObj import CityObj

class CiudadesLogic(Logic):
    def __init__(self):
        super().__init__("ciudades")
        self.idName="idCiudad"

    def getCities(self):
        cityList = super().getAllRows(self.tableName)
        cityObjList = []
        for city in cityList:
            newCity = self.createCityObj(city)
            cityObjList.append(newCity)
        return cityObjList

    def createCityObj(self, cityDict):
        cityObj = CityObj(
            cityDict["NombreCiudad"],
            cityDict["IdPais"],
            cityDict["idCiudad"]
        )
        return cityObj

    def insertCity(self, cityname,idcountry):
        database = self.database
        sql = f"""INSERT INTO airbnb.ciudades
            (NombreCiudad, IdPais)
            VALUES
            ('{cityname}', '{idcountry}');"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def searchCityById(self, idCity):
        rowDict = super().getRowById(self.idName,idCity,self.tableName)
        newCity = self.createCityObj(rowDict)
        return newCity

    def updateCityBD(self, id,cityname, idcountry):
        database = self.database
        sql = f"""UPDATE airbnb.ciudades SET
            NombreCiudad = '{cityname}', IdPais = {idcountry}
            WHERE idCiudad = {id};"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def traerIDCity(self, cityname, idcountry):
        database = self.database
        sql = f"""SELECT idCiudad
        FROM ciudades
        WHERE NombreCiudad = '{cityname}' AND IdPais = '{idcountry}';"""
        id = database.executeQueryOneRow(sql)
        return id["idCiudad"]

    def deleteCityDB(self, idCiudad):
        super().deleteRowById(self.idName, id, self.tableName)