import pymysql

class calificacionesDB:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="12345",
            db="airbnb",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def obtenerCalificaciones(self):
        result = {}
        try:
            with self.connection.cursor() as cursor:
                sql = """SELECT IdResidencia,round(avg(Calificacion),2) as Promedio
                FROM calificaciones
                GROUP BY IdResidencia;
                """
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def agregarCalificacion(self,calificacion,residencia):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""INSERT INTO airbnb.calificaciones
                (Calificacion,
                IdResidencia)
                VALUES
                ({calificacion},
                {residencia});"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass
