from prettytable import PrettyTable
from DB_Clientes import (
    connection,
    getClients,
    insertClient,
    searchClientById,
    updateClientBD,
    deleteClientDB
)

def getAllClients():
    result = getClients()

    table = PrettyTable()
    table.field_names = ["IdCliente","Nombre","Apellido","Telefono","Pais","Correo","Usuario"]

    for cliente in result:
        table.add_row([cliente["idClientes"],cliente["Nombre"],cliente["Apellido"],cliente["NumeroTelefonico"],cliente["Pais"],cliente["Correo"],cliente["Usuario"]])

    print(table)
    table.clear()

def addClient():
    print("\nAdding a new client...")
    name = input("\nNombre: ")
    lastname = input("\nApellido: ")
    telephone = input("\nNumero de Telefono: ")
    country = input("\nPais de provinencia: ")
    email = input("\nCorreo electrónico: ")
    pswrd = input("\nContraseña: ")
    user = input("\nNombre de usuario: ")

    insertClient(name,lastname,telephone,country,email,pswrd,user)
    print("\nSu perfil se ha creado con éxito.\n")
    getAllClients()

def updateClient():
    print("\nUpdating an existing client...")
    id = int(input("\nID del cliente a actualizar: "))

    client = searchClientById(id)

    update = int(input("Update Name? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Name: {client['Nombre']}")
        name = input("New Name: ")
    else:
        name = client["Nombre"]

    update = int(input("Update Lastname? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Lastname: {client['Apellido']}")
        lastname = input("New Lastname: ")
    else:
        lastname = client["Apellido"]

    update = int(input("Update Telephone number? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Telephone number {client['NumeroTelefonico']}")
        number = input("New Telephone number: ")
    else:
        number = client["NumeroTelefonico"]

    update = int(input("Update Country? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Country: {client['Pais']}")
        client["Pais"] = input("New Country: ")
        country = client["Pais"]
    else:
        country = client["Pais"]

    update = int(input("Update Email? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Email: {client['Correo']}")
        email = input("New Email: ")
    else:
        email = client["Correo"]

    update = int(input("Update Password? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old password {client['Contrasenha']}")
        pswd = input("New password: ")
    else:
        pswd = client["Contrasenha"]

    update = int(input("Update User? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old User {client['Usuario']}")
        user = input("New User: ")
    else:
        user = client["Usuario"]

    updateClientBD(id,name,lastname,number,country,email,pswd,user)
    print("\nLos cambios se han efectuado con éxito.")
    getAllClients()

def deleteClient():
    print("Deleting client...")
    id = int(input("ID of client to delete: "))

    deleteClientDB(id)
    print("El usuario se ha removido con éxito.")
    getAllClients()
