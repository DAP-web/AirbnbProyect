import pymysql

class AccesibilidadDB:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="12345",
            db="airbnb",
            cursorclass=pymysql.cursors.DictCursor,
        )
    def getAccessibilities(self):
        result = {}
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM airbnb.accesibilidad;"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def insertAccessibility(self,accessibilityname):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""INSERT INTO airbnb.accesibilidad
                (Nombre)
                VALUES
                ('{accessibilityname}');"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def searchAccessibilityById(self,idAccessibility):
        accesibilidad = {}
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM airbnb.accesibilidad WHERE idAccesibilidad={idAccessibility};"
                cursor.execute(sql)
                accesibilidad = cursor.fetchone()
        finally:
            pass
        return accesibilidad

    def updateAccesibilityBD(self,id,accessibilityname):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""UPDATE airbnb.accesibilidad SET 
                Nombre = '{accessibilityname}'
                WHERE idAccesibilidad = {id};"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def traerIDAccessibility(self,accessibilityname):
        idaccesibilidad = 0
        try:
            with self.connection.cursor() as cursor:
                sql = f"""SELECT idAccesibilidad
                FROM accesibilidad
                WHERE Nombre = '{accessibilityname}' ;"""
                cursor.execute(sql)
                idaccesibilidad = cursor.fetchone()
        finally:
            pass
        return idaccesibilidad["idAccesibilidad"]

    def deleteAccessibilityDB(self,idAccessibility):
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM airbnb.accesibilidad WHERE idAccesibilidad={idAccessibility};"
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass
        