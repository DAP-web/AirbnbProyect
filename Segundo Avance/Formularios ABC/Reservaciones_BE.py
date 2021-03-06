from prettytable import PrettyTable
from DB_Reservaciones_BE import reservasBD
from DB_Residencia_BE import ResidenciaDB
class reservaciones:
    def __init__(self):
        self.dbreservas=reservasBD()
        self.dbresidencia=ResidenciaDB()

    def getAllReservas(self,):
        result = self.dbreservas.getReservas()

        table = PrettyTable()
        table.field_names = ["IdReserva","NombreCliente","TelefonoCliente","IdResidencia","FechaLlegada",
                            "FechaRetirada","Adultos","Ninhos","Bebes","TipoPago"]

        for reserva in result:
            table.add_row([
                reserva["IdReserva"],
                reserva["Cliente"],
                reserva["NumeroTelefonico"],
                reserva["IdResidencia"],
                reserva["FechaLlegada"], 
                reserva["FechaRetirada"],
                reserva["Adultos"],
                reserva["Ninhos"],
                reserva["Bebes"],
                reserva["TipoPago"]
                ])

        print(table)
        table.clear()

    def agendarReservaV(self):
        print("\nAdding a new client...")
        idCliente = int(input("\nNo. de Cliente: "))
        idResidencia = int(input("\nNo. Residencia: "))
        strFechaLlegada = input("\nFecha de llegada (dd-mm-yyyy): ")
        strHoraLlegada = input("\nHora de llegada (hh:mm:ss): ")
        strFechaRetirada = input("\nFecha de retirada (dd-mm-yyyy): ")
        strHoraRetirada = input("\nHora de retirada (hh:mm:ss): ")
        intAdultos = int(input("\nNo. de adultos: "))
        intNinhos = int(input("\nNo. de niños: "))
        intBebes = int(input("\nNo. de bebés: "))
        intTipoPago = int(input("\nTipo de pago (0-Tarjeta | 1-Efectivo): "))

        strLlegada = strFechaLlegada+" "+strHoraLlegada
        strRetirada = strFechaRetirada+" "+strHoraRetirada

        self.dbreservas.agendarReserva(idCliente,idResidencia,strLlegada,strRetirada,intAdultos,intNinhos,intBebes,intTipoPago)
        idreserva=self.dbreservas.traerIDReserva(idCliente,idResidencia,strLlegada,strRetirada,intAdultos,intNinhos,intBebes,intTipoPago)

        print(f"\nSu reserva se ha agendado con éxito. Su número de reservación es {idreserva}\n")
        self.getAllReservas()

    def modificarReserva(self):
        print("\nUpdating a booking...")
        id = int(input("\nID de la reserva a modificar: "))

        reserva = self.dbreservas.buscarReservaU(id)

        update = int(input("¿Actualizar fecha de llegada? 0-No - 1-Sí "))
        if update == 1:
            print(f"Fecha de Llegada Vieja: {reserva['FechaLlegada']}")
            strfechallegada = input("Nueva Fecha de Llegada (dd-mm-yyyy): ")
            strhorallegada = input("Nueva hora de llegada (hh:mm:ss): ")
            strllegada = strfechallegada+' '+strhorallegada
        else:
            strllegada = reserva["FechaLlegada"]

        update = int(input("¿Actualizar fecha de retirada? 0-No - 1-Sí "))
        if update == 1:
            print(f"Fecha de retirada Vieja: {reserva['FechaRetirada']}")
            strfecharetirada = input("Nueva Fecha de Retirada (dd-mm-yyyy): ")
            strhoraretirada = input("Nueva hora de retirada (hh:mm:ss): ")
            strRetirada = strfecharetirada+' '+strhoraretirada
        else:
            strRetirada = reserva["FechaRetirada"]

        update = int(input("¿Actualizar el número de adultos? 0-No - 1-Sí "))
        if update == 1:
            print(f"Número de adultos anterior: {reserva['Adultos']}")
            intAdultos = int(input("Nuevo número de adultos: "))
        else:
            intAdultos = reserva["Adultos"]

        update = int(input("¿Actualizar el número de niños? 0-No - 1-Sí "))
        if update == 1:
            print(f"Número de niños anterior: {reserva['Ninhos']}")
            intNinhos = int(input("Nuevo número de ninños: "))
        else:
            intNinhos = reserva["Ninhos"]

        update = int(input("¿Actualizar el número de bebés? 0-No - 1-Sí "))
        if update == 1:
            print(f"Número de bebés anterior: {reserva['Bebes']}")
            intBebes = int(input("Nuevo número de bebés: "))
        else:
            intBebes = reserva["Bebes"]

        update = int(input("¿Actualizar el tipo de pago? 0-No - 1-Sí "))
        if update == 1:
            print(f"Tipo de pago anterior: {reserva['TipoPago']}")
            intTipoPago = int(input("Nuevo tipo de pago: "))
        else:
            intTipoPago = reserva["TipoPago"]

        self.dbreservas.actualizarReserva(id,strllegada,strRetirada,intAdultos,intNinhos,intBebes,intTipoPago)
        print("\nLos cambios se han efectuado con éxito.")
        # self.getAllReservas()

    def cancelacionDeReserva(self):
        print("Cancelando reserva...")
        id = int(input("ID de reserva único: "))

        residencia = self.dbreservas.chequeoCancelacion(id)
        chequeo = self.dbresidencia.chequeoFlexCancelacion(residencia["IdResidencia"])

        if chequeo["FlexibilidadDeCancelacion"]==0:
            print("\nLa residencia no tiene flexibilidad de cancelación.")
            print("No se ha podido cancelar la reserva.")
        else:
            self.dbreservas.cancelarReserva(id)
            print("\nLa reserva se ha cancelado con éxito.")

    #A PARTIR DE AQUI LAS FUNCIONES SON PARA AGENDARLAS DESDE EL PERFIL DE UN CLIENTE
    #Esta parte es de procesos no de tablas
    def agendarReservaClientePerfil(self,cliente,residencia):
        print("\nAgregando una nueva reserva...")
        idCliente = int(cliente["idClientes"])
        idResidencia = int(residencia)
        strFechaLlegada = input("\nFecha de llegada (dd-mm-yyyy): ")
        strHoraLlegada = input("\nHora de llegada (hh:mm:ss): ")
        strFechaRetirada = input("\nFecha de retirada (dd-mm-yyyy): ")
        strHoraRetirada = input("\nHora de retirada (hh:mm:ss): ")
        intAdultos = int(input("\nNo. de adultos: "))
        intNinhos = int(input("\nNo. de niños: "))
        intBebes = int(input("\nNo. de bebés: "))
        intTipoPago = int(input("\nTipo de pago (0-Tarjeta | 1-Efectivo): "))

        strLlegada = strFechaLlegada+" "+strHoraLlegada
        strRetirada = strFechaRetirada+" "+strHoraRetirada

        self.dbreservas.agendarReserva(idCliente,idResidencia,strLlegada,strRetirada,intAdultos,intNinhos,intBebes,intTipoPago)
        idreserva=self.dbreservas.traerIDReserva(idCliente,idResidencia,strLlegada,strRetirada,intAdultos,intNinhos,intBebes,intTipoPago)

        print(f"\nSu reserva se ha agendado con éxito. Su número de reservación es {idreserva}\n")