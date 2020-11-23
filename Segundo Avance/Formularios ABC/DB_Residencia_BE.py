import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="airbnb",
    cursorclass=pymysql.cursors.DictCursor,
)

def getResidencias():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM airbnb.residencias;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result


def insertResidencias(tipo, rooms, bathrooms, beds, direction, price, cancellation, plus, pets, smokers):
    try:
        with connection.cursor() as cursor:
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
            {cancellation},
            {plus},
            {pets},
            {smokers});"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def searchResidenciasById(idResidencia):
    residencia = {}
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM airbnb.residencias WHERE idResidencia={idResidencia};"
            cursor.execute(sql)
            residencia = cursor.fetchone()
    finally:
        pass
    return residencia


def updateResidenciaBD(id,tipo,rooms,bathrooms,beds,price,cancellation,plus,pets,smokers):
    try:
        with connection.cursor() as cursor:
            sql = f"""UPDATE airbnb.residencias SET 
            TipoAlojamiento = '{tipo}', Habitaciones = {rooms}, 
            Banhos = {bathrooms}, Camas = {beds}, Precio = {price}, 
            FlexibilidadDeCancelacion = {cancellation}, AirbnbPlus = {plus}, 
            Mascotas = {pets}, Fumadores = {smokers}
            WHERE idResidencia = {id};"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def traerIDResidencia(tipo, rooms, bathrooms, beds, direction, price, cancellation, plus, pets, smokers):
    idresidencia = 0
    try:
        with connection.cursor() as cursor:
            sql = f"""SELECT idResidencia
            FROM residencias
            WHERE TipoAlojamiento = '{tipo}' AND Habitaciones = {rooms} AND Banhos = {bathrooms} 
            AND Camas = {beds} AND IdDireccion = {direction} AND Precio = {price} 
            AND FlexibilidadDeCancelacion = {cancellation} AND AirbnbPlus = {plus} AND Mascotas = {pets} 
            AND Fumadores = {smokers};"""
            cursor.execute(sql)
            idresidencia = cursor.fetchone()
    finally:
        pass
    return idresidencia["idResidencia"]


def deleteResidenciaDB(idResidencia):
    try:
        with connection.cursor() as cursor:
            sql = f"DELETE FROM airbnb.residencias WHERE idResidencia={idResidencia};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
#Esta funcion es parte de la funcionalidad de la tabla Reservaciones
def chequeoFlexCancelacion(idResidencia):
    residencia = {}
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT FlexibilidadDeCancelacion FROM airbnb.residencias WHERE idResidencia={idResidencia};"
            cursor.execute(sql)
            residencia = cursor.fetchone()
    finally:
        pass
    return residencia

#Esta función es de procesos no de tablas
#Cuando un cliente quiera agendar una reserva se le solicita el pais al que viaja
#y se llama a este metodo para mostrarle todas las residencias que se encuentran en ese pais
def busquedaDeResidencias(pais):
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = f"""select residencias.idResidencia,residencias.TipoAlojamiento,residencias.Habitaciones,residencias.Banhos,
	            residencias.Camas,residencias.Precio,residencias.FlexibilidadDeCancelacion,residencias.AirbnbPlus,
                residencias.Mascotas,residencias.Fumadores
            from residencias
	            inner join direcciones on residencias.IdDireccion=direcciones.IdDireccion
                inner join ciudades on direcciones.IdCiudad=ciudades.idCiudad
                inner join paises on ciudades.IdPais=paises.idPais
            where paises.NombrePais='{pais}';"""
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result

def verResidenciaEspecifica(id):
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = f"""select residencias.idResidencia,residencias.TipoAlojamiento,residencias.Habitaciones,residencias.Banhos,
	            residencias.Camas,residencias.Precio,residencias.FlexibilidadDeCancelacion,residencias.AirbnbPlus,
                residencias.Mascotas,residencias.Fumadores,direccioncompleta.Estado,
                direccioncompleta.CodigoPostal,direccioncompleta.Calle,
                direccioncompleta.NombreCiudad,direccioncompleta.NombrePais
            from residencias
	            inner join direccioncompleta on residencias.IdDireccion=direccioncompleta.IdDireccion
            where residencias.idResidencia={id};"""
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result