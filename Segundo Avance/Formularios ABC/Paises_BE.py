from prettytable import PrettyTable
from DB_Paises_BE import (
    connection,
    getCountries,
    insertCountry,
    searchCountryById,
    updateCountryBD,
    traerIDCountry,
    deleteCountryDB
)

def getAllCountries():
    result = getCountries()

    table = PrettyTable()
    table.field_names = ["IdPais", "NombrePais", "CodigoTelefonico"]

    for paises in result:
        table.add_row([paises["idPais"],paises["NombrePais"],paises["CodigoTelefonico"]])

    print(table)
    table.clear()

def addCountry():
    print("\nAdding a new country...")
    countryname = input("\nNombre de pais: ")
    code = input("\nCodigo telefonico: ")

    insertCountry(countryname,code)
    idpais=traerIDCountry(countryname,code)

    print("\nSu pais se ha creado con éxito.\n")
    print(f"Su código de país único es {idpais}.\n")
    getAllCountries()

def updateCountry():
    print("\nUpdating an existing country...")
    id = int(input("\nID del pais a actualizar: "))

    pais = searchCountryById(id)

    update = int(input("Update Name? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Name: {pais['NombrePais']}")
        countryname = input("New Name: ")
    else:
        countryname = pais["NombrePais"]

    update = int(input("Update PhoneCode? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old PhoneCode: {pais['CodigoTelefonico']}")
        code = input("New PhoneCode: ")
    else:
        code = pais["CodigoTelefonico"]

    updateCountryBD(id,countryname,code)
    print("\nLos cambios se han efectuado con éxito.")
    getAllCountries()

def deleteCountry():
    print("Deleting country...")
    id = int(input("ID of country to delete: "))

    deleteCountryDB(id)
    print("El país se ha removido con éxito.")
    getAllCountries()
