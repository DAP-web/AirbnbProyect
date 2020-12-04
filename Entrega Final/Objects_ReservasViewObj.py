class ReservasViewObj:
    def __init__(self,idreserva,strCliente,strTelephone,idresidencia,strFechaLlegada,strFechaRetirada,
                intAdultos,intNinhos,intBebes,intTipoPago):
        self.idreserva=idreserva
        self.cliente=strCliente
        self.telephone = strTelephone
        self.idresidencia=idresidencia
        self.strFechaLlegada=strFechaLlegada
        self.strFechaRetirada=strFechaRetirada
        self.intAdultos=intAdultos
        self.intNinhos=intNinhos
        self.intBebes=intBebes
        self.intTipoPago=intTipoPago