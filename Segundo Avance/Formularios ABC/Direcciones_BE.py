from prettytable import PrettyTable
from DB_Direcciones_BE import (
    connection,
    getDirections,
    insertDirection,
    searchDirectionById,
    updateDirectionBD,
    traerIDDireccion,
    deleteDirectionDB
)

def getAllDirections():
    result = getDirections()

    table = PrettyTable()
    table.field_names = ["IdDireccion","Estado","CodigoPostal","Calle","IdCiudad"]

    for direccion in result:
        table.add_row([direccion["IdDireccion"],direccion["Estado"],direccion["CodigoPostal"],direccion["Calle"],direccion["IdCiudad"]])

    print(table)
    table.clear()

def addDirection():
    print("\nAdding a new direction...")
    state = input("\nEstado: ")
    postalcode = input("\nCodigoPostal: ")
    street = input("\nCalle: ")
    idcity = input("\nIdCiudad: ")

    insertDirection(state,postalcode,street,idcity)
    iddireccion=traerIDDireccion(state,postalcode,street,idcity)

    print("\nSu direccion se ha registrado con éxito.\n")
    print(f"Su código de direccion única es {iddireccion}.\n")
    getAllDirections()

def updateDirection():
    print("\nUpdating an existing direction...")
    id = int(input("\nID de la direccion a actualizar: "))

    direction = searchDirectionById(id)

    update = int(input("Update State? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old State: {direction['Estado']}")
        state = input("New State: ")
    else:
        state = direction["Estado"]

    update = int(input("Update PostalCode? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old PostalCode: {direction['CodigoPostal']}")
        postalcode = input("New PostalCode: ")
    else:
        postalcode = direction["CodigoPostal"]

    update = int(input("Update Street? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Telephone {direction['NumeroTelefonico']}")
        street = input("New Telephone : ")
    else:
        street = direction["NumeroTelefonico"]

    update = int(input("Update IdCity number? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old IdCity number: {direction['IdCiudad']}")
        idcity = input("New IdCity number: ")
    else:
        idcity = direction["IdCiudad"]

   

    updateDirectionBD(id,state,postalcode,street,idcity)
    print("\nLos cambios se han efectuado con éxito.")
    getAllDirections()

def deleteDirection():
    print("Deleting direction...")
    id = int(input("ID of direction to delete: "))

    deleteDirectionDB(id)
    print("La direccion se ha removido con éxito.")
    getAllDirections()

def getDirection(direccion):
    id = direccion["idDirecciones"]
    direccion = searchDirectionById(id)

    print(f"ID de direccion única: {direccion['idDirecciones']}")
    print(f"Estado: {direccion['Estado']}")
    print(f"CodigoPostal: {direccion['CodigoPostal']}")
    print(f"Calle: {direccion['Calle']}")
    print(f"IdCiudad: {direccion['IdCiudad']}")

def actualizarDireccion(direccion):
    print("\nUpdating an existing direction...")

    direction = direccion

    update = int(input("Update State? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old State: {direction['Estado']}")
        state = input("New State: ")
    else:
        state = direction["Estado"]

    update = int(input("Update PostalCode? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old PostalCode: {direction['CodigoPostal']}")
        postalcode = input("New PostalCode: ")
    else:
        postalcode = direction["CodigoPostal"]

    update = int(input("Update Street? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Street  {direction['Calle']}")
        street = input("New Street: ")
    else:
        street = direction["Calle"]

    update = int(input("Update IdCity number? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old IdCity number: {direction['IdCiudad']}")
        idcity = input("New IdCity number: ")
    else:
        idcity = direction["IdCiudad"]


    updateDirectionBD(direction["idDirecciones"],state,postalcode,street,idcity)
    direction = searchDirectionById(direction["idDirecciones"])
    print("\nLos cambios se han efectuado con éxito.")
    getDirection(direction)
