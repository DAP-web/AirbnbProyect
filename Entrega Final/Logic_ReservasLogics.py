from Core_dx_logic import Logic
from Objects_ReservaObj import ReservasObj
from Objects_ReservasViewObj import ReservasViewObj

class ReservasLogic(Logic):
    def __init__(self):
        super().__init__("reservaciones")
        self.idName="IdReserva"
        self.vistaReservas = "reservas"

    def getReservas(self):
        reservasList = super().getAllRows(self.vistaReservas)
        reservasViewObjList = []
        for reserva in reservasList:
            newClient = self.createReservaViewObj(reserva)
            reservasViewObjList.append(newClient)
        return reservasViewObjList

    def createReservaObj(self, reservasDict):
        reservaobj = ReservasObj(
            reservasDict["IdCliente"],
            reservasDict["IdResidencia"],
            reservasDict["FechaLlegada"],
            reservasDict["FechaRetirada"],
            reservasDict["Adultos"], 
            reservasDict["Ninhos"],
            reservasDict["Bebes"],
            reservasDict["TipoPago"],
            reservasDict["IdReserva"]
        )
        return reservaobj

    def createReservaViewObj(self, reservasDict):
        reservaoviewbj = ReservasViewObj(
            reservasDict["Cliente"],
            reservasDict["NumeroTelefonico"],
            reservasDict["IdResidencia"],
            reservasDict["FechaLlegada"], 
            reservasDict["FechaRetirada"],
            reservasDict["Adultos"],
            reservasDict["Ninhos"],
            reservasDict["Bebes"],
            reservasDict["TipoPago"],
            reservasDict["IdReserva"]
        )
        return reservaoviewbj

    def agendarReserva(self,idcliente,idresidencia,strFechaLlegada,strFechaRetirada,
                        intAdultos,intNinhos,intBebes,intTipoPago):
        database = self.database
        sql = f"""INSERT INTO `airbnb`.`reservaciones`
        (`IdCliente`, `IdResidencia`,
        `FechaLlegada`, `FechaRetirada`,
        `Adultos`, `Ninhos`,
        `Bebes`, `TipoPago`)
        VALUES
        ({idcliente},
        {idresidencia},
        '{strFechaLlegada}',
        '{strFechaRetirada}',
        {intAdultos},
        {intNinhos},
        {intBebes},
        {intTipoPago});"""
        rows = database.executeNonQueryRows(sql)
        return rows

    def buscarReservaU(self, id):
        rowDict = super().getRowById(self.idName,id,self.tableName)
        newReserva = self.createReservaObj(rowDict)
        return newReserva
    
    def actualizarReserva(self,id,strFechaLlegada,strFechaRetirada,
                        intAdultos,intNinhos,intBebes,intTipoPago):
        database = self.database
        sql = f"""UPDATE `airbnb`.`reservaciones`
        SET
        FechaLlegada = '{strFechaLlegada}',
        FechaRetirada = '{strFechaRetirada}',
        Adultos = {intAdultos},
        Ninhos = {intNinhos},
        Bebes = {intBebes},
        TipoPago = {intTipoPago}
        WHERE IdReserva = {id};
        """
        rows = database.executeNonQueryRows(sql)
        return rows

    def buscarReservaV(self, id):
        rowDict = super().getRowById(self.idName,id,self.vistaReservas)
        newReserva = self.createReservaObj(rowDict)
        return newReserva

    def traerIDReserva(self,idcliente,idresidencia,strFechaLlegada,strFechaRetirada,
                        intAdultos,intNinhos,intBebes,intTipoPago):
        database = self.database
        sql = f"""SELECT IdReserva
        FROM reservaciones
        WHERE IdCliente={idcliente} AND IdResidencia={idresidencia} AND FechaLlegada='{strFechaLlegada}' 
        AND FechaRetirada='{strFechaRetirada}' AND Adultos={intAdultos} AND Ninhos={intNinhos} 
        AND Bebes={intBebes} AND TipoPago={intTipoPago};
        """
        id = database.executeQueryOneRow(sql)
        return id["IdReserva"]
    
    def cancelarReserva(self, id):
        super().deleteRowById(self.idName, id, self.tableName)

    def chequeoCancelacion(self,idReserva):
        reservas={}
        database=self.database
        sql = f"SELECT IdResidencia FROM airbnb.reservas WHERE IdReserva={idReserva};"
        reservas = database.executeQueryOneRow(sql)
        return reservas["IdResidencia"]