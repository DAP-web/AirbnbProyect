from Core.Core_dx_logic import Logic
from Objects.Objects_DireccionesObj import DirectionObj
 
class DirectionLogic(Logic):
    def __init__(self):
        super().__init__("direcciones")
        self.idName = "IdDireccion"

    def getDirections(self):
        directionsList= super().getAllRows(self.tableName) 
        directionsObjList = []
        for direction in directionsList:
            newDirection = self.createDirectionObj(direction)
            directionsObjList.append(newDirection)
        return directionsObjList

    def createDirectionObj(self,directionDict):
        directionObj = DirectionObj(
            directionDict["Estado"],
            directionDict["CodigoPostal"],
            directionDict["Calle"],
            directionDict["IdCiudad"],
            directionDict["IdDireccion"]
        )
        return directionObj

    def insertDirection(self,state,postalCode,street,idCity):
        database = self.database
        sql = f"""INSERT INTO airbnb.direcciones
                (Estado,CodigoPostal,Calle,IdCiudad)
                VALUES
                ('{state}',
                '{postalCode}',
                '{street}',
                {idCity});"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def searchDirectionById(self,id):
        rowDict = super().getRowById(self.idName,id,self.tableName)
        newDirection = self.createDirectionObj(rowDict)
        return newDirection

    def updateDirectionBD(self,idDirection, state,postalCode,street,idCity):
        database =self.database
        sql = f"""UPDATE airbnb.direcciones SET 
                Estado = '{state}', CodigoPostal = '{postalCode}', 
                Calle = '{street}', IdCiudad = {idCity}
                WHERE IdDireccion = {idDirection};"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def traerIDDireccion(self,state,postalCode,street,idCity):
        database = self.database
        sql = f"""SELECT IdDireccion
                FROM direcciones
                WHERE Estado = '{state}' AND CodigoPostal = '{postalCode}' AND Calle = '{street}'
                AND IdCiudad = {idCity};"""
        id = database.executeQueryOneRow(sql)
        return id["IdDireccion"]

    def deleteDirectionDB(self,id):
        super().deleteRowById(self.idName,id,self.tableName)