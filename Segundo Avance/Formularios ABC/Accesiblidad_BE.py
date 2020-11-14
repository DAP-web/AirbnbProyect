from prettytable import PrettyTable
from DB_Accesibilidad_BE import (
    connection,
    getAccessibilities,
    insertAccessibility,
    searchAccessibilityById,
    updateAccessibilityBD,
    traerIDAccessibility,
    deleteAccessibilityDB
)

def getAccessibilities():
    result = getAccessibilities()

    table = PrettyTable()
    table.field_names = ["IdAccesibilidad", "Nombre"]

    for accesibilidad in result:
        table.add_row([accesibilidad["idAccesibilidad"],accesibilidad["Nombre"]])

    print(table)
    table.clear()

def addAccessibility():
    print("\nAdding a new accessibility...")
    accessibilityname = input("\nNombre de la accesibilidad: ")
    
    insertAccessibility(accessibilityname)
    idaccessibility=traerIDAccessibility(accessibilityname)

    print("\nSu accesibilidad se ha creado con éxito.\n")
    print(f"Su código de accesibilidad único es {idaccesibilidad}.\n")
    getAllAccessibilities()

def updateAccessibility():
    print("\nUpdating an existing accessibility...")
    id = int(input("\nID de la accesibilidad a actualizar: "))

    accesibility = searchAccessibilityById(id)

    update = int(input("Update Name? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Name: {accesibilidad['Nombre']}")
        accessibilityname = input("New Name: ")
    else:
        accessibilityname = accesibilidad["Nombre"]

    

    updateAccessibilityBD(id,accessibilityname,code)
    print("\nLos cambios se han efectuado con éxito.")
    getAllAccessibilities()

def deleteAccessibility():
    print("Deleting accessibility...")
    id = int(input("ID of accessibility to delete: "))

    deleteAccessibility(id)
    print("La accesibilidad se ha removido con éxito.")
    getAllAccessibilities()
