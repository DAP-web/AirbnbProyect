from Core_dx_logic import Logic
from Objects_ResidenciaObj import ResidenciaObj


class ResidenciaLogic(Logic):
    def __init__(self):
        super().__init__("residencias")
        self.idName = "idResidencia"

    def getResidencias(self):
        residenciaList = super().getAllRows(self.tableName)
        residenciaObjList = []
        for residencia in residenciaList:
            newResidencia = self.createResidenciaObj(residencia)
            residenciaObjList.append(newResidencia)
        return residenciaObjList

    def createResidenciaObj(self, residenciaDict):
        residenciaObj = ResidenciaObj(
            residenciaDict["TipoAlojamiento"],
            residenciaDict["Habitaciones"],
            residenciaDict["Banhos"],
            residenciaDict["Camas"],
            residenciaDict["IdDireccion"],
            residenciaDict["Precio"],
            residenciaDict["FlexibilidadDeCancelacion"],
            residenciaDict["AirbnbPlus"],
            residenciaDict["Mascotas"],
            residenciaDict["Fumadores"],
            residenciaDict["idResidencia"],
        )
        return residenciaObj

    def insertResidencias(
        self,
        tipo,
        rooms,
        bathrooms,
        beds,
        direction,
        price,
        cancelation,
        plus,
        pets,
        smokers,
    ):
        database = self.database
        sql = f"""INSERT INTO airbnb.residencias
                (TipoAlojamiento,
                Habitaciones,
                Banhos,
                Camas,
                IdDireccion,
                Precio,
                FlexibilidadDeCancelacion,
                AirbnbPlus,
                Mascotas,
                Fumadores)
                VALUES
                ('{tipo}',
                {rooms},
                {bathrooms},
                {beds},
                {direction},
                {price},
                {cancelation},
                {plus},
                {pets},
                {smokers});"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def searchResidenciasById(self, idResidencia):
        rowDict = super().getRowById(self.idName, idResidencia, self.tableName)
        newUser = self.createResidenciaObj(rowDict)
        return newUser

    def updateResidenciaBD(
        self, id, tipo, rooms, bathrooms, beds, price, cancelation, plus, pets, smokers
    ):
        database = self.database
        sql = f"""UPDATE airbnb.residencias SET 
                TipoAlojamiento = '{tipo}', Habitaciones = {rooms}, 
                Banhos = {bathrooms}, Camas = {beds}, Precio = {price}, 
                FlexibilidadDeCancelacion = {cancelation}, AirbnbPlus = {plus}, 
                Mascotas = {pets}, Fumadores = {smokers}
                WHERE idResidencia = {id};"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def traerIDResidencia(
        self,
        tipo,
        rooms,
        bathrooms,
        beds,
        direction,
        price,
        cancelation,
        plus,
        pets,
        smokers,
    ):
        database = self.database
        sql = f"""SELECT idResidencia
                FROM residencias
                WHERE TipoAlojamiento = '{tipo}' AND Habitaciones = {rooms} AND Banhos = {bathrooms} 
                AND Camas = {beds} AND IdDireccion = {direction} AND Precio = {price} 
                AND FlexibilidadDeCancelacion = {cancelation} AND AirbnbPlus = {plus} AND Mascotas = {pets} 
                AND Fumadores = {smokers};"""
        id = database.executeQueryOneRow(sql)
        return id["idResidencia"]

    def deleteResidenciaDB(self, idResidencia):
        super().deleteRowById(self.idName, idResidencia, self.tableName)

    # Esta funcion es parte de la funcionalidad de la tabla de Reservas

    def chequeoFlexCancelacion(self, idResidencia):
        residencia = {}
        database = self.database
        sql = f"SELECT FlexibilidadDeCancelacion FROM airbnb.residencias WHERE idResidencia={idResidencia};"
        residencia = database.executeQueryOneRow(sql)
        return residencia

    # Esta función es de procesos no de tablas
    # Cuando un cliente quiera agendar una reserva se le solicita el pais al que viaja
    # y se llama a este metodo para mostrarle todas las residencias que se encuentran en ese pais
    def busquedaDeResidencias(self, pais):
        result = {}
        database = self.database
        sql = f"""select residencias.idResidencia,residencias.TipoAlojamiento,residencias.Habitaciones,residencias.Banhos,
            residencias.Camas,residencias.Precio,residencias.FlexibilidadDeCancelacion,residencias.AirbnbPlus,
            residencias.Mascotas,residencias.Fumadores
        from residencias
            inner join direcciones on residencias.IdDireccion=direcciones.IdDireccion
            inner join ciudades on direcciones.IdCiudad=ciudades.idCiudad
            inner join paises on ciudades.IdPais=paises.idPais
            where paises.NombrePais='{pais}';"""
        result = database.executeQueryOneRow(sql)
        return result

    def verResidenciaEspecifica(self, id):
        result = {}
        database = self.database
        sql = f"""select residencias.idResidencia,residencias.TipoAlojamiento,residencias.Habitaciones,residencias.Banhos,
                residencias.Camas,residencias.Precio,residencias.FlexibilidadDeCancelacion,residencias.AirbnbPlus,
                residencias.Mascotas,residencias.Fumadores,direccioncompleta.Estado,
                direccioncompleta.CodigoPostal,direccioncompleta.Calle,
                direccioncompleta.NombreCiudad,direccioncompleta.NombrePais
            from residencias
                inner join direccioncompleta on residencias.IdDireccion=direccioncompleta.IdDireccion
            where residencias.idResidencia={id};"""
        result = database.executeQueryOneRow(sql)
        return result
