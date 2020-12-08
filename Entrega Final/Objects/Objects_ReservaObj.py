class ReservasObj:
    def __init__(self,idcliente,idresidencia,strFechaLlegada,strFechaRetirada,
                        intAdultos,intNinhos,intBebes,intTipoPago,id):
        self.idreserva=id
        self.idcliente=idcliente
        self.idresidencia=idresidencia
        self.strFechaLlegada=strFechaLlegada
        self.strFechaRetirada=strFechaRetirada
        self.intAdultos=intAdultos
        self.intNinhos=intNinhos
        self.intBebes=intBebes
        self.intTipoPago=intTipoPago

    def __init__(self,idcliente,idresidencia,strFechaLlegada,strFechaRetirada,
                    intAdultos,intNinhos,intBebes,intTipoPago,id=0):
        self.idreserva=id
        self.idcliente=idcliente
        self.idresidencia=idresidencia
        self.strFechaLlegada=strFechaLlegada
        self.strFechaRetirada=strFechaRetirada
        self.intAdultos=intAdultos
        self.intNinhos=intNinhos
        self.intBebes=intBebes
        self.intTipoPago=intTipoPago
        