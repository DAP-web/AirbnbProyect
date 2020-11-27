from prettytable import PrettyTable
from DB_Direcciones_BE import direccionesDB 

class direccionesBE:
    def __init__(self):
        self.direcciones=direccionesDB()

    def getAllDirections(self):
        result = self.direcciones.getDirections()

        table = PrettyTable()
        table.field_names = ["IdDireccion","Estado","CodigoPostal","Calle","IdCiudad"]

        for direccion in result:
            table.add_row([direccion["IdDireccion"],direccion["Estado"],direccion["CodigoPostal"],direccion["Calle"],direccion["IdCiudad"]])

        print(table)
        table.clear()

    def addDirection(self):
        print("\nAdding a new direction...")
        state = input("\nEstado: ")
        postalcode = input("\nCodigoPostal: ")
        street = input("\nCalle: ")
        idcity = input("\nIdCiudad: ")

        self.direcciones.insertDirection(state,postalcode,street,idcity)
        iddireccion=self.direcciones.traerIDDireccion(state,postalcode,street,idcity)

        print("\nSu direccion se ha registrado con éxito.\n")
        print(f"Su código de direccion única es {iddireccion}.\n")
        self.direcciones.getAllDirections()

    def updateDirection(self):
        print("\nUpdating an existing direction...")
        id = int(input("\nID de la direccion a actualizar: "))

        direction = self.direcciones.searchDirectionById(id)

        update = int(input("Update State? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old State: {direction['Estado']}")
            state = input("New State: ")
        else:
            state = direction["Estado"]

        update = int(input("Update PostalCode? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old PostalCode: {direction['CodigoPostal']}")
            postalcode = input("New PostalCode: ")
        else:
            postalcode = direction["CodigoPostal"]

        update = int(input("Update Street? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Telephone {direction['Calle']}")
            street = input("New Street : ")
        else:
            street = direction["Calle"]

        update = int(input("Update IdCity number? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old IdCity number: {direction['IdCiudad']}")
            idcity = input("New IdCity number: ")
        else:
            idcity = direction["IdCiudad"]

   

        self.direcciones.updateDirectionBD(id,state,postalcode,street,idcity)
        print("\nLos cambios se han efectuado con éxito.")
        self.direcciones.getAllDirections()

    def deleteDirection(self):
        print("Deleting direction...")
        id = int(input("ID of direction to delete: "))

        self.direcciones.deleteDirectionDB(id)
        print("La direccion se ha removido con éxito.")
        self.direcciones.getAllDirections()

#Desde aqui empieza el codigo para procesos
    def getDirection(self,direccion):   
        id = direccion["idDirecciones"]
        direccion = self.direcciones.searchDirectionById(id)

        print(f"ID de direccion única: {direccion['idDirecciones']}")
        print(f"Estado: {direccion['Estado']}")
        print(f"CodigoPostal: {direccion['CodigoPostal']}")
        print(f"Calle: {direccion['Calle']}")
        print(f"IdCiudad: {direccion['IdCiudad']}")

    def actualizarDireccion(self,direccion):
        print("\nUpdating an existing direction...")

        direction = direccion

        update = int(input("Update State? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old State: {direction['Estado']}")
            state = input("New State: ")
        else:
            state = direction["Estado"]

        update = int(input("Update PostalCode? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old PostalCode: {direction['CodigoPostal']}")
            postalcode = input("New PostalCode: ")
        else:
            postalcode = direction["CodigoPostal"]

        update = int(input("Update Street? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Street  {direction['Calle']}")
            street = input("New Street: ")
        else:
            street = direction["Calle"]

        update = int(input("Update IdCity number? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old IdCity number: {direction['IdCiudad']}")
            idcity = input("New IdCity number: ")
        else:
            idcity = direction["IdCiudad"]


        self.direcciones.updateDirectionBD(direction["IdDireccion"],state,postalcode,street,idcity)
        direction = self.direcciones.searchDirectionById(direction["IdDireccion"])
        print("\nLos cambios se han efectuado con éxito.")
        self.direcciones.getDirections(direction)