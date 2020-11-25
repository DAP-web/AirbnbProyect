import pymysql

class DBClientes:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="12345",
            db="airbnb",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def getClients(self):
        result = {}
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM airbnb.clientes;"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            pass
        return result

    def insertClient(self,name, lastname,telephone,country,email,pswrd,user):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""INSERT INTO airbnb.clientes
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
                self.connection.commit()
        finally:
            pass

    def searchClientById(self,idCliente):
        cliente = {}
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM airbnb.clientes WHERE idClientes={idCliente};"
                cursor.execute(sql)
                cliente = cursor.fetchone()
        finally:
            pass
        return cliente

    def updateClientBD(self,id,name, lastname,telephone,country,email,pswrd,user):
        try:
            with self.connection.cursor() as cursor:
                sql = f"""UPDATE airbnb.clientes SET 
                Nombre = '{name}', Apellido = '{lastname}', NumeroTelefonico = '{telephone}', Pais = '{country}', Correo = '{email}', Contrasenha = '{pswrd}', Usuario = '{user}' 
                WHERE idClientes = {id};"""
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    def traerIDCliente(self,name, lastname,telephone,country,email,pswrd,user):
        idcliente = 0
        try:
            with self.connection.cursor() as cursor:
                sql = f"""SELECT idClientes
                FROM clientes
                WHERE Nombre = '{name}' AND Apellido = '{lastname}' AND NumeroTelefonico = '{telephone}' 
                AND Pais = '{country}' AND Correo = '{email}' AND Contrasenha = '{pswrd}' 
                AND Usuario = '{user}';"""
                cursor.execute(sql)
                idcliente = cursor.fetchone()
        finally:
            pass
        return idcliente["idClientes"]

    def deleteClientDB(self,idClient):
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM airbnb.clientes WHERE idClientes={idClient};"
                cursor.execute(sql)
                self.connection.commit()
        finally:
            pass

    #Esta funcion es para permitir iniciar sesion al usuario
    #Es parte de un proceso no de una tabla
    def verificarUsuario(self,email, contrasenha):
        cliente = {}
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM airbnb.clientes WHERE Correo='{email}' and Contrasenha='{contrasenha}';"
                cursor.execute(sql)
                cliente = cursor.fetchone()
        finally:
            pass
        return cliente
