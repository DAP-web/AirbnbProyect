from prettytable import PrettyTable
from Logic_FacturasLogic import FacturasLogic
from Logic_ResidenciasLogic import ResidenciaLogic
from Logic_ExperienciasLogic import ExperienciaLogic

class facturasBE:
    def __init__(self):
        self.dbfacturas = FacturasLogic()
        self.dbresidencias = ResidenciaLogic()
        self.dbexperiencias = ExperienciaLogic()
    
    def getFacturasResidencias(self):
        result = self.dbfacturas.obtenerFacturasResidencias()

        table = PrettyTable()
        table.field_names = [
            "idFactura", 
            "IdResidencia", 
            "IdReserva", 
            "Precio", 
            "Cliente", 
            "FechaEmitida", 
            "NumeroTelefonico", 
            "IVA", 
            "Subtotal", 
            "Cupon"
        ]

        for factura in result:
            table.add_row([
                factura.idfactura,
                factura.idresidencia,
                factura.idreserva,
                factura.precio,
                factura.cliente,
                factura.fechaEmitida,
                factura.numero,
                factura.iva,
                factura.subtotal,
                factura.cupon
            ])
        print(table)
        table.clear()
    
    def getFacturasExp(self):
        result = self.dbfacturas.obtenerFacturasExperiencias()

        table = PrettyTable()
        table.field_names = [
            "idFactura", 
            "IdExp", 
            "PrecioIndividual", 
            "Cliente", 
            "NumeroTelefonico", 
            "IVA", 
            "Subtotal", 
            "Cupon"
        ]

        for factura in result:
            table.add_row([
                factura.idfactura,
                factura.idexperiencia,
                factura.precio,
                factura.cliente,
                factura.numero,
                factura.iva,
                factura.subtotal,
                factura.cupon
            ])
        print(table)
        table.clear()

    def insertarFacturaResidencia(self):
        idresidencia = int(input("ID de la residencia: "))
        reserva = int(input("ID de la reserva: "))
        cliente = int(input("ID Cliente: "))

        #hacer un metodo para ir a traer el precio de la residencia
        residencia = self.dbresidencias.searchResidenciasById(idresidencia)
        
        cupon = int(input("¿Tiene cupón? (0-No||1-Sí): "))

        if cupon==0:
            subtotal = ((float(residencia.precio))*0.13)+((float(residencia.precio))*1.09)
        else:
            subtotal = ((float(residencia.precio))*1.13)

        self.dbfacturas.agregarFacturaResidencia(idresidencia,reserva,cliente,subtotal,cupon)
        print("La factura se ha registrado con éxito.")
    
    def insertarFacturaExp(self):
        idexperiencia = int(input("ID de la experiencia: "))
        cliente = int(input("ID Cliente: "))

        #hacer un metodo para ir a traer el precio de la residencia
        experiencia = self.dbexperiencias.searchExperienciaById(idexperiencia)
        cupon = int(input("¿Tiene cupón? (0-No||1-Sí): "))

        if cupon==0:
            subtotal = (float(experiencia.precio)*1.19)
        else:
            subtotal = (float(experiencia.precio)*1.13)

        self.dbfacturas.agregarFacturaExp(idexperiencia,cliente,subtotal,cupon)
        print("La factura se ha registrado con éxito.")

    def insertarFacturaResidenciaProceso(self, residencia, reserva, cliente):
        idresidencia = residencia
        reserva = reserva
        cliente = cliente

        #hacer un metodo para ir a traer el precio de la residencia
        residencia = self.dbresidencias.searchResidenciasById(idresidencia)
        
        cupon = int(input("¿Tiene cupón? (0-No||1-Sí): "))

        if cupon==0:
            subtotal = ((float(residencia.precio))*0.13)+((float(residencia.precio))*1.09)
        else:
            subtotal = ((float(residencia.precio))*1.13)

        self.dbfacturas.agregarFacturaResidencia(idresidencia,reserva,cliente,subtotal,cupon)
        print("La factura se ha registrado con éxito.")

    def insertarFacturaExpProceso(self, experiencia, cliente):
        idexperiencia = experiencia
        cliente = cliente

        #hacer un metodo para ir a traer el precio de la residencia
        experiencia = self.dbexperiencias.searchExperienciaById(idexperiencia)
        cupon = int(input("¿Tiene cupón? (0-No||1-Sí): "))

        if cupon==0:
            subtotal = (float(experiencia.precio)*1.19)
        else:
            subtotal = (float(experiencia.precio)*1.13)
            
        self.dbfacturas.agregarFacturaExp(idexperiencia,cliente,subtotal,cupon)
        print("La factura se ha registrado con éxito.")

    def verMisFacturas(self, cliente):
        print("Facturas de Experiencias: ")
        result = self.dbfacturas.verMisFacturas(cliente.id,True)

        table = PrettyTable()
        table.field_names = [
            "idFactura", 
            "IdExp", 
            "PrecioIndividual", 
            "Cliente", 
            "NumeroTelefonico", 
            "IVA", 
            "Subtotal", 
            "Cupon"
        ]

        for factura in result:
            table.add_row([
                factura.idfactura,
                factura.idexperiencia,
                factura.precio,
                factura.cliente,
                factura.numero,
                factura.iva,
                factura.subtotal,
                factura.cupon
            ])
        print(table)
        table.clear()

        print("Facturas de Reservaciones: ")
        result1 = self.dbfacturas.verMisFacturas(cliente.id, False)
        table1 = PrettyTable()
        table1.field_names = [
            "idFactura", 
            "IdResidencia", 
            "IdReserva", 
            "Precio", 
            "Cliente", 
            "FechaEmitida", 
            "NumeroTelefonico", 
            "IVA", 
            "Subtotal", 
            "Cupon"
        ]

        for factura in result1:
            table1.add_row([
                factura.idfactura,
                factura.idresidencia,
                factura.idreserva,
                factura.precio,
                factura.cliente,
                factura.fechaEmitida,
                factura.numero,
                factura.iva,
                factura.subtotal,
                factura.cupon
            ])
        print(table1)
        table1.clear()