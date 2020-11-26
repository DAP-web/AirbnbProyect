from prettytable import PrettyTable
from DB_Clientes_BE import DBClientes
from DB_Residencia_BE import ResidenciaDB
from Reservaciones_BE import reservaciones

class clientesBE:
    def __init__(self):
        self.dbcliente=DBClientes()
        self.dbreservaciones = reservaciones()
        self.dbresidencias = ResidenciaDB()

    def getAllClients(self):
        result = self.dbcliente.getClients()

        table = PrettyTable()
        table.field_names = ["IdCliente","Nombre","Apellido","Telefono","Pais","Correo","Usuario"]

        for cliente in result:
            table.add_row([
                cliente["idClientes"],
                cliente["Nombre"],
                cliente["Apellido"],
                cliente["NumeroTelefonico"],
                cliente["Pais"],
                cliente["Correo"],
                cliente["Usuario"]
                ])

        print(table)
        table.clear()

    def addClient(self):
        print("\nAdding a new client...")
        name = input("\nNombre: ")
        lastname = input("\nApellido: ")
        telephone = input("\nNumero de Telefono: ")
        country = input("\nPais de provinencia: ")
        email = input("\nCorreo electrónico: ")
        pswrd = input("\nContraseña: ")
        user = input("\nNombre de usuario: ")

        self.dbcliente.insertClient(name,lastname,telephone,country,email,pswrd,user)
        idcliente=self.dbcliente.traerIDCliente(name,lastname,telephone,country,email,pswrd,user)

        print("\nSu perfil se ha creado con éxito.\n")
        print(f"Su código de cliente único es {idcliente}.\n")
        self.getAllClients()

    def updateClient(self):
        print("\nUpdating an existing client...")
        id = int(input("\nID del cliente a actualizar: "))

        client = self.dbcliente.searchClientById(id)

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

        self.dbcliente.updateClientBD(id,name,lastname,number,country,email,pswd,user)
        print("\nLos cambios se han efectuado con éxito.")
        self.getAllClients()

    def deleteClient(self):
        print("Deleting client...")
        id = int(input("ID of client to delete: "))

        self.dbcliente.deleteClientDB(id)
        print("El usuario se ha removido con éxito.")
        self.getAllClients()

    #ESTOS METODOS SON ESPECIFICAMENTE PARA UN USUARIO YA LOGGEADO
    #Esta parte es de procesos no de tablas
    def getClient(self,cliente):
        id = cliente["idClientes"]
        cliente = self.dbcliente.searchClientById(id)

        print(f"ID de cliente único: {cliente['idClientes']}")
        print(f"Nombre: {cliente['Nombre']}")
        print(f"Apellido: {cliente['Apellido']}")
        print(f"Número telefónico: {cliente['NumeroTelefonico']}")
        print(f"País: {cliente['Pais']}")
        print(f"Correo: {cliente['Correo']}")
        print(f"Usuario: {cliente['Usuario']}")
        print(f"Contraseña: {cliente['Contrasenha']}")

    def actualizarCliente(self,cliente):
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

        self.dbcliente.updateClientBD(client["idClientes"],name,lastname,number,country,email,pswd,user)
        client = self.dbcliente.searchClientById(client["idClientes"])
        print("\nLos cambios se han efectuado con éxito.")
        self.getClient(client)

    def clienteAgendaReserva(self,cliente):
        pais=input("¿A qué país viajas? ")
        
        residencias = self.dbresidencias.busquedaDeResidencias(pais)

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
            morada = self.dbresidencias.verResidenciaEspecifica(residenciaVer)

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
                for res in morada:
                    self.dbreservaciones.agendarReservaClientePerfil(cliente,res["idResidencia"])

        else:
            eleccion = int(input("¿Reservar alguna residencia? No(0)|Sí(1): "))
            if eleccion==1:
                res = int(input("¿Cuál residencia desea reservar? Ingrese el ID de la residencia"))
                self.dbreservaciones.agendarReservaClientePerfil(cliente,res)
        """decision = bool(input("¿Quieres escoger otro país? No(0)|Sí(1)"))
        if decision==False:
            eleccion = input("¿Cuál residencia quieres reservar? ¡Ingresa el ID de la residencia! ")"""
            



