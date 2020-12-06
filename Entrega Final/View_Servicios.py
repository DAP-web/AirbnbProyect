from prettytable import PrettyTable
from Logic_ServiciosLogic import ServiceLogic

class serviciosBE:
    def __init__(self):
        self.dbcliente=ServiceLogic()

    def getAllServices(self):
        result = self.dbcliente.getServices()

        table = PrettyTable()
        table.field_names = ["IdServicio","NombreServicio"]

        for servicio in result:
            table.add_row([
                    servicio.id,
                    servicio.name
                ])

        print(table)
        table.clear()

    def addService(self):
        print("\nAdding a new service...")
        name = input("\nNombreServicio: ")

        self.dbcliente.insertService(name)
        idservicio=self.dbcliente.traerIDServicio(name)

        print("\nSu servicio se ha registrado con éxito.\n")
        print(f"Su código de servico único es {idservicio}.\n")
        self.getAllServices()
    
    def updateService(self):
        print("\nUpdating an existing service...")
        id = int(input("\nID del servicio a actualizar: "))

        service = self.dbcliente.searchServiceById(id)

        update = int(input("Update Name? 0-No - 1-Yes "))
        if update == 1:
            print(f"Viejo Nombre del Servicio: {service.name}")
            name = input("Nuevo Nombre del Servicio: ")
        else:
            name = service.name
    
        self.dbcliente.updateServiceBD(id,name)
        print("\nLos cambios se han efectuado con éxito.")
        self.getAllServices()

    def deleteService(self):
        print("\nDeleting service...")
        id = int(input("\nID of service to delete: "))

        self.dbcliente.deleteServiceDB(id)
        print("\nEl servicio se ha removido con éxito.")
        self.getAllServices()