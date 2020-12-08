from Core.Core_dx_logic import Logic
from Objects.Objects_ResidenciaAccesibilidadObj import RAccesibilidadObj
from Objects.Objects_ResidenciaAccesibilidadViewObj import RAccesibilidadesViewObj

class RAccesibilidadLogic(Logic):
    def __init__(self):
        super().__init__("residenciaaccesibilidad")
        self.idName="idRA"
        self.vistaRAccesibilidad = "raccesibilidades"

    def getRAccesibilidades(self):
        RAccesibilidadesList = super().getAllRows(self.vistaRAccesibilidad)
        RAccesibilidadesViewObjList = []
        for raccesibilidades in RAccesibilidadesList:
            newRAccesibilidad = self.createRAccesibilidadViewObj(raccesibilidades)
            RAccesibilidadesViewObjList.append(newRAccesibilidad)
        return RAccesibilidadesViewObjList

    def createRAccesibilidadObj(self,RAccesibilidadesDict):
        RAccesibilidadobj = RAccesibilidadObj(
            RAccesibilidadesDict["IdAccesibilidad"],
            RAccesibilidadesDict["IdResidencia"],
            RAccesibilidadesDict["idRA"]
        )
        return RAccesibilidadobj

    def createRAccesibilidadViewObj(self, RAccesibilidadesDict):
        RAccesibilidadesoviewbj = RAccesibilidadesViewObj(
            RAccesibilidadesDict["IdResidencia"],
            RAccesibilidadesDict["Nombre"],
            RAccesibilidadesDict["Descripcion"],
            RAccesibilidadesDict["idAccesibilidades"]
        )
        return RAccesibilidadesoviewbj

    def agregarRAccesibilidades(self, idAccesibilidad, idResidencia):
        database = self.database
        sql = f"""INSERT INTO `airbnb`.`residenciaaccesibilidad`
        (`IdAccesibilidad`,
        `IdResidencia`)
        VALUES
        ({idAccesibilidad},
        {idResidencia});"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def buscarRAccesibilidadU(self, id):
        rowDict = super().getRowById(self.idName,id,self.tableName)
        newRAccesibilidad = self.createRAccesibilidadObj(rowDict)
        return newRAccesibilidad
    
    def actualizarRAccesibilidad(self, idRA,idAccesibilidad,idResidencia):
        database = self.database
        sql = f"""UPDATE `airbnb`.`residenciaaccesibilidad`
        SET 
        `IdAccesibilidad` = {idAccesibilidad}, 
        `IdResidencia` = {idResidencia} 
        WHERE `idRA` = {idRA};"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def buscarRAccesibilidadV(self, id):
        rowDict = super().getRowById(self.idName,id,self.vistaRAccesibilidad)
        newRAccesibilidad = self.createRAccesibilidadViewObj(rowDict)
        return newRAccesibilidad

    def traerIDAccesibilidad(self, idAccesibilidad,idResidencia):
        database = self.database
        sql = f"""SELECT idRA
        FROM residenciaaccesibilidad
        WHERE IdAccesibilidad={idAccesibilidad} AND IdResidencia={idResidencia};"""
        id = database.executeQueryOneRow(sql)
        return id["idRA"]
    
    def cancelarRAccesibilidad(self, id):
        super().deleteRowById(self.idName, id, self.tableName)
