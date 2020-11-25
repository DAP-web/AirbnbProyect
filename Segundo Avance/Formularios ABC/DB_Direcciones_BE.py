import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="airbnb",
    cursorclass=pymysql.cursors.DictCursor,
)

def getDirections():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM airbnb.direcciones;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result

def insertDirection(state,postalCode,street,idCity):
    try:
        with connection.cursor() as cursor:
            sql = f"""INSERT INTO airbnb.direcciones
            (Estado,CodigoPostal,Calle,IdCiudad)
            VALUES
            ('{state}',
            '{postalCode}',
            '{street}',
            {idCity});"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def searchDirectionById(idDireccion):
    direccion = {}
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM airbnb.direcciones WHERE IdDireccion={idDireccion};"
            cursor.execute(sql)
            direccion = cursor.fetchone()
    finally:
        pass
    return direccion

def updateDirectionBD(idDirection, state,postalCode,street,idCity):
    try:
        with connection.cursor() as cursor:
            sql = f"""UPDATE airbnb.direcciones SET 
            Estado = '{state}', CodigoPostal = '{postalCode}', Calle = '{street}', idCiudad = {idCity}
            WHERE IdDireccion = {idDirection};"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def traerIDDireccion(state,postalCode,street,idCity):
    iddirreccion = 0
    try:
        with connection.cursor() as cursor:
            sql = f"""SELECT IdDireccion
            FROM direcciones
            WHERE Estado = '{state}' AND CodigoPostal = '{postalCode}' AND Calle = '{street}' 
            AND idCiudad = {idCity};"""
            cursor.execute(sql)
            iddirreccion = cursor.fetchone()
    finally:
        pass
    return iddirreccion["IdDireccion"]

def deleteDirectionDB(idDirection):
    try:
        with connection.cursor() as cursor:
            sql = f"DELETE FROM airbnb.direcciones WHERE IdDireccion={idDirection};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass