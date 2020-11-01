from prettytable import PrettyTable
from database import (
    connection,
    getClientsDB,
    insertClientDB,
    searchClientById,
    updateClientDB,
    deleteClientDB,
)

"""
def getAllClients():
este es un metodo de este archivo que se encarga de traer todos
los clientes de nuestra tabla cliente, colocarlos en una prettytable
y luego desplegarlos
"""


def getAllClients():
    # con la conexion y sql va a traer todos los datos y los guarda en
    # una variable llamada result
    # x database
    result = getClientsDB()

    # crea un objeto pretty table y le genera los encabezados de la tabla
    table = PrettyTable()
    table.field_names = ["Id", "Name", "Age", "Email"]
    # for medio del for saco todos los cliente y los voy ingresando
    # a la pretty table
    for client in result:
        table.add_row([client["id"], client["name"], client["age"], client["email"]])
    # imprimo la prettytable
    print(table)
    # luego limpiamos la tabla
    table.clear()


"""
def addNewClient():
este metodo se encarga de colocar un nuevo cliente a la base de datos por esa razon
comienza pidiendo al usuario la informacion del cliente.
luego genera el insert en transql y lo corre en la base de datos
al final manda a llamar al metodo getAllClients para mostrar la adicion
"""


def addNewClient():
    # obtener informacion del cliente del usuario
    print("add a new client...")
    name = input("name: ")
    age = int(input("age: "))
    email = input("email: ")
    # se ocupa la conexion para insertar el registro en la base de datos
    # con el insert
    # x database
    insertClientDB(name, age, email)
    getAllClients()


"""
def updateClient():
este metodo hara la actualizacion de un dato en la base de datos
primero debemos saber el id del cliente que vamos a actualizar
segundo debemos saber que columna vamos a modificar
luego debo dar la informacion nueva
al manda a llamar el metodo getAllClients para ver la tabla
"""


def updateClient():
    print("update client...")
    id = int(input("id of client to update: "))
    # x database
    client = searchClientById(id)

    update = int(input("update name 0-no 1-yes? "))
    if update == 1:
        print(f"old name: {client['name']}")
        name = input("name: ")
    else:
        name = client["name"]

    update = int(input("update age 0-no 1-yes? "))
    if update == 1:
        print(f"old age: {client['age']}")
        age = int(input("age: "))
    else:
        age = client["age"]

    update = int(input("update email 0-no 1-yes? "))
    if update == 1:
        print(f"old email: {client['email']}")
        email = input("email: ")
    else:
        email = client["email"]

    # x database
    updateClientDB(name, age, email)
    getAllClients()


"""
def deleteClient():
este metodo se encarga de borrar un cliente de la base de datos
necesitamos del usuario el id de cliente a borrar
"""


def deleteClient():
    print("delete client...")
    id = int(input("id of client to delete: "))
    # x database
    deleteClientDB()
    getAllClients()
