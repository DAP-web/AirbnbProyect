import pymysql


class ExperienciasResidencialesBD:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="12345",
            db="airbnb",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def getExperienciaResidencias(self):
        result = {}
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM airbnb.experienciaresidencia;"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def insertExperienciaResidencias(self, IdExp, IdResidencia):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""INSERT INTO airbnb.experienciaresidencia
                (IdExp,
                IdResidencia)
                VALUES
                ('{IdExp}',
                {IdResidencia});"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def searchExperienciaResidenciasById(self, idER):
        experienciaResidencia = {}
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM airbnb.experienciaresidencia WHERE idER={idER};"
                cursor.execute(sql)
                experienciaResidencia = cursor.fetchone()
        finally:
            pass
        return experienciaResidencia

    def updateExperienciaResidenciaBD(self, id, idExp, idResidencia):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""UPDATE airbnb.experienciaresidencia SET 
                IdExp = {idExp}, IdResidencia = {idResidencia} 
                WHERE idER = {id};"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def traerIDExperienciaResidencia(self, IdExp, idResidencia):
        idExperienciaresidencia = 0
        try:
            with self.connection.cursor() as cursor:
                sql = f"""SELECT idER
                FROM experienciaresidencia
                WHERE IdExp = '{IdExp}' AND IdResidencia = {idResidencia};"""
                cursor.execute(sql)
                idexperienciaresidencia = cursor.fetchone()
        finally:
            pass
        return idExperienciaresidencia["idExperienciaresidencia"]

    def deleteExperienciaResidenciaDB(self, idER):
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM airbnb.experienciaresidencia WHERE IdER={idER};"
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass
