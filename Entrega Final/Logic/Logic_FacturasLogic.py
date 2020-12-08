from Core.Core_dx_logic import Logic
from Objects.Objects_FacturasObj import FacturaObj
from Objects.Objects_FacturasViews import FacturasViewExpObj,FacturasViewReservasObj

class FacturasLogic(Logic):
    def __init__(self):
        super().__init__("factura")
        self.idName="idFactura"
        self.vistaResFac = "facturaresidencias"
        self.vistaExpFac = "facturaexperiencias"
    
    def obtenerFacturasResidencias(self):
        facturasList = super().getAllRows(self.vistaResFac)
        facturasObjList=[]
        for factura in facturasList:
            nuevaFactura = self.createFacturaResidenciaViewObj(factura)
            facturasObjList.append(nuevaFactura)
        return facturasObjList

    def obtenerFacturasExperiencias(self):
        facturasList = super().getAllRows(self.vistaExpFac)
        facturasObjList=[]
        for factura in facturasList:
            nuevaFactura = self.createFacturaExpViewObj(factura)
            facturasObjList.append(nuevaFactura)
        return facturasObjList
    
    def createFacturaObj(self,facturaDict):
        facturaobj = FacturaObj([ 
            facturaDict["IdResidencia"], 
            facturaDict["IdReserva"], 
            facturaDict["IdCliente"], 
            facturaDict["IdExp"], 
            facturaDict["IVA"], 
            facturaDict["Subtotal"], 
            facturaDict["Cupon"],
            facturaDict["idFactura"]
        ])
    
    def createFacturaResidenciaViewObj(self,facturaResidenciaDict):
        facturaResidenciaObj=FacturasViewReservasObj(
            facturaResidenciaDict["idFactura"], 
            facturaResidenciaDict["IdResidencia"], 
            facturaResidenciaDict["IdReserva"], 
            facturaResidenciaDict["Precio"], 
            facturaResidenciaDict["Cliente"], 
            facturaResidenciaDict["FechaEmitida"], 
            facturaResidenciaDict["NumeroTelefonico"], 
            facturaResidenciaDict["IVA"], 
            facturaResidenciaDict["Subtotal"], 
            facturaResidenciaDict["Cupon"]
        )
        return facturaResidenciaObj
    
    def createFacturaExpViewObj(self,facturaExpDict):
        facturaExpObj = FacturasViewExpObj(
            facturaExpDict["idFactura"], 
            facturaExpDict["IdExp"], 
            facturaExpDict["PrecioIndividual"], 
            facturaExpDict["Cliente"], 
            facturaExpDict["NumeroTelefonico"], 
            facturaExpDict["IVA"], 
            facturaExpDict["Subtotal"], 
            facturaExpDict["Cupon"]
        )
        return facturaExpObj

    def agregarFacturaResidencia(self, idresidencia, idreserva, 
    idcliente, subtotal, cupon):
        database = self.database
        sql = f"""INSERT INTO `airbnb`.`factura`
        (`IdResidencia`,
        `IdReserva`,
        `IdCliente`,
        `IdExp`,
        `IVA`,
        `Subtotal`,
        `Cupon`)
        VALUES
        ({idresidencia},
        {idreserva},
        {idcliente},
        NULL,
        {13},
        {subtotal:.2f},
        {cupon});
        """
        rows = database.executeNonQueryRows(sql)
        return rows
    
    def agregarFacturaExp(self, idexperiencia, idcliente, subtotal, cupon):
        database = self.database
        sql = f"""INSERT INTO `airbnb`.`factura`
        (`IdResidencia`,
        `IdReserva`,
        `IdCliente`,
        `IdExp`,
        `IVA`,
        `Subtotal`,
        `Cupon`)
        VALUES
        (NULL,
        NULL,
        {idcliente},
        {idexperiencia},
        {13},
        {subtotal:.2f},
        {cupon});
        """
        rows = database.executeNonQueryRows(sql)
        return rows
    
    def botarFactura(self, idreserva):
        database = self.database
        sql = f"delete from factura where IdReserva = {idreserva};"
        rows = database.executeNonQueryRows(sql)
        return rows

    def verMisFacturasDB(self, cliente, boolExp):
        database = self.database
        facturasObjList=[]
        if boolExp:
            sql = f"""select facturaexperiencias.*
            from facturaexperiencias 
                inner join factura on facturaexperiencias.idFactura = factura.idFactura
                inner join clientes on factura.IdCliente = clientes.idClientes
            where clientes.idClientes = {cliente};
            """
            facturasList = database.executeQueryRows(sql)
            
            for factura in facturasList:
                nuevaFactura = self.createFacturaExpViewObj(factura)
                facturasObjList.append(nuevaFactura)
            return facturasObjList
        else:
            sql = f"""select facturaresidencias.*
            from facturaresidencias 
                inner join factura on facturaresidencias.idFactura = factura.idFactura
                inner join clientes on factura.IdCliente = clientes.idClientes
            where clientes.idClientes = {cliente};
            """
            facturasList = database.executeQueryRows(sql)
            for factura in facturasList:
                nuevaFactura = self.createFacturaResidenciaViewObj(factura)
                facturasObjList.append(nuevaFactura)
            return facturasObjList

    def verUnaFactura(self, cliente, boolExp):
        database = self.database
        if boolExp:
            sql = f"""select facturaexperiencias.*
            from facturaexperiencias 
                inner join factura on facturaexperiencias.idFactura = factura.idFactura
                inner join clientes on factura.IdCliente = clientes.idClientes
            where clientes.idClientes = {cliente}
            order by idFactura desc
            limit 1;
            """
            facturasList = database.executeQueryOneRow(sql)
            facturaObj = self.createFacturaExpViewObj(facturasList)
            return facturaObj
        else:
            sql = f"""select facturaresidencias.*
            from facturaresidencias 
                inner join factura on facturaresidencias.idFactura = factura.idFactura
                inner join clientes on factura.IdCliente = clientes.idClientes
            where clientes.idClientes = {cliente}
            order by idFactura desc
            limit 1;
            """
            facturasList = database.executeQueryOneRow(sql)
            facturaObj = self.createFacturaResidenciaViewObj(facturasList)
            return facturaObj