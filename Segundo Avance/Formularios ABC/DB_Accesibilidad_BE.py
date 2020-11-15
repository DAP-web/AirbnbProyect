import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="airbnb",
    cursorclass=pymysql.cursors.DictCursor,
)

def getAccessibilities():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM airbnb.accesibilidad;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result

def insertAccessibility(accessibilityname):
    try:
        with connection.cursor() as cursor:
            sql = f"""INSERT INTO airbnb.accesibilidad
            (Nombre)
            VALUES
            ('{accessibilityname}');"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def searchAccessibilityById(idAccessibility):
    accesibilidad = {}
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM airbnb.accesibilidad WHERE idAccesibilidad={idAccessibility};"
            cursor.execute(sql)
            accesibilidad = cursor.fetchone()
    finally:
        pass
    return accesibilidad

def updateAccesibilityBD(id,accessibilityname):
    try:
        with connection.cursor() as cursor:
            sql = f"""UPDATE airbnb.accesibilidad SET 
            Nombre = '{accessibilityname}'
            WHERE idAccesibilidad = {id};"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def traerIDAccessibility(accessibilityname):
    idaccesibilidad = 0
    try:
        with connection.cursor() as cursor:
            sql = f"""SELECT idAccesibilidad
            FROM accesibilidad
            WHERE Nombre = '{accessibilityname}' ;"""
            cursor.execute(sql)
            idaccesibilidad = cursor.fetchone()
    finally:
        pass
    return idaccesibilidad["idAccesibilidad"]

def deleteAccessibilityDB(idAccessibility):
    try:
        with connection.cursor() as cursor:
            sql = f"DELETE FROM airbnb.accesibilidad WHERE idAccesibilidad={idAccessibility};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
        