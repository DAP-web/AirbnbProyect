from prettytable import PrettyTable
from DB_Ciudades_BE import (
    connection,
    getCities,
    insertCity,
    searchCityById,
    updateCityBD,
    traerIDCity,
    deleteCityDB
)

def getAllCities():
    result = getCities()

    table = PrettyTable()
    table.field_names = ["NombreCiudad", "NombrePais", "CodigoTelefonico"]

    for ciudades in result:
        table.add_row([ciudades["NombreCiudad"],ciudades["NombrePais"],ciudades["CodigoTelefonico"]])

    print(table)
    table.clear()

def addCity():
    print("\nAdding a new city...")
    cityname = input("\nNombre de ciudad: ")
    idcountry = int(input("\nCodigo de pais: "))

    insertCity(cityname,idcountry)
    idciudad=traerIDCity(cityname,idcountry)

    print("\nSu ciudad se ha creado con éxito.\n")
    print(f"Su código de ciudad único es {idciudad}.\n")
    getAllCities()

def updateCity():
    print("\nUpdating an existing city...")
    id = int(input("\nID de la ciudad a actualizar: "))

    ciudad = searchCityById(id)

    update = int(input("Update Name? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old Name: {ciudad['NombreCiudad']}")
        cityname = input("New Name: ")
    else:
        cityname = ciudad["NombreCiudad"]

    update = int(input("Update IdPais? 0-No - 1-Yes "))
    if update == 1:
        print(f"Old IdPais: {ciudad['IdPais']}")
        idcountry = int(input("New IdPais: "))
    else:
        idcountry = ciudad["IdPais"]

    updateCityBD(id,cityname,idcountry)
    print("\nLos cambios se han efectuado con éxito.")
    getAllCities()

def deleteCity():
    print("Deleting city...")
    id = int(input("ID of city to delete: "))

    deleteCityDB(id)
    print("La ciudad se ha removido con éxito.")
    getAllCities()
