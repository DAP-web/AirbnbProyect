from Core.Core_dx_logic import Logic
from Objects.Objects_ResidenciaObj import ResidenciaObj
from Objects.Objects_CiudadesObj import CityObj
from Objects.Objects_PaisesObj import CountryObj
from Objects.Objects_DireccionesObj import DirectionObj

class ResidenciaServicioLogic(Logic):
    def __init__(self):
        super().__init__("residenciaservicio")
        self.idName = "idRS"

    def getResidenciaServicio(self):
        resiservList = super().getAllRows(self.tableName)
        resiservObjList = []
        for residenciaservicio in resiservList:
            newResiServ = self.createResiServObj(residenciaservicio)
            resiservObjList.append(newResidencia)
        return resiservObjList

    def createResidenciaServicioObj(self, residenciaservicio):
        resiservObj = ResidenciaServicioObj(
            residenciaservicio["IdServicio"],
            residenciaservicio["IdResidencia"],
            residenciaservicio["idRS"]
        )
        return resiservObj

    def insertResidenciaServicio(self, idServicio, idResidencia):
        database = self.database
        sql = f"""INSERT INTO airbnb.residenciaservicio
        (IdServicio,
        IdResidencia)
        VALUES
        ('{idServicio}',
        {idResidencia});"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def searchResidenciaServicioById(self, idRS):
        rowDict = super().getRowById(self.idName, idRS, self.tableName)
        newUser = self.createResiServObj(rowDict)
        return newUser

    def updateResidenciaServicioBD(self, id, idServicio, idResidencia
    ):
        database = self.database
        sql = f"""UPDATE airbnb.residenciaservicio SET 
        IdServicio = '{idServicio}', IdResidencia = {idResidencia}
        WHERE idRS = {id};"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def traerIDResidenciaServicio(self, idServicio, idResidencia):
        database = self.database
        sql = f"""SELECT idResidencia
        FROM residenciaservicio
        WHERE IdServicio = '{idServicio}' AND IdResidencia = {idResidencia};"""
        id = database.executeQueryOneRow(sql)
        return id["idRS"]

    def deleteResidenciaServicioDB(self, idRS):
        super().deleteRowById(self.idName, idRS, self.tableName)

    # Esta función es de procesos no de tablas
    # Cuando un cliente quiera agendar una reserva se le solicita el pais al que viaja
    # y se llama 
    # a este metodo para mostrarle todas las residencias que se encuentran en ese pais
    #def busquedaDeResidencias(self, pais):
        #database = self.database
        #sql = f"""select residencias.idResidencia,residencias.TipoAlojamiento,residencias.Habitaciones,residencias.Banhos,
            #residencias.Camas,residencias.Precio,residencias.FlexibilidadDeCancelacion,residencias.AirbnbPlus,
            #residencias.Mascotas,residencias.Fumadores
        #from residencias
            #inner join direcciones on residencias.IdDireccion=direcciones.IdDireccion
            #inner join ciudades on direcciones.IdCiudad=ciudades.idCiudad
            #inner join paises on ciudades.IdPais=paises.idPais
            #where paises.NombrePais='{pais}';"""
        #resultList = database.executeQueryRows(sql)
        #result = []
        #for residencia in resultList:
            #newResidencia = self.createResidenciaObjProceso(residencia)
            #result.append(newResidencia)
        #return result

    #def createResidenciaObjProceso(self, residenciaDict):
        #residenciaObj = ResidenciaObj(
            #residenciaDict["TipoAlojamiento"],
            #residenciaDict["Habitaciones"],
            #residenciaDict["Banhos"],
            #residenciaDict["Camas"],
            #residenciaDict["Precio"],
            #residenciaDict["FlexibilidadDeCancelacion"],
            #residenciaDict["AirbnbPlus"],
            #residenciaDict["Mascotas"],
            #residenciaDict["Fumadores"],
            #residenciaDict["idResidencia"]
        #)
        #return residenciaObj

    #def verResidenciaEspecifica(self, id):
        #result = {}
        #database = self.database
        #sql = f"""select residencias.idResidencia,residencias.TipoAlojamiento,residencias.Habitaciones,residencias.Banhos,
            #residencias.Camas,residencias.Precio,residencias.FlexibilidadDeCancelacion,residencias.AirbnbPlus,
            #residencias.Mascotas,residencias.Fumadores,direcciones.Estado,
            #direcciones.CodigoPostal,direcciones.Calle,
            #ciudades.NombreCiudad,paises.NombrePais
        #from residencias
            #inner join direcciones on residencias.IdDireccion = direcciones.IdDireccion
            #inner join ciudades on direcciones.idCiudad = ciudades.idCiudad
            #inner join paises on ciudades.IdPais = paises.IdPais
        #where residencias.idResidencia={id};"""
        #result = database.executeQueryOneRow(sql)
        #return result
