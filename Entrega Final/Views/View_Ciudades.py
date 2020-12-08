from prettytable import PrettyTable
from Logic_CiudadesLogic import CiudadesLogic

class ciudadesBE:
    def __init__(self):
        self.dbciudad=CiudadesLogic()

    def getAllCities(self):
        result = self.dbciudad.getCities()

        table = PrettyTable()
        table.field_names = ["IdCiudad", "NombreCiudad", "IdPais"]

        for ciudades in result:
            table.add_row([
                ciudades.id,
                ciudades.cityname,
                ciudades.idcountry
                ])

        print(table)
        table.clear()

    def addCity(self):
        print("\nAdding a new city...")
        cityname = input("\nNombre de ciudad: ")
        idcountry = input("\nCodigo de pais: ")

        self.dbciudad.insertCity(cityname,idcountry)
        idciudad=self.dbciudad.traerIDCity(cityname,idcountry)

        print("\nSu ciudad se ha creado con éxito.\n")
        print(f"Su código de ciudad único es {idciudad}.\n")
        self.getAllCities()

    def updateCity(self):
        print("\nUpdating an existing city...")
        id = int(input("\nID de la ciudad a actualizar: "))

        ciudad = self.dbciudad.searchCityById(id)

        update = int(input("Update Name? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Name: {ciudad.cityname}")
            cityname = input("New Name: ")
        else:
            cityname = ciudad.cityname

        update = int(input("Update IdPais? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old IdPais: {ciudad.idcountry}")
            idcountry = input("New IdPais: ")
        else:
            idcountry = ciudad.idcountry

        self.dbciudad.updateCityBD(id,cityname,idcountry)
        print("\nLos cambios se han efectuado con éxito.")
        self.getAllCities()

    def deleteCity(self):
        print("Deleting city...")
        id = int(input("ID of city to delete: "))

        self.dbciudad.deleteCityDB(id)
        print("La ciudad se ha removido con éxito.")
        self.getAllCities()
