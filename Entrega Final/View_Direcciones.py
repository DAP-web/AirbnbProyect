from prettytable import PrettyTable
from Logic_DireccionesLogic import DirectionLogic

class direccionesBE:
    def __init__(self):
        self.direcciones=DirectionLogic()

    def getAllDirections(self):
        result = self.direcciones.getDirections()

        table = PrettyTable()
        table.field_names = ["IdDireccion","Estado","CodigoPostal","Calle","idCiudad"]

        for direccion in result:
            table.add_row([
                direccion.id,
                direccion.state,
                direccion.postalcode,
                direccion.street,
                direccion.cityid
                ])

        print(table)
        table.clear()

    def addDirection(self):
        print("\nAdding a new direction...")
        state = input("\nEstado: ")
        postalcode = input("\nCodigoPostal: ")
        street = input("\nCalle: ")
        cityid = input("\nIdCiudad: ")

        self.direcciones.insertDirection(state,postalcode,street,cityid)
        iddireccion=self.direcciones.traerIDDireccion(state,postalcode,street,cityid)

        print("\nSu direccion se ha registrado con éxito.\n")
        print(f"Su código de direccion única es {iddireccion}.\n")
        self.getAllDirections()

    def updateDirection(self):
        print("\nUpdating an existing direction...")
        id = int(input("\nID de la direccion a actualizar: "))

        direction = self.direcciones.searchDirectionById(id)

        update = int(input("Update State? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old State: {direction.state}")
            state = input("New State: ")
        else:
            state = direction.state

        update = int(input("Update PostalCode? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old PostalCode: {direction.postalcode}")
            postalcode = input("New PostalCode: ")
        else:
            postalcode = direction.postalcode

        update = int(input("Update Street? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Stree: {direction.street}")
            street = input("New Street: ")
        else:
            street = direction.street

        update = int(input("Update CityId number? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old CityId number: {direction.cityid}")
            cityid = input("New CityId number: ")
        else:
            cityid = direction.cityid

        self.direcciones.updateDirectionBD(id,state,postalcode,street,cityid)
        print("\nLos cambios se han efectuado con éxito.")
        self.getAllDirections()

    def deleteDirection(self):
        print("Deleting direction...")
        id = int(input("ID of direction to delete: "))

        self.direcciones.deleteDirectionDB(id)
        print("La direccion se ha removido con éxito.")
        self.getAllDirections()

#Desde aqui empieza el codigo para procesos

    # def getDirection(self,direccion):   
    #     id = direccion.id
    #     direccion = self.direcciones.searchDirectionById(id)

    #     print(f"ID de direccion única: {direccion.id}")
    #     print(f"Estado: {direccion.state}")
    #     print(f"CodigoPostal: {direccion.postalcode}")
    #     print(f"Calle: {direccion.street}")
    #     print(f"IdCiudad: {direccion.cityid}")


    # def actualizarDireccion(self,direccion):
    #     print("\nUpdating an existing direction...")

    #     direction = direccion

    #     update = int(input("Update State? 0-No - 1-Yes "))
    #     if update == 1:
    #         print(f"Old State: {direction.state}")
    #         state = input("New State: ")
    #     else:
    #         state = direction.state

    #     update = int(input("Update PostalCode? 0-No - 1-Yes "))
    #     if update == 1:
    #         print(f"Old PostalCode: {direction.postalcode}")
    #         postalcode = input("New PostalCode: ")
    #     else:
    #         postalcode = direction.postalcode

    #     update = int(input("Update Street? 0-No - 1-Yes "))
    #     if update == 1:
    #         print(f"Old Street  {direction.street}")
    #         street = input("New Street: ")
    #     else:
    #         street = direction.street

    #     update = int(input("Update CityId number? 0-No - 1-Yes "))
    #     if update == 1:
    #         print(f"Old CityId number: {direction.cityid}")
    #         cityid = input("New IdCity number: ")
    #     else:
    #         cityid = direction.cityid
        
    #     self.direcciones.updateDirectionBD(direction.id,state,postalcode,street,cityid)
    #     direction = self.direcciones.searchDirectionById(direction.id)
    #     print("\nLos cambios se han efectuado con éxito.")
    #     self.getDirections(direction)