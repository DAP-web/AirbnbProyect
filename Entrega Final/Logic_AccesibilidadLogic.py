from Core_dx_logic import Logic
from Objects_AccesibilidadObj import AccesibilidadesObj

class AccesibilidadLogic(Logic):
    def __init__(self):
        super().__init__("accesibilidades")
        self.idName="idAccesibilidades"

    def getAccesibilidades(self):
        accesibilidadesList = super().getAllRows(self.tableName)
        accesibilidadesObjList = []
        for accesibilidades in accesibilidadesList:
            newAccesibilidad = self.createAccesibilidadObj(accesibilidades)
            accesibilidadesObjList.append(newAccesibilidad)
        return accesibilidadesObjList

    def createAccesibilidadObj(self, accesibilidadesDict):
        accesibilidadobj = AccesibilidadesObj(
            accesibilidadesDict["Nombre"],
            accesibilidadesDict["Descripcion"],
            accesibilidadesDict["idAccesibilidades"]
        )
        return accesibilidadobj

    def agregarAccesibilidad(self, strNombre, strDescripcion):
        database = self.database
        sql = f"""INSERT INTO `airbnb`.`accesibilidades`
        (`Nombre`,
        `Descripcion`)
        VALUES
        ('{strNombre}',
        '{strDescripcion}');
        """
        rows = database.executeNonQueryRows(sql)
        return rows

    def buscarAccesibilidadU(self, id):
        rowDict = super().getRowById(self.idName,id,self.tableName)
        newAccesibilidad = self.createAccesibilidadObj(rowDict)
        return newAccesibilidad
    
    def actualizarAccesibilidad(self,id, strNombre, strDescripcion):
        database = self.database
        sql = f"""UPDATE `airbnb`.`accesibilidades` 
        SET `Nombre` = '{strNombre}', 
        `Descripcion` = '{strDescripcion}' 
        WHERE `idAccesibilidades` = {id};"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def buscarAccesibilidadV(self, id):
        rowDict = super().getRowById(self.idName,id,self.tableName)
        newAccesibilidad = self.createAccesibilidadObj(rowDict)
        return newAccesibilidad

    def traerIDAccesibilidad(self, strNombre, strDescripcion):
        database = self.database
        sql = f"""SELECT idAccesibilidades
        FROM accesibilidades
        WHERE Nombre='{strNombre}' AND Descripcion='{strDescripcion}' ;
        """
        id = database.executeQueryOneRow(sql)
        return id["idAccesibilidades"]
    
    def eliminarAccesibilidad(self, id):
        super().deleteRowById(self.idName, id, self.tableName)
