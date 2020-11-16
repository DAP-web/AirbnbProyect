import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="airbnb",
    cursorclass=pymysql.cursors.DictCursor,
)

def getServices():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM airbnb.servicios;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result

def insertService(name):
    try:
        with connection.cursor() as cursor:
            sql = f"""INSERT INTO airbnb.servicios
            (NombreServicio)
            VALUES
            ('{name}');"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def searchServiceById(idServicio):
    servicio = {}
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM airbnb.servicios WHERE idServicio={idServicio};"
            cursor.execute(sql)
            servicio = cursor.fetchone()
    finally:
        pass
    return servicio

def updateServiceBD(id,name):
    try:
        with connection.cursor() as cursor:
            sql = f"""UPDATE airbnb.servicios SET 
            Nombre = '{name}' 
            WHERE idServicio = {id};"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def traerIDServicio(name):
    idservicio = 0
    try:
        with connection.cursor() as cursor:
            sql = f"""SELECT idServicio
            FROM servicios
            WHERE NombreServicio = '{name}';"""
            cursor.execute(sql)
            idservicio = cursor.fetchone()
    finally:
        pass
    return idservicio["idServicio"]

def deleteServiceDB(idService):
    try:
        with connection.cursor() as cursor:
            sql = f"DELETE FROM airbnb.servicios WHERE idServicio={idService};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass