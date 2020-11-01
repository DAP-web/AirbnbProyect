import pymysql

"""
1. identificar cada parte de lo que esta en el codigo
2. empezar a separar el frontend del backend
"""

"""
connection = pymysql.connect(

esta creando la conexion entre mi programa python con la base de datos
mysql vean que se tiene los datos de conexion host, user, passwrd, el
eschema o la base de datos
x database
"""
connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="cardexdb",
    cursorclass=pymysql.cursors.DictCursor,
)


def getClientsDB():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM cardexdb.client;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    return result


def insertClientDB(name, age, email):
    try:
        with connection.cursor() as cursor:
            sql = f"insert into cardexdb.client(name, age, email) values('{name}', {age}, '{email}');"
            cursor.execute(sql)
            # cuando hago inserts, update o deletes, create
            connection.commit()
    finally:
        pass


def searchClientById(idClient):
    client = {}
    try:
        with connection.cursor() as cursor:
            sql = f"select * from cardexdb.client where id={idClient};"
            cursor.execute(sql)
            client = cursor.fetchone()
    finally:
        pass
    return client


def updateClientDB(name, age, email):
    try:
        with connection.cursor() as cursor:
            sql = f"UPDATE cardexdb.client SET name = '{name}', age = {age}, email = '{email}' WHERE id = {id};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass


def deleteClientDB(idClient):
    try:
        with connection.cursor() as cursor:
            sql = f"delete from cardexdb.client where id={idClient};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
