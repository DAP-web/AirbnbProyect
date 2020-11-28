import pymysql

class Desc_AccesibilidadDB:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="12345",
            db="airbnb",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def getDescription(self):
        result = {}
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM airbnb.desc_accesibilidad;"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def insertDescription(self,description, accesibility):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""INSERT INTO airbnb.desc_accesibilidad
                (Descripcion, IdAccesibilidad)
                VALUES
                ('{description}', {accesibility});"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def searchDesc_AccesibilidadById(self,idDescAccesibilidad):
        accesibilidades = {}
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM airbnb.desc_accesibilidad WHERE idDA={idDescAccesibilidad};"
                cursor.execute(sql)
                accesibilidades = cursor.fetchone()
        finally:
            pass
        return accesibilidades

    def updateDescriptionBD(self,id,description):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""UPDATE airbnb.desc_accesibilidad SET 
                Descripcion = '{description}'
                WHERE idDA = {id};"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def deleteDescriptionBD(self,idDA):
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM airbnb.desc_accesibilidad WHERE idDA={idDA};"
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass