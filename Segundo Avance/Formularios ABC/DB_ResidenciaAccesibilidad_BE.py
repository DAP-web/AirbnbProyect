import pymysql

class DBRA:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="12345",
            db="airbnb",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def getRAccessibilities(self):
        result = {}
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * airbnb.raccesibilidades;"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def insertRAccessibility(self, idaccesibilidad, idresidencia):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""INSERT INTO airbnb.residenciaaccesibilidad
                (idAccesibilidad,
                IdResidencia)
                VALUES
                ('{idaccesibilidad}',
                '{idresidencia}');"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def searchRAccessibility(self, idaccesibilidad, idresidencia):
        raccesibilidad = {}
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM  airbnb.raccesibilidades WHERE idAccesibilidad={idaccesibilidad} AND idResidencia={idresidencia} ;"
                cursor.execute(sql)
                raccesibilidad = cursor.fetchone()
        finally:
            pass
        return raccesibilidad

    def updateRAccessibilityBD(self, id,idaccesibilidad,idresidencia):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""UPDATE airbnb.residenciaaccesibilidad  SET 
                IdRA='{id}',IdAccesibilidad = '{idaccesibilidad}', IResidencia = '{idresidencia}'
                WHERE idRA = {id};"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def traerIDRAccessibility(self, idaccesibilidad, idresidencia):
        idraccesibilidad = 0
        try:
            with self.connection.cursor() as cursor:
                sql = f"""SELECT idRA
                FROM residenciaaccesibilidad
                WHERE idAccesibilidad = '{idaccesibilidad}' AND IdResidencia = '{idresidencia}';"""
                cursor.execute(sql)
                idraccesibilidad = cursor.fetchone()
        finally:
            pass
        return idraccesibilidad["idRA"]

    def deleteRAccessibilityDB(self, idraccesibilidad):
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM airbnb.residenciaaccesibilidad WHERE idAccesibilidad={idraccesibilidad};"
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass