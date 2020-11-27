import pymysql

class serviciosDB:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="12345",
            db="airbnb",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def getServices(self):
        result = {}
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM airbnb.servicios;"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def insertService(self,name):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""INSERT INTO airbnb.servicios
                (NombreServicio)
                VALUES
                ('{name}');"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def searchServiceById(self,idServicio):
        servicio = {}
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM airbnb.servicios WHERE idServicio={idServicio};"
                cursor.execute(sql)
                servicio = cursor.fetchone()
        finally:
            pass
        return servicio

    def updateServiceBD(self,id,name):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""UPDATE airbnb.servicios SET 
                NombreServicio = '{name}' 
                WHERE idServicio = {id};"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def traerIDServicio(self,name):
        idservicio = 0
        try:
            with self.connection.cursor() as cursor:
                sql = f"""SELECT idServicio
                FROM servicios
                WHERE NombreServicio = '{name}';"""
                cursor.execute(sql)
                idservicio = cursor.fetchone()
        finally:
            pass
        return idservicio["idServicio"]

    def deleteServiceDB(self,idService):
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM airbnb.servicios WHERE idServicio={idService};"
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass