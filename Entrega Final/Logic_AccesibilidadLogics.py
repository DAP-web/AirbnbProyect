from Core_dx_logic import Logic
from Objects_AccesibilidadObj import AccesibilidadesObj
from Objects_AccesibilidadViewObj import AccesibilidadViewObj

class AccesibilidadLogic(Logic):
    def __init__(self):
        super().__init__("accesibilidades")
        self.idName="IdAccesibilidades"
        self.vistaAccesibilidad = "accesibilidades"

    def getAccesibilidad(self):
        accesibilidadesList = super().getAllRows(self.vistaAccesibilidades)
        accesibilidadesViewObjList = []
        for accesibilidades in accesibilidadesList:
            newAccesibilidad = self.createAccesibilidadViewObj(accesibilidades)
            accesibilidadesViewObjList.append(newAccesibilidad)
        return accesibilidadesViewObjList

    def createAccesibilidadObj(self, accesibilidadesDict):
        accesibilidadobj = AccesibilidadesObj(
            accesibilidadesDict["Nombre"],
            accesibilidadesDict["Descripcion"]
        )
        return accesibilidadobj

    def createAccesibilidadViewObj(self, accesibilidadesDict):
        accesibilidadesoviewbj = AccesibilidadViewObj(
            accesibilidadesDict["Nombre"],
            accesibilidadesDict["Descripcion"],
            
        )
        return accesibilidadesoviewbj

    def agendarAccesibilidad(self,idAccesibilidades,strNombre, strDescripcion):
        database = self.database
        sql = f"""INSERT INTO `airbnb`.`accesibilidades`
        (`idAccesibilidades`,
        `Nombre`,
        `Descripcion`)
        VALUES
        ({idAccesibilidades},
        {strNombre},
        {strDescripcion});
        """
        rows = database.executeNonQueryRows(sql)
        return rows

    def buscarAccesibilidadU(self, id):
        rowDict = super().getRowById(self.idName,id,self.tableName)
        newAccesibilidad = self.createAccesibilidadObj(rowDict)
        return newAccesibilidad
    
    def actualizarAccesibilidad(self,id,idAccesibilidades,strNombre,strDescripcion):
        database = self.database
        sql = f"""UPDATE `airbnb`.`accesibilidades`
        SET
        `idAccesibilidades` = <{idAccesibilidades}>,
        `Nombre` = {strNombre},
        `Descripcion` = {strDescripcion}
        WHERE `idAccesibilidades` = {id};


        """
        rows = database.executeNonQueryRows(sql)
        return rows

    def buscarAccesibilidadV(self, id):
        rowDict = super().getRowById(self.idName,id,self.vistaAccesibilidad)
        newAccesibilidad = self.createAccesibilidadObj(rowDict)
        return newAccesibilidad

    def traerIDAccesibilidad(self,idAccesibilidades,strNombre,strDescripcion):
        database = self.database
        sql = f"""SELECT IdAccesibilidades
        FROM accesibilidades
        WHERE IdAccesibilidades{idAccesibilidades} AND Nombre={strNombre} AND Descripcion='{strDescripcion}' ;
        """
        id = database.executeQueryOneRow(sql)
        return id["IdAccesibilidades"]
    
    def cancelarAccesibilidad(self, id):
        super().deleteRowById(self.idName, id, self.tableName)

    def chequeoCancelacion(self,idAccesibilidades):
        reservas={}
        database=self.database
        sql = f"SELECT IdAccesibilidades FROM airbnb.accesibilidades WHERE IdAccesibilidades={idAccesibilidades};"
        accesibilidades = database.executeQueryOneRow(sql)
        return accesibilidades["IdAccesibilidades"]