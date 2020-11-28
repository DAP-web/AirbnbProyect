from prettytable import PrettyTable
from DB_ResidenciaAccesibilidad_BE import DBRA

class raccesibilidadBE:
    def __init__(self):
        self.dbraccesibilidad=DBRA()

    def getAllRAccessibilities(self):
        result = self.dbraccesibilidad.getRAccessibilities()

        table = PrettyTable()
        table.field_names = ["Nombre", "Descripcion"]

        for raccesibilidad in result:
            table.add_row([
                raccesibilidad["Nombre"],
                raccesibilidad["Descripcion"],
                ])

        print(table)
        table.clear()

    def addRAccessibilities(self):
        print("\nAdding a new residencia accessibility...")
        idaccesibilidad = input("\nNombre de la accesibilidad: ")
        idresidencia = int(input("\nCodigo de la residencia: "))

        self.dbraccesibilidad.insertRAccessibility(idaccesibilidad, idresidencia)
        idraccesibilidad=self.dbraccesibilidad.traerIDRAccessibility(idaccesibilidad, idresidencia)

        print("\nSu residencia accessibility se ha creado con éxito.\n")
        print(f"Su código de residencia accessibility único es {idraccesibilidad}.\n")
        self.getAllRAccessibilities()

    def updateRAccessibility(self):
        print("\nUpdating an existing residencia accessibility...")
        id = int(input("\nID de la residencia accessibility a actualizar: "))

        raccesibilidad = self.dbraccesibilidad.searchRAccessibility(id)


        update = int(input("Update Name? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Name: {raccesibilidad['Nombre']}")
            nameraccesibilidad = input("New Name: ")
        else:
            nameraccesibilidad = raccesibilidad["Nombre"]

        update = int(input("Update Descripcion? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Descripcion: {raccesibilidad['Descripcion']}")
            descripcionraccesibilidad = int(input("New Descripcion: "))
        else:
             descripcionraccesibilidad = raccesibilidad["Descripcion"]

        self.dbraccesibilidad.updateRAccessibilityBD(id)
        print("\nLos cambios se han efectuado con éxito.")
        self.getAllRAccessibilities()

    def deleteRAccessibility(self):
        print("Deleting residencia accesibility...")
        id = int(input("ID of residencia accessibility to delete: "))

        self.dbraccesibilidad.deleteRAccessibilityDB(id)
        print("La residencia accessibility se ha removido con éxito.")
        self.getAllRAccessibilities()
