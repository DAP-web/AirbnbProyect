from prettytable import PrettyTable
from DB_Servicios_BE import serviciosDB 

class serviciosBE:
    def __init__(self):
        self.servicios=serviciosDB()

    def getAllServices(self):
        result = self.servicios.getServices()

        table = PrettyTable()
        table.field_names = ["IdServicio","NombreServicio"]

        for servicio in result:
            table.add_row([servicio["idServicio"],servicio["NombreServicio"]])

        print(table)
        table.clear()

    def addService(self):
        print("\nAdding a new service...")
        name = input("\nNombreServicio: ")


        self.servicios.insertService(name)
        idservicio=self.servicios.traerIDServicio(name)

        print("\nSu servicio se ha registrado con éxito.\n")
        print(f"Su código de servico único es {idservicio}.\n")
        self.servicios.getAllServices()

    def updateService(self):
        print("\nUpdating an existing service...")
        id = int(input("\nID del servicio a actualizar: "))

        service = self.servicios.searchServiceById(id)

        update = int(input("Update Name? 0-No - 1-Yes "))
        if update == 1:
            print(f"Viejo Nombre del Servicio: {service['NombreServicio']}")
            name = input("Nuevo Nombre del Servicio: ")
        else:
            name = service["NombreServicio"]

    
        self.servicios.updateServiceBD(id,name)
        print("\nLos cambios se han efectuado con éxito.")
        self.servicios.getAllServices()

    def deleteService(self):
        print("\nDeleting service...")
        id = int(input("\nID of service to delete: "))

        self.servicios.deleteServiceDB(id)
        print("\nEl servicio se ha removido con éxito.")
        self.servicios.getAllServices()