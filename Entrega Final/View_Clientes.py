from prettytable import PrettyTable
from Logic_ClientLogic import ClientLogic
from Logic_ResidenciasLogic import ResidenciaLogic
from View_Reservas import reservaciones
from Logic_ReservasLogics import ReservasLogic
from Logic_FacturasLogic import FacturasLogic
from View_Facturas import facturasBE

class clientesBE:
    def __init__(self):
        self.dbcliente=ClientLogic()
        self.dbreservaciones = reservaciones()
        self.dbresidencias = ResidenciaLogic()
        self.reservaslogic = ReservasLogic()
        self.dbfacturas = FacturasLogic()
        self.facturasbe = facturasBE()

    def getAllClients(self):
        result = self.dbcliente.getClientes()

        table = PrettyTable()
        table.field_names = ["IdCliente","Nombre","Apellido","Telefono","Pais","Correo","Usuario"]

        for cliente in result:
            table.add_row([
                cliente.id,
                cliente.name,
                cliente.lastname,
                cliente.telephone,
                cliente.country,
                cliente.email,
                cliente.user
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
            print(f"Old Name: {client.name}")
            name = input("New Name: ")
        else:
            name = client.name

        update = int(input("Update Lastname? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Lastname: {client.lastname}")
            lastname = input("New Lastname: ")
        else:
            lastname = client.lastname

        update = int(input("Update Telephone number? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Telephone number {client.telephone}")
            number = input("New Telephone number: ")
        else:
            number = client.telephone

        update = int(input("Update Country? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Country: {client.country}")
            country = input("New Country: ")
        else:
            country = client.country

        update = int(input("Update Email? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Email: {client.email}")
            email = input("New Email: ")
        else:
            email = client.email

        update = int(input("Update Password? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old password {client.pswd}")
            pswd = input("New password: ")
        else:
            pswd = client.pswd

        update = int(input("Update User? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old User {client.user}")
            user = input("New User: ")
        else:
            user = client.user

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
        id = cliente.id
        cliente = self.dbcliente.searchClientById(id)

        print(f"ID de cliente único: {cliente.id}")
        print(f"Nombre: {cliente.name}")
        print(f"Apellido: {cliente.lastname}")
        print(f"Número telefónico: {cliente.telephone}")
        print(f"País: {cliente.country}")
        print(f"Correo: {cliente.email}")
        print(f"Usuario: {cliente.user}")
        print(f"Contraseña: {cliente.pswd}")

    def actualizarCliente(self,cliente):
        print("\nUpdating an existing client...")

        client = cliente

        update = int(input("Update Name? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Name: {client.name}")
            name = input("New Name: ")
        else:
            name = client.name

        update = int(input("Update Lastname? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Lastname: {client.lastname}")
            lastname = input("New Lastname: ")
        else:
            lastname = client.lastname

        update = int(input("Update Telephone number? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Telephone number {client.telephone}")
            number = input("New Telephone number: ")
        else:
            number = client.telephone

        update = int(input("Update Country? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Country: {client.country}")
            country = input("New Country: ")
        else:
            country = client.country

        update = int(input("Update Email? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Email: {client.email}")
            email = input("New Email: ")
        else:
            email = client.email

        update = int(input("Update Password? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old password {client.pswd}")
            pswd = input("New password: ")
        else:
            pswd = client.pswd

        update = int(input("Update User? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old User {client.user}")
            user = input("New User: ")
        else:
            user = client.user

        self.dbcliente.updateClientBD(client.id,name,lastname,number,country,email,pswd,user)
        client = self.dbcliente.searchClientById(client.id)
        print("\nLos cambios se han efectuado con éxito.")
        self.getClient(client)

    def clienteAgendaReserva(self,cliente):
        pais=input("¿A qué país viajas? ")
        
        residencias = self.dbresidencias.busquedaDeResidencias(pais)

        table = PrettyTable()
        table.field_names = ["idResidencia","TipoAlojamiento","AirbnbPlus","Precio"]

        for residencia in residencias:
            table.add_row([
            residencia.id,
            residencia.tipoAlojamiento,
            residencia.aPlus,
            residencia.precio
            ])

        print(table)
        table.clear()

        ver = int(input("¿Ver alguna residencia en específico? No(0)|Sí(1): "))
        if ver==1:
            residenciaVer = int(input("¿Cuál residencia quieres ver? (Introduce el ID de la residencia): "))
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

            tablaResidencia.add_row([
                morada.id,
                morada.tipoAlojamiento,
                morada.habitaciones,
                morada.banhos,
                morada.camas,
                morada.precio,
                morada.flexDeCancelacion,
                morada.aPlus,
                morada.pets,
                morada.smokers,
            ])

            tablaDireccioin.add_row([
                morada.estado,
                morada.cp, 
                morada.calle, 
                morada.ciudad, 
                morada.pais
            ])

            print(tablaResidencia)
            tablaResidencia.clear()
            print(tablaDireccioin)
            tablaDireccioin.clear()
        
            eleccion = int(input("Reservar ya No(0)|Sí(1): "))
            if eleccion==1:
                idreserva = self.dbreservaciones.agendarReservaClientePerfil(cliente,morada.id)
                self.facturasbe.insertarFacturaResidenciaProceso(morada.id,idreserva,cliente.id)

        else:
            eleccion = int(input("¿Reservar alguna residencia? No(0)|Sí(1): "))
            if eleccion==1:
                res = int(input("¿Cuál residencia desea reservar? Ingrese el ID de la residencia"))
                self.dbreservaciones.agendarReservaClientePerfil(cliente,res)
                idreserva = self.dbreservaciones.agendarReservaClientePerfil(cliente,morada.id)
                self.facturasbe.insertarFacturaResidenciaProceso(morada.id,idreserva,cliente.id)

    def verReservasCliente(self, cliente):
        result = self.reservaslogic.getReservasCliente(cliente)

        table = PrettyTable()
        table.field_names = ["IdReserva","NombreCliente","TelefonoCliente","IdResidencia","FechaLlegada",
                            "FechaRetirada","Adultos","Ninhos","Bebes","TipoPago"]

        for reserva in result:
            table.add_row([
                reserva.idreserva,
                reserva.cliente,
                reserva.telephone,
                reserva.idresidencia,
                reserva.strFechaLlegada, 
                reserva.strFechaRetirada,
                reserva.intAdultos,
                reserva.intNinhos,
                reserva.intBebes,
                reserva.intTipoPago
                ])

        print(table)
        table.clear()
    
    def ClienteRegistro(self):
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

