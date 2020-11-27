from prettytable import PrettyTable
from DB_Accesibilidad_BE import AccesibilidadDB



class accesibilidad:
    self.dbaccesibilidad=AccesibilidadDB()
        

    def getAllAccessibilities(self):
        result = self.dbaccesibilidad.getAccessibilities()

        table = PrettyTable()
        table.field_names = ["IdAccesibilidad", "Nombre"]

        for accesibilidad in result:
            table.add_row([accesibilidad["idAccesibilidad"],accesibilidad["Nombre"]])

        print(table)
        table.clear()

    def addAccessibility(self):
        print("\nAdding a new accessibility...")
        accessibilityname = input("\nNombre de la accesibilidad: ")
        
        self.dbaccesibilidad.insertAccessibility(accessibilityname)
        idaccesibilidad=self.dbaccesibilidad.traerIDAccessibility(accessibilityname)

        print("\nSu accesibilidad se ha creado con éxito.\n")
        print(f"Su código de accesibilidad único es {idaccesibilidad}.\n")
        getAllAccessibilities()

    def updateAccessibility(self):
        print("\nUpdating an existing accessibility...")
        id = int(input("\nID de la accesibilidad a actualizar: "))

        accesibilidad = self.dbaccesibilidad.searchAccessibilityById(id)

        update = int(input("Update Name? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Name: {accesibilidad['Nombre']}")
            accessibilityname = input("New Name: ")
        else:
            accessibilityname = accesibilidad["Nombre"]

        self.dbaccesibilidad.updateAccesibilityBD(id,accessibilityname)
        print("\nLos cambios se han efectuado con éxito.")
        getAllAccessibilities()

    def deleteAccessibility(self):
        print("Deleting accessibility...")
        id = int(input("ID of accessibility to delete: "))

        self.dbaccesibilidad.deleteAccessibilityDB(id)
        print("La accesibilidad se ha removido con éxito.")
        getAllAccessibilities()
