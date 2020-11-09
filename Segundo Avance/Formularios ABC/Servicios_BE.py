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
    table.field_names = ["IdServicio","Nombre","Apellido","Telefono","Pais","Correo","Usuario"]

    for servicio in result:
        table.add_row([servicio["idServicios"],servicio["Nombre"],servicio["Apellido"],servicio["NumeroTelefonico"],servicio["Pais"],servicio["Correo"],servicio["Usuario"]])

    print(table)
    table.clear()

def addService():
    print("\nAdding a new service...")
    name = input("\nNombre: ")
    lastname = input("\nApellido: ")
    telephone = input("\nNumero de Telefono: ")
    country = input("\nPais de provinencia: ")
    email = input("\nCorreo electrónico: ")
    pswrd = input("\nContraseña: ")
    user = input("\nNombre del servicio: ")

    insertService(name,lastname,telephone,country,email,pswrd,user)
    idservicio=traerIDServicio(name,lastname,telephone,country,email,pswrd,user)

    print("\nSu perfil se ha creado con éxito.\n")
    print(f"Su código de cliente único es {idservicio}.\n")
    getAllServices()

def updateService():
    print("\nUpdating an existing client...")
    id = int(input("\nID del cliente a actualizar: "))

    service = searchServiceById(id)

    update = int(input("Update Name? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Name: {service['Nombre']}")
        name = input("New Name: ")
    else:
        name = service["Nombre"]

    update = int(input("Update Lastname? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Lastname: {service['Apellido']}")
        lastname = input("New Lastname: ")
    else:
        lastname = service["Apellido"]

    update = int(input("Update Telephone number? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Telephone number {service['NumeroTelefonico']}")
        number = input("New Telephone number: ")
    else:
        number = service["NumeroTelefonico"]

    update = int(input("Update Country? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Country: {service['Pais']}")
        country = input("New Country: ")
    else:
        country = service["Pais"]

    update = int(input("Update Email? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Email: {service['Correo']}")
        email = input("New Email: ")
    else:
        email = service["Correo"]

    update = int(input("Update Password? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old password {service['Contrasenha']}")
        pswd = input("New password: ")
    else:
        pswd = service["Contrasenha"]

    update = int(input("Update Service? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Service {service['Servicio']}")
        user = input("New Service: ")
    else:
        user = service["Usuario"]

    updateServiceBD(id,name,lastname,number,country,email,pswd,user)
    print("\nLos cambios se han efectuado con éxito.")
    getAllServices()

def deleteService():
    print("Deleting service...")
    id = int(input("ID of service to delete: "))

    deleteServiceDB(id)
    print("El servicio se ha removido con éxito.")
    getAllServices()