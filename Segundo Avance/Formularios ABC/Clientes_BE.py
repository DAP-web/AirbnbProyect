from prettytable import PrettyTable
from DB_Clientes_BE import (
    connection,
    getClients,
    insertClient,
    searchClientById,
    updateClientBD,
    traerIDCliente,
    deleteClientDB
)
from DB_Residencia_BE import(
    busquedaDeResidencias,
    verResidenciaEspecifica
)
from Reservaciones_BE import(
    agendarReservaClientePerfil
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
    idcliente=traerIDCliente(name,lastname,telephone,country,email,pswrd,user)

    print("\nSu perfil se ha creado con éxito.\n")
    print(f"Su código de cliente único es {idcliente}.\n")
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
        country = input("New Country: ")
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

#ESTOS METODOS SON ESPECIFICAMENTE PARA UN USUARIO YA LOGGEADO
#Esta parte es de procesos no de tablas
def getClient(cliente):
    id = cliente["idClientes"]
    cliente = searchClientById(id)

    print(f"ID de cliente único: {cliente['idClientes']}")
    print(f"Nombre: {cliente['Nombre']}")
    print(f"Apellido: {cliente['Apellido']}")
    print(f"Número telefónico: {cliente['NumeroTelefonico']}")
    print(f"País: {cliente['Pais']}")
    print(f"Correo: {cliente['Correo']}")
    print(f"Usuario: {cliente['Usuario']}")
    print(f"Contraseña: {cliente['Contrasenha']}")

def actualizarCliente(cliente):
    print("\nUpdating an existing client...")

    client = cliente

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
        country = input("New Country: ")
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

    updateClientBD(client["idClientes"],name,lastname,number,country,email,pswd,user)
    client = searchClientById(client["idClientes"])
    print("\nLos cambios se han efectuado con éxito.")
    getClient(client)

def clienteAgendaReserva(cliente):
    pais=input("¿A qué país viajas? ")
    
    residencias = busquedaDeResidencias(pais)

    table = PrettyTable()
    table.field_names = ["idResidencia","TipoAlojamiento","AirbnbPlus","Precio"]

    for residencia in residencias:
        table.add_row([
        residencia["idResidencia"],
        residencia["TipoAlojamiento"],
        residencia["AirbnbPlus"],
        residencia["Precio"]
        ])

    print(table)
    table.clear()

    ver = int(input("¿Ver alguna residencia en específico? No(0)|Sí(1): "))
    if ver==1:
        residenciaVer = input("¿Cuál residencia quieres ver? (Introduce el ID de la residencia): ")
        morada = verResidenciaEspecifica(residenciaVer)

        tablaResidencia = PrettyTable()
        tablaDireccioin = PrettyTable()

        tablaResidencia.field_names = [
            "idResidencia",
            "TipoAlojamiento",
            "Habitaciones",
            "Banhos",
            "Camas",
            "Precio",
            "FlexibilidadDeCancelacion",
            "AirbnbPlus",
            "Mascotas",
            "Fumadores"
        ]

        tablaDireccioin.field_names=[ 
            "Estado",
            "CodigoPostal", 
            "Calle", 
            "NombreCiudad", 
            "NombrePais"
        ]

        for residencia in morada:
            tablaResidencia.add_row([
                residencia["idResidencia"],
                residencia["TipoAlojamiento"],
                residencia["Habitaciones"],
                residencia["Banhos"],
                residencia["Camas"],
                residencia["Precio"],
                residencia["FlexibilidadDeCancelacion"],
                residencia["AirbnbPlus"],
                residencia["Mascotas"],
                residencia["Fumadores"],
            ])
            tablaDireccioin.add_row([
                residencia["Estado"],
                residencia["CodigoPostal"], 
                residencia["Calle"], 
                residencia["NombreCiudad"], 
                residencia["NombrePais"]
            ])
        print(tablaResidencia)
        tablaResidencia.clear()
        print(tablaDireccioin)
        tablaDireccioin.clear()
    
        eleccion = int(input("Reservar ya No(0)|Sí(1): "))
        if eleccion==1:
            agendarReservaClientePerfil(cliente,morada["idResidencia"])
            
    """decision = bool(input("¿Quieres escoger otro país? No(0)|Sí(1)"))
    if decision==False:
        eleccion = input("¿Cuál residencia quieres reservar? ¡Ingresa el ID de la residencia! ")"""
        



