import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="airbnb",
    cursorclass=pymysql.cursors.DictCursor,
)

def getCountries():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM airbnb.paises;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result

def insertCountry(countryname,code):
    try:
        with connection.cursor() as cursor:
            sql = f"""INSERT INTO airbnb.paises
            (NombrePais,
            CodigoTelefonico)
            VALUES
            ('{countryname}',
            '{code}');"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def searchCountryById(idCountry):
    pais = {}
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM airbnb.paises WHERE idPais={idCountry};"
            cursor.execute(sql)
            pais = cursor.fetchone()
    finally:
        pass
    return pais

def updateCountryBD(id,countryname,code):
    try:
        with connection.cursor() as cursor:
            sql = f"""UPDATE airbnb.paises SET 
            NombrePais = '{countryname}', CodigoTelefonico = '{code}'
            WHERE idPais = {id};"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def traerIDCountry(countryname, code):
    idpais = 0
    try:
        with connection.cursor() as cursor:
            sql = f"""SELECT idPais
            FROM paises
            WHERE NombrePais = '{countryname}' AND Codigotelefonico = '{code}';"""
            cursor.execute(sql)
            idpais = cursor.fetchone()
    finally:
        pass
    return idpais["idPais"]

def deleteCountryDB(idCountry):
    try:
        with connection.cursor() as cursor:
            sql = f"DELETE FROM airbnb.paises WHERE idPais={idCountry};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
        