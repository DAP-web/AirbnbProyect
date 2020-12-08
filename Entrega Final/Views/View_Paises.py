from prettytable import PrettyTable
from Logic.Logic_PaisesLogic import PaisesLogic

class paisesBE:
    def __init__(self):
        self.dbpais=PaisesLogic()

    def getAllCountries(self):
        result = self.dbpais.getCountries()

        table = PrettyTable()
        table.field_names = ["IdPais", "NombrePais", "CodigoTelefonico"]

        for paises in result:
            table.add_row([
                paises.id,
                paises.countryname,
                paises.code
                ])

        print(table)
        table.clear()

    def addCountry(self):
        print("\nAdding a new country...")
        countryname = input("\nNombre de pais: ")
        code = input("\nCodigo telefonico: ")

        self.dbpais.insertCountry(countryname,code)
        idpais=self.dbpais.traerIDCountry(countryname,code)
        
        print("\nSu pais se ha creado con éxito.\n")
        print(f"Su código de país único es {idpais}.\n")
        self.getAllCountries()

    def updateCountry(self):
        print("\nUpdating an existing country...")
        id = int(input("\nID del pais a actualizar: "))

        pais = self.dbpais.searchCountryById(id)

        update = int(input("Update Name? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Name: {pais.countryname}")
            countryname = input("New Name: ")
        else:
            countryname = pais.countryname

        update = int(input("Update PhoneCode? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old PhoneCode: {pais.code}")
            code = input("New PhoneCode: ")
        else:
            code = pais.code

        self.dbpais.updateCountryBD(id,countryname,code)
        print("\nLos cambios se han efectuado con éxito.")
        self.getAllCountries()

    def deleteCountry(self):
        print("Deleting country...")
        id = int(input("ID of country to delete: "))

        self.dbpais.deleteCountryDB(id)
        print("El país se ha removido con éxito.")
        self.getAllCountries()
        