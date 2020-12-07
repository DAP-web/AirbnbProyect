from Core_dx_logic import Logic
from Objects_ResidenciaAccesibilidadObj import RAccesibilidadObj
from Objects_ResidenciaAccesibilidadViewObj import RAccesibilidadesViewObj

class RAccesibilidadLogic(Logic):
    def __init__(self):
        super().__init__("raccesibilidades")
        self.idName="IdRA"
        self.vistaRAccesibilidad = "raccesibilidades"

    def getRAccesibilidad(self):
        RAccesibilidadesList = super().getAllRows(self.vistaRAccesibilidades)
        RAccesibilidadesViewObjList = []
        for raccesibilidades in RAccesibilidadesList:
            newRAccesibilidad = self.createRAccesibilidadViewObj(raccesibilidades)
            RAccesibilidadesViewObjList.append(newRAccesibilidad)
        return RAccesibilidadesViewObjList

    def createRAccesibilidadObj(self,RAccesibilidadesDict):
        RAccesibilidadobj = RAccesibilidadObj(
            RAccesibilidadesDict["idAccesibilidad"],
            RAccesibilidadesDict["idResidencia"]
        )
        return RAccesibilidadobj

    def createAccesibilidadViewObj(self, RAccesibilidadesDict):
        RAccesibilidadesoviewbj = RAccesibilidadesViewObj(
            RAccesibilidadesDict["idAccesibilidad"],
            RAccesibilidadesDict["idResidencia"],
            
        )
        return RAccesibilidadesoviewbj

    def agregarRAccesibilidad(self,idRA,idAccesibilidad, idResidencia):
        database = self.database
        sql = f"""INSERT INTO `airbnb`.`residenciaaccesibilidad`
        (`idRA`,
        `IdAccesibilidad`,
        `IdResidencia`)
        VALUES
        ({idRA},
        {idAccesibilidad},
        {idResidencia});

        """
        rows = database.executeNonQueryRows(sql)
        return rows

    def buscarRAccesibilidadU(self, id):
        rowDict = super().getRowById(self.idName,id,self.tableName)
        newRAccesibilidad = self.createRAccesibilidadObj(rowDict)
        return newRAccesibilidad
    
    def actualizarRAccesibilidad(self,id,idRA,idAccesibilidad,idResidencia):
        database = self.database
        sql = f"""UPDATE `airbnb`.`residenciaaccesibilidad`
        SET
        `idRA` = {idRA},
        `IdAccesibilidad` = <{idAccesibilidad}>,
        `IdResidencia` = {idResidencia}
        WHERE `idRA` = <{id}>;



        """
        rows = database.executeNonQueryRows(sql)
        return rows

    def buscarRAccesibilidadV(self, id):
        rowDict = super().getRowById(self.idName,id,self.vistaRAccesibilidad)
        newRAccesibilidad = self.createRAccesibilidadObj(rowDict)
        return newRAccesibilidad

    def traerIDAccesibilidad(self,idRA,idAccesibilidad,idResidencia):
        database = self.database
        sql = f"""SELECT IdRA
        FROM residenciaaccesibilidad
        WHERE IdRA{idRA} AND IDAccesibilidad={idAccesibilidad} AND IDResidencia='{idResidencia}' ;
        """
        id = database.executeQueryOneRow(sql)
        return id["IdRA"]
    
    def cancelarRAccesibilidad(self, id):
        super().deleteRowById(self.idName, id, self.tableName)

    def chequeoCancelacion(self,idRA):
        reservas={}
        database=self.database
        sql = f"SELECT IdRA FROM airbnb.residenciaaccesibilidad WHERE IdRA={idRA};"
        RAccesibilidades = database.executeQueryOneRow(sql)
        return RAccesibilidades["IdRA"]