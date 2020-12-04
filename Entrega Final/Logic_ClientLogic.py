from Core_dx_logic import Logic
from Objects_ClientObj import ClientObj

class ClientLogic(Logic):
    def __init__(self):
        super().__init__("clientes")
        self.idName="idClientes"
    
    def getClientes(self):
        clientList = super().getAllRows(self.tableName)
        clientObjList = []
        for client in clientList:
            newClient = self.createClientObj(client)
            clientObjList.append(newClient)
        return clientObjList

    def createClientObj(self,id, name,lastname, telephone, country, email, pswd, user):
        clientobj = ClientObj(name,lastname,telephone,country,email,pswd,user,id)
        return clientobj

    def createClientObj(self, clientDict):
        userObj = ClientObj(
            clientDict["Nombre"],
            clientDict["Apellido"],
            clientDict["NumeroTelefonico"],
            clientDict["Pais"],
            clientDict["Correo"],
            clientDict["Contrasenha"],
            clientDict["Usuario"],
            clientDict["idClientes"]
        )
        return userObj

    def insertClient(self,name, lastname,telephone,country,email,pswrd,user):
        database = self.database
        sql = f"""INSERT INTO airbnb.clientes
                (Nombre, Apellido, NumeroTelefonico,
                Pais, Correo, Contrasenha, Usuario)
                VALUES
                ('{name}', '{lastname}', '{telephone}',
                '{country}', '{email}', '{pswrd}', '{user}');"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def searchClientById(self, id):
        rowDict = super().getRowById(self.idName,id,self.tableName)
        newUser = self.createClientObj(rowDict)
        return newUser
    
    def updateClientBD(self,id,name, lastname,telephone,country,email,pswrd,user):
        database = self.database
        sql = f"""UPDATE airbnb.clientes SET 
        Nombre = '{name}', Apellido = '{lastname}', 
        NumeroTelefonico = '{telephone}', 
        Pais = '{country}', Correo = '{email}', 
        Contrasenha = '{pswrd}', Usuario = '{user}' 
        WHERE idClientes = {id};"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def traerIDCliente(self,name, lastname,telephone,country,email,pswrd,user):
        database = self.database
        sql = f"""SELECT idClientes
        FROM clientes
        WHERE Nombre = '{name}' AND Apellido = '{lastname}' AND NumeroTelefonico = '{telephone}' 
        AND Pais = '{country}' AND Correo = '{email}' AND Contrasenha = '{pswrd}' 
        AND Usuario = '{user}';"""
        id = database.executeQueryOneRow(sql)
        return id["idClientes"]
    
    def deleteClientDB(self, id):
        super().deleteRowById(self.idName, id, self.tableName)

    def verificarUsuario(self,email,pswd):
        cliente={}
        database = self.database
        sql = f"""SELECT * FROM airbnb.clientes 
        WHERE Correo='{email}' and Contrasenha='{pswd}';"""
        cliente = database.executeQueryOneRow(sql)
        return cliente
