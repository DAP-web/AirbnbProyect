import pymysql

class DBPaises:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="12345",
            db="airbnb",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def getCountries(self):
        result = {}
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM airbnb.paises;"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def insertCountry(self, countryname,code):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""INSERT INTO airbnb.paises
                (NombrePais,
                CodigoTelefonico)
                VALUES
                ('{countryname}',
                '{code}');"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def searchCountryById(self, idCountry):
        pais = {}
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM airbnb.paises WHERE idPais={idCountry};"
                cursor.execute(sql)
                pais = cursor.fetchone()
        finally:
            pass
        return pais

    def updateCountryBD(self, id,countryname,code):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""UPDATE airbnb.paises SET 
                NombrePais = '{countryname}', CodigoTelefonico = '{code}'
                WHERE idPais = {id};"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def traerIDCountry(self, countryname, code):
        idpais = 0
        try:
            with self.connection.cursor() as cursor:
                sql = f"""SELECT idPais
                FROM paises
                WHERE NombrePais = '{countryname}' AND Codigotelefonico = '{code}';"""
                cursor.execute(sql)
                idpais = cursor.fetchone()
        finally:
            pass
        return idpais["idPais"]

    def deleteCountryDB(self, idCountry):
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM airbnb.paises WHERE idPais={idCountry};"
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass
            