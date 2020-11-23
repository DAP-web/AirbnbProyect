from prettytable import PrettyTable
from DB_Residencia_BE import (
    connection,
    getResidencias,
    insertResidencias,
    searchResidenciasById,
    updateResidenciaBD,
    traerIDResidencia,
    deleteResidenciaDB
)


def getAllResidencias():
    result = getResidencias()

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
                residencia["idResidencia"],
                residencia["TipoAlojamiento"],
                residencia["Habitaciones"],
                residencia["Banhos"],
                residencia["Camas"],
                residencia["IdDireccion"],
                residencia["Precio"],
                residencia["FlexibilidadDeCancelacion"],
                residencia["AirbnbPlus"],
                residencia["Mascotas"],
                residencia["Fumadores"]
            ]
        )
    print(table)
    table.clear()


def addResidencia():
    print("\nAñadiendo una nueva residencia...")
    tipoAlojamiento = input("\nTipo de alojamiento")
    habitaciones = input("\nNúmero de habitaciones")
    banhos = input("\nNúmero de baños")
    camas = input("\nNúmero de camas")
    idDireccion = input("\nid de la dirección")
    precio = input("\nIngrese el precio de la residencia")
    FlexDeCancelacion = int(input("\nFlexibilidad (0-No | 1-Sí): "))
    aPlus = int(input("\nAirB&B Plus (0-No | 1-Sí): "))
    pets = int(input("\nMascotas (0-No | 1-Sí): "))
    smokers = int(input("\nFumador (0-No | 1-Sí): "))

    insertResidencias(
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
    idResidencia = traerIDResidencia(
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

    print("\nLa residencia se ha agregado con éxito")
    print(f"El código de la residencia es {idResidencia}. \n")
    getAllResidencias()


def updateResidencia():
    print("\nActualizando la residencia...")
    id = int(input("\nID de la residencia a actualizar: "))

    residencia = searchResidenciasById(id)

    update = int(input("¿Actualizar tipo de alojamiento? 0-No - 1-Yes "))
    if update == 1:
        print(f"Tipo de alojamiento antigüo: {residencia['TipoAlojamiento']}")
        tipoAlojamiento = input("Nuevo tipo de alojamiento: ")
    else:
        tipoAlojamiento = residencia["TipoAlojamiento"]

    update = int(input("¿Actualizar habitaciones? 0-No - 1-Yes "))
    if update == 1:
        print(f"Antigüo habitacion: {residencia['Habitaciones']}")
        habitaciones = input("Nueva habitación: ")
    else:
        habitaciones = residencia["Habitaciones"]

    update = int(input("¿Actualizar baños? 0-No - 1-Yes "))
    if update == 1:
        print(f"Antigüo baño {residencia['Banhos']}")
        banhos = input("Nueva cantidad de baños: ")
    else:
        banhos = residencia["Banhos"]

    update = int(input("¿Actualizar el número de camas? 0-No - 1-Yes "))
    if update == 1:
        print(f"Antigüo número de camas: {residencia['Camas']}")
        camas = input("Nuevo número de camas: ")
    else:
        camas = residencia["Camas"]

    update = int(input("¿Actualizar precio? 0-No - 1-Yes "))
    if update == 1:
        print(f"Antigüo precio: {residencia['Precio']}")
        precio = input("Nuevo precio: ")
    else:
        precio = residencia["Precio"]

    update = int(input("¿Actualizar flexibilidad de cancelación? 0-No - 1-Yes "))
    if update == 1:
        print(
            f"Antigüa flexibilidad de cancelación {residencia['FlexibilidadDeCancelacion']}"
        )
        FlexDeCancelacion = input("Nueva flexibilidad de cancelación: ")
    else:
        FlexDeCancelacion = residencia["FlexibilidadDeCancelacion"]

    update = int(input("¿Actualizar Airbnb Plus? 0-No - 1-Yes "))
    if update == 1:
        print(f"Antigüo bnb Plus: {residencia['AirbnbPlus']}")
        aPlus = input("Nueva Airbnb Plus: ")
    else:
        aPlus = residencia["AirbnbPlus"]

    update = int(input("¿Actualizar estadia de mascotas? 0-No - 1-Yes "))
    if update == 1:
        print(f"Antigüa estadia de mascotas {residencia['Mascotas']}")
        pets = input("Nueva estadia de mascota: ")
    else:
        pets = residencia["Mascotas"]

    update = int(input("¿Actualizar servicio de fumadores? 0-No - 1-Yes "))
    if update == 1:
        print(f"Antigüo servio de fumadores {residencia['Fumadores']}")
        smokers = input("Nuevo servicio de fumadores: ")
    else:
        smokers = residencia["Fumadores"]

    updateResidenciaBD(
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
    getAllResidencias()


def deleteResidencia():
    print("Borrando residencia...")
    id = int(input("ID de recidencia eliminado: "))

    deleteResidenciaDB(id)
    print("La residencia se ha removido con éxito.")
    getAllResidencias()
