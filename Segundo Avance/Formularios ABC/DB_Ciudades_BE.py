import pymysql

class DBCiudades:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="12345",
            db="airbnb",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def getCities(self):
        result = {}
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM airbnb.ciudadpais;"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def insertCity(self, cityname, idcountry):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""INSERT INTO airbnb.ciudades
                (NombreCiudad,
                IdPais)
                VALUES
                ('{cityname}',
                '{idcountry}');"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def searchCityById(self, idCity):
        ciudad = {}
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM airbnb.ciudades WHERE idCiudad={idCity};"
                cursor.execute(sql)
                ciudad = cursor.fetchone()
        finally:
            pass
        return ciudad

    def updateCityBD(self, id,cityname,idcountry):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""UPDATE airbnb.ciudades SET 
                NombreCiudad = '{cityname}', IdPais = '{idcountry}'
                WHERE idCiudad = {id};"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def traerIDCity(self, cityname, idcountry):
        idciudad = 0
        try:
            with self.connection.cursor() as cursor:
                sql = f"""SELECT idCiudad
                FROM ciudades
                WHERE NombreCiudad = '{cityname}' AND IdPais = '{idcountry}';"""
                cursor.execute(sql)
                idciudad = cursor.fetchone()
        finally:
            pass
        if idciudad is None:
            idciudad=0
            return idciudad
        else:
            return idciudad["idCiudad"]

    def deleteCityDB(self, idCity):
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM airbnb.ciudades WHERE idCiudad={idCity};"
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass