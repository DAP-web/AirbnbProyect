from prettytable import PrettyTable
from DB_Servicios_BE import (
    connection,
    getServices,
    insertService,
    searchServiceById,
    updateServiceBD,
    traerIDServicio,
    deleteServiceDB
)

def getAllServices():
    result = getServices()

    table = PrettyTable()
    table.field_names = ["NombreServicio"]

    for servicio in result:
        table.add_row([servicio["idServicios"],servicio["NombreServicio"]])

    print(table)
    table.clear()

def addService():
    print("\nAdding a new service...")
    name = input("\nNombreServicio: ")


    insertService(name)
    idservicio=traerIDServicio(name)

    print("\nSu servicio se ha registrado con éxito.\n")
    print(f"Su código de servico único es {idservicio}.\n")
    getAllServices()

def updateService():
    print("\nUpdating an existing service...")
    id = int(input("\nID del servicio a actualizar: "))

    service = searchServiceById(id)

    update = int(input("Update Name? 0-No - 1-Yes "))
    if update == 1:
        print(f"Viejo Nombre del Servicio: {service['NombreServicio']}")
        name = input("Nuevo Nombre del Servicio: ")
    else:
        name = service["NombreServicio"]

    
    updateServiceBD(id,name)
    print("\nLos cambios se han efectuado con éxito.")
    getAllServices()

def deleteService():
    print("Deleting service...")
    id = int(input("ID of service to delete: "))

    deleteServiceDB(id)
    print("El servicio se ha removido con éxito.")
    getAllServices()