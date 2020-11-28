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
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM airbnb.rservicio;"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def insertResiServ(self,residenceID, serviceID):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""INSERT INTO airbnb.residenciaservicio
                (IdServicio,
                IdResidencia)
                VALUES
                ({serviceID},
                {residenceID});"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def searchResiServById(self, idResiServ):
        resiserv = {}
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM airbnb.residenciaservicio WHERE idRS={idResiServ};"
                cursor.execute(sql)
                resiserv = cursor.fetchone()
        finally:
            pass
        return resiserv

    def updateResiServBD(self, id, serviceID, residenceID):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""UPDATE airbnb.residenciaservicio SET 
                IdServicio = {serviceID}, IdResidencia = {residenceID}
                WHERE idRS = {id};"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def traerIDResiServ(self, serviceID, residenceID):
        idresservicio = 0
        try:
            with self.connection.cursor() as cursor:
                sql = f"""SELECT idRS
                FROM residenciaservicio
                WHERE IdServicio = {serviceID} AND IdResidencia = {residenceID};"""
                cursor.execute(sql)
                idresservicio = cursor.fetchone()
        finally:
            pass
        return idresservicio["idRS"]

    def deleteResiServDB(self, idRS):
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM airbnb.residenciaservicio WHERE idRS={idRS};"
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass