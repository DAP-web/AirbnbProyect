import pymysql

class direccionesDB:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="12345",
            db="airbnb",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def getDirections(self):
        result = {}
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM airbnb.direcciones;"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def insertDirection(self,state,postalCode,street,idCity):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""INSERT INTO airbnb.direcciones
                (Estado,CodigoPostal,Calle,IdCiudad)
                VALUES
                ('{state}',
                '{postalCode}',
                '{street}',
                {idCity});"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def searchDirectionById(self,idDireccion):
        direccion = {}
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM airbnb.direcciones WHERE IdDireccion={idDireccion};"
                cursor.execute(sql)
                direccion = cursor.fetchone()
        finally:
            pass
        return direccion

    def updateDirectionBD(self,idDirection, state,postalCode,street,idCity):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""UPDATE airbnb.direcciones SET 
                Estado = '{state}', CodigoPostal = '{postalCode}', Calle = '{street}', idCiudad = {idCity}
                WHERE IdDireccion = {idDirection};"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def traerIDDireccion(self,state,postalCode,street,idCity):
        iddirreccion = 0
        try:
            with self.connection.cursor() as cursor:
                sql = f"""SELECT IdDireccion
                FROM direcciones
                WHERE Estado = '{state}' AND CodigoPostal = '{postalCode}' AND Calle = '{street}' 
                AND idCiudad = {idCity};"""
                cursor.execute(sql)
                iddirreccion = cursor.fetchone()
        finally:
            pass
        return iddirreccion["IdDireccion"]

    def deleteDirectionDB(self,idDirection):
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM airbnb.direcciones WHERE IdDireccion={idDirection};"
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass