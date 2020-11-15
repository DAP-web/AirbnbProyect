import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="airbnb",
    cursorclass=pymysql.cursors.DictCursor,
)

def getTematica():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM airbnb.tematica;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result

def insertTematica(tematicaname,description):
    try:
        with connection.cursor() as cursor:
            sql = f"""INSERT INTO airbnb.tematica
            (NombreTematica,
            Descripcion)
            VALUES
            ('{tematicaname}',
            '{description}');"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def searchTematicaById(idTematica):
    tematica = {}
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM airbnb.tematica WHERE idTematica={idTematica};"
            cursor.execute(sql)
            tematica = cursor.fetchone()
    finally:
        pass
    return tematica

def updateTematicaBD(id,tematicaname,description):
    try:
        with connection.cursor() as cursor:
            sql = f"""UPDATE airbnb.tematica SET 
            NombreTematica = '{tematicaname}', Descripcion = '{description}'
            WHERE idTematica = {id};"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def traerIDTematica(tematicaname, description):
    idtematica = 0
    try:
        with connection.cursor() as cursor:
            sql = f"""SELECT idTematica
            FROM tematica
            WHERE NombreTematica = '{tematicaname}' AND Descripcion = '{description}';"""
            cursor.execute(sql)
            idtematica = cursor.fetchone()
    finally:
        pass
    return idtematica["idTematica"]

def deleteTematicaDB(idTematica):
    try:
        with connection.cursor() as cursor:
            sql = f"DELETE FROM airbnb.tematica WHERE idTematica={idTematica};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
        