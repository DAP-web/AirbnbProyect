from prettytable import PrettyTable
from Logic.Logic_TematicaLogic import TematicaLogic

class TematicaBE:
    def __init__(self):
        self.dbtematica=TematicaLogic()

    def getAllTematicas(self):
        result = self.dbtematica.getTematicas()

        table = PrettyTable()
        table.field_names = ["IdTematica", "NombreTematica", "Descripcion"]

        for tematica in result:
            table.add_row([
                tematica.id,
                tematica.tematicaname,
                tematica.description
                ])

        print(table)
        table.clear()

    def addTematica(self):
        print("\nAdding a new tematica...")
        tematicaname = input("\nNombre de tematica: ")
        description = input("\nDescripción: ")

        self.dbtematica.insertTematica(tematicaname,description)
        idtematica=self.dbtematica.traerIDTematica(tematicaname,description)

        print("\nSu tematica se ha creado con éxito.\n")
        print(f"Su descripción es {idtematica}.\n")
    
    def addTematicaProceso(self):
        print("\nAdding a new tematica...")
        tematicaname = input("\nNombre de tematica: ")
        description = input("\nDescripción: ")

        self.dbtematica.insertTematica(tematicaname,description)
        idtematica=self.dbtematica.traerIDTematica(tematicaname,description)

        print("\nSu tematica se ha creado con éxito.\n")
        print(f"Su descripción es {idtematica}.\n")
        return idtematica

    def updateTematica(self):
        print("\nUpdating an existing tematica...")
        id = int(input("\nID de la tematica a actualizar: "))

        tematica = self.dbtematica.searchTematicaById(id)

        update = int(input("Update Name? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Name: {tematica.tematicaname}")
            tematicaname = input("New Name: ")
        else:
            tematicaname = tematica.tematicaname

        update = int(input("Update Descripcion? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Description: {tematica.description}")
            description = input("New Description: ")
        else:
            description = tematica.description

        self.dbtematica.updateTematicaBD(id,tematicaname,description)
        print("\nLos cambios se han efectuado con éxito.")

    def deleteTematica(self):
        print("Deleting tematica...")
        id = int(input("ID of tematica to delete: "))

        self.dbtematica.deleteTematicaDB(id)
        print("La temática se ha removido con éxito.")
