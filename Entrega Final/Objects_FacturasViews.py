class FacturasViewReservasObj:
    #metodo inicializador para facturas de reservas
    def __init__(self, idfactura,idresidencia,idreserva,precio,
    cliente,fechaemitida,telefono,iva,subtotal,cupon):
        self.idfactura=idfactura
        self.idresidencia=idresidencia
        self.idreserva=idreserva
        self.precio = precio
        self.cliente=cliente
        self.fechaEmitida=fechaemitida
        self.numero=telefono
        self.iva=iva
        self.subtotal=subtotal
        self.cupon=cupon

class FacturasViewExpObj:
    #metodo inicializador para facturas de experiencias
    def __init__(self,idfactura,idexperiencia,precio,cliente,telefono,iva,subtotal,cupon):
        self.idfactura=idfactura
        self.idexperiencia=idexperiencia
        self.precio=precio
        self.cliente=cliente
        self.numero=telefono
        self.iva=iva
        self.subtotal=subtotal
        self.cupon=cupon
