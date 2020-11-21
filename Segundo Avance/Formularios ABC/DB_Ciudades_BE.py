import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="airbnb",
    cursorclass=pymysql.cursors.DictCursor,
)

def getCities():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM airbnb.ciudadpais;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result

def insertCity(cityname, idcountry):
    try:
        with connection.cursor() as cursor:
            sql = f"""INSERT INTO airbnb.ciudades
            (NombreCiudad,
            IdPais)
            VALUES
            ('{cityname}',
            '{idcountry}');"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def searchCityById(idCity):
    ciudad = {}
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM airbnb.ciudades WHERE idCiudad={idCity};"
            cursor.execute(sql)
            ciudad = cursor.fetchone()
    finally:
        pass
    return ciudad

def updateCityBD(id,cityname,idcountry):
    try:
        with connection.cursor() as cursor:
            sql = f"""UPDATE airbnb.ciudades SET 
            NombreCiudad = '{cityname}', IdPais = '{idcountry}'
            WHERE idCiudad = {id};"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def traerIDCity(cityname, idcountry):
    idciudad = 0
    try:
        with connection.cursor() as cursor:
            sql = f"""SELECT idCiudad
            FROM ciudades
            WHERE NombreCiudad = '{cityname}' AND IdPais = '{idcountry}';"""
            cursor.execute(sql)
            idciudad = cursor.fetchone()
    finally:
        pass
    return idciudad["idCiudad"]

def deleteCityDB(idCity):
    try:
        with connection.cursor() as cursor:
            sql = f"DELETE FROM airbnb.ciudades WHERE idCiudad={idCity};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass