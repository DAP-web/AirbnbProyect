from prettytable import PrettyTable
from DB_Tematica_BE import DBTematica

class TematicaBE:
    def __init__(self):
        self.dbtematica=DBTematica()

    def getAllTematicas():
        result = getTematicas()

        table = PrettyTable()
        table.field_names = ["IdTematica", "NombreTematica", "Descripcion"]

        for tematica in result:
            table.add_row([tematica["IdTematica"],tematica["NombreTematica"],tematica["Descripcion"]])

        print(table)
        table.clear()

    def addTematica():
        print("\nAdding a new tematica...")
        tematicaname = input("\nNombre de tematica: ")
        description = input("\nDescripción: ")

        insertTematica(tematicaname,description)
        idtematica=traerIDTematica(tematicaname,description)

        print("\nSu tematica se ha creado con éxito.\n")
        print(f"Su descripción es {idtematica}.\n")
        getAllTematicas()

    def updateTematica():
        print("\nUpdating an existing tematica...")
        id = int(input("\nID de la tematica a actualizar: "))

        tematica = searchTematicaById(id)

        update = int(input("Update Name? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Name: {tematica['NombreTematica']}")
            tematicaname = input("New Name: ")
        else:
            tematicaname = tematica["NombreTematica"]

        update = int(input("Update Descripcion? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Description: {tematica['Descripcion']}")
            code = input("New Description: ")
        else:
            code = tematica["Descripcion"]

        updateTematicaBD(id,tematicaname,description)
        print("\nLos cambios se han efectuado con éxito.")
        getAllTematicas()

    def deleteTematica():
        print("Deleting tematica...")
        id = int(input("ID of tematica to delete: "))

        deleteTematicaDB(id)
        print("La temática se ha removido con éxito.")
        getAllTematicas()
