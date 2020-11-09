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

def insertService(name, lastname,telephone,country,email,pswrd,user):
    try:
        with connection.cursor() as cursor:
            sql = f"""INSERT INTO airbnb.servicios
            (Nombre,
            Apellido,
            NumeroTelefonico,
            Pais,
            Correo,
            Contrasenha,
            Usuario)
            VALUES
            ('{name}',
            '{lastname}',
            '{telephone}',
            '{country}',
            '{email}',
            '{pswrd}',
            '{user}');"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def searchServiceById(idServicio):
    servicio = {}
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM airbnb.servicios WHERE idServicios={idServicio};"
            cursor.execute(sql)
            servicio = cursor.fetchone()
    finally:
        pass
    return servicio

def updateServiceBD(id,name, lastname,telephone,country,email,pswrd,user):
    try:
        with connection.cursor() as cursor:
            sql = f"""UPDATE airbnb.service SET 
            Nombre = '{name}', Apellido = '{lastname}', NumeroTelefonico = '{telephone}', Pais = '{country}', Correo = '{email}', Contrasenha = '{pswrd}', Usuario = '{user}' 
            WHERE idServicios = {id};"""
            cursor.execute(sql)
            connection.commit()
    finally:
        pass

def traerIDServicio(name, lastname,telephone,country,email,pswrd,user):
    idservicio = 0
    try:
        with connection.cursor() as cursor:
            sql = f"""SELECT idServicios
            FROM servicios
            WHERE Nombre = '{name}' AND Apellido = '{lastname}' AND NumeroTelefonico = '{telephone}' 
            AND Pais = '{country}' AND Correo = '{email}' AND Contrasenha = '{pswrd}' 
            AND Usuario = '{user}';"""
            cursor.execute(sql)
            idservicio = cursor.fetchone()
    finally:
        pass
    return idservicio["idServicios"]

def deleteServiceDB(idService):
    try:
        with connection.cursor() as cursor:
            sql = f"DELETE FROM airbnb.clientes WHERE idClientes={idService};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass