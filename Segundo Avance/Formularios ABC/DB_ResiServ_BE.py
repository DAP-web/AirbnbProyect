import pymysql

class ResiServDB:
    def __init__(self):
        self.connection = pymysql.connect(
        host="localhost",
        user="root",
        passwd="12345",
        db="airbnb",
        cursorclass=pymysql.cursors.DictCursor,
        )

    def getResiServ(self):
        result = {}
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM airbnb.residenciaservicio;"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def insertResiServ(self, serviceID, residenceID):
        try:
            with connection.cursor() as cursor:
                sql = f"""INSERT INTO airbnb.residenciaservicio
                (IdServicio,
                IdResidencia)
                VALUES
                ('{serviceID}'
                '{residenceID});"""
                cursor.execute(sql)
                connection.commit()
        finally:
            pass

    def searchResiServById(self, idResiServ):
        resiserv = {}
        try:
            with connection.cursor() as cursor:
                sql = f"SELECT * FROM airbnb.residenciaservicio WHERE idRS={idResiServ};"
                cursor.execute(sql)
                resiserv = cursor.fetchone()
        finally:
            pass
        return resiserv

    def updateResiServBD(self, id, serviceID, residenceID):
        try:
            with connection.cursor() as cursor:
                sql = f"""UPDATE airbnb.residenciaservicio SET 
                IDServicio = '{serviceID}', IDResidencia = '{residenceID}'
                WHERE idRS = {id};"""
                cursor.execute(sql)
                connection.commit()
        finally:
            pass

    def traerIDResiServ(self, serviceID, residenceID):
        idRS = 0
        try:
            with connection.cursor() as cursor:
                sql = f"""SELECT idRS
                FROM residenciaservicio
                WHERE idServicio = '{serviceID}' AND idResidencia = '{residenceID}';"""
                cursor.execute(sql)
                idservicio = cursor.fetchone()
        finally:
            pass
        return idRS["idRS"]

    def deleteResiServDB(self, idRS):
        try:
            with connection.cursor() as cursor:
                sql = f"DELETE FROM airbnb.residenciaservicio WHERE idRS={idRS};"
                cursor.execute(sql)
                connection.commit()
        finally:
            pass