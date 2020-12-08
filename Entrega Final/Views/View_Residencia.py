from prettytable import PrettyTable
from Logic_ResidenciasLogic import ResidenciaLogic


class residenciasBE:
    def __init__(self):
        self.dbresidencia = ResidenciaLogic()

    def getAllResidencias(self):
        result = self.dbresidencia.getResidencias()

        table = PrettyTable()
        table.field_names = [
            "idResidencia",
            "TipoAlojamiento",
            "Habitaciones",
            "Banhos",
            "Camas",
            "IdDireccion",
            "Precio",
            "FlexibilidadDeCancelacion",
            "AirbnbPlus",
            "Mascotas",
            "Fumadores",
        ]

        for residencia in result:
            table.add_row(
                [
                    residencia.id,
                    residencia.tipoAlojamiento,
                    residencia.habitaciones,
                    residencia.banhos,
                    residencia.camas,
                    residencia.idDireccion,
                    residencia.precio,
                    residencia.flexDeCancelacion,
                    residencia.aPlus,
                    residencia.pets,
                    residencia.smokers,
                ]
            )

        print(table)
        table.clear()

    def addResidencia(self):
        print("\nAñadiendo una nueva residencia...")
        tipoAlojamiento = input("\nTipo de alojamiento: ")
        habitaciones = input("\nNúmero de habitaciones: ")
        banhos = input("\nNúmero de baños: ")
        camas = input("\nNúmero de camas: ")
        idDireccion = input("\nid de la dirección: ")
        precio = input("\nIngrese el precio de la residencia: ")
        FlexDeCancelacion = int(input("\nFlexibilidad de cancelación (0-No | 1-Sí): "))
        aPlus = int(input("\nAirbnb Plus (0-No | 1-Sí): "))
        pets = int(input("\nMascotas (0-No | 1-Sí): "))
        smokers = int(input("\nFumador (0-No | 1-Sí): "))

        self.dbresidencia.insertResidencias(
            tipoAlojamiento,
            habitaciones,
            banhos,
            camas,
            idDireccion,
            precio,
            FlexDeCancelacion,
            aPlus,
            pets,
            smokers,
        )
        idResidencia = self.dbresidencia.traerIDResidencia(
            tipoAlojamiento,
            habitaciones,
            banhos,
            camas,
            idDireccion,
            precio,
            FlexDeCancelacion,
            aPlus,
            pets,
            smokers,
        )

        print("\nLa residencia se ha agregado con éxito.")
        print(f"El código de la residencia es {idResidencia}. \n")
        self.getAllResidencias()

    def updateResidencia(self):
        print("\nActualizando la residencia...")
        id = int(input("\nID de la residencia a actualizar: "))

        residencia = self.dbresidencia.searchResidenciasById(id)

        update = int(input("¿Actualizar tipo de alojamiento? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Tipo de alojamiento antigüo: {residencia.tipoAlojamiento}")
            tipoAlojamiento = input("Nuevo tipo de alojamiento: ")
        else:
            tipoAlojamiento = residencia.tipoAlojamiento

        update = int(input("¿Actualizar habitaciones? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo habitacion: {residencia.habitaciones}")
            habitaciones = input("Nueva habitación: ")
        else:
            habitaciones = residencia.habitaciones

        update = int(input("¿Actualizar baños? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo baño {residencia.banhos}")
            banhos = input("Nueva cantidad de baños: ")
        else:
            banhos = residencia.banhos

        update = int(input("¿Actualizar el número de camas? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo número de camas: {residencia.camas}")
            camas = input("Nuevo número de camas: ")
        else:
            camas = residencia.camas

        update = int(input("¿Actualizar precio? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo precio: {residencia.precio}")
            precio = input("Nuevo precio: ")
        else:
            precio = residencia.precio

        update = int(input("¿Actualizar flexibilidad de cancelación? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüa flexibilidad de cancelación {residencia.flexDeCancelacion}")
            FlexDeCancelacion = input("Nueva flexibilidad de cancelación: ")
        else:
            FlexDeCancelacion = residencia.flexDeCancelacion

        update = int(input("¿Actualizar Airbnb Plus? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo bnb Plus: {residencia.aPlus}")
            aPlus = input("Nueva Airbnb Plus: ")
        else:
            aPlus = residencia.aPlus

        update = int(input("¿Actualizar estadia de mascotas? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüa estadia de mascotas {residencia.pets}")
            pets = input("Nueva estadia de mascota: ")
        else:
            pets = residencia.pets

        update = int(input("¿Actualizar servicio de fumadores? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo servio de fumadores {residencia.smokers}")
            smokers = input("Nuevo servicio de fumadores: ")
        else:
            smokers = residencia.smokers

        self.dbresidencia.updateResidenciaBD(
            id,
            tipoAlojamiento,
            habitaciones,
            banhos,
            camas,
            precio,
            FlexDeCancelacion,
            aPlus,
            pets,
            smokers,
        )
        print("\nLos cambios se han efectuado con éxito.")
        self.getAllResidencias()

    def deleteResidencia(self):
        print("Borrando residencia...")
        id = int(input("ID de residencia a eliminar: "))

        self.dbresidencia.deleteResidenciaDB(id)
        print("La residencia se ha removido con éxito.")
        self.getAllResidencias()
