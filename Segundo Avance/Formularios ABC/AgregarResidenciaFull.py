from Paises_BE import paisesBE
from DB_Paises_BE import DBPaises
from Ciudades_BE import ciudadesBE
from DB_Ciudades_BE import DBCiudades
from DB_Direcciones_BE import direccionesDB
from Residencia_BE import residenciasBE
from DB_Residencia_BE import ResidenciaDB

def residenciaFull():
    paisbe = paisesBE()
    paisdb = DBPaises()
    ciudadbe = ciudadesBE()
    ciudadbd= DBCiudades()
    direccionbd = direccionesDB()
    residenciabe = residenciasBE()
    residenciabd = ResidenciaDB()

    paisbe.getAllCountries()
    pais = input("¿En qué país se encuentra tu residencia? ")
    codigo = input("¿Cuál es el código telefónico de tu país? ")
    idpais = paisdb.traerIDCountry(pais,codigo)
    
    if idpais is None:
        paisdb.insertCountry(pais,codigo)
        idpais=paisdb.traerIDCountry(pais,codigo)
    
    ciudadbe.getAllCities()
    ciudad = input("¿En qué ciudad se localiza su residencia?" )
    idciudad = ciudadbd.traerIDCity(ciudad,idpais)
    if idciudad is None or idciudad==0:
        ciudadbd.insertCity(ciudad,idpais)
        idciudad = ciudadbd.traerIDCity(ciudad,idciudad)
    
    estado = input("¿En qué Estado se encuentra su residencia? ")
    cp = input("¿Código postal del estado? ")
    calle = input("¿En qué calle queda su residencia? ")

    iddireccion = direccionbd.traerIDDireccion(estado,cp,calle,idciudad)
    if iddireccion is None or iddireccion==0:
        direccionbd.insertDirection(estado,cp,calle,idciudad)
        iddireccion = direccionbd.traerIDDireccion(estado,cp,calle,idciudad)
    
    tipoAlojamiento = input("\nTipo de alojamiento: ")
    habitaciones = input("\nNúmero de habitaciones: ")
    banhos = input("\nNúmero de baños: ")
    camas = input("\nNúmero de camas: ")
    precio = input("\nIngrese el precio de la residencia: ")
    FlexDeCancelacion = int(input("\nFlexibilidad de cancelación (0-No | 1-Sí): "))
    aPlus = int(input("\nAirbnb Plus (0-No | 1-Sí): "))
    pets = int(input("\nMascotas (0-No | 1-Sí): "))
    smokers = int(input("\nFumador (0-No | 1-Sí): "))  

    residenciabd.insertResidencias(
            tipoAlojamiento,
            habitaciones,
            banhos,
            camas,
            iddireccion,
            precio,
            FlexDeCancelacion,
            aPlus,
            pets,
            smokers
        )

    idresidencia=residenciabd.traerIDResidencia(
            tipoAlojamiento,
            habitaciones,
            banhos,
            camas,
            iddireccion,
            precio,
            FlexDeCancelacion,
            aPlus,
            pets,
            smokers,
        )

    print("\nLa residencia se ha agregado con éxito.")
    print(f"El código de la residencia es {idresidencia}. \n")

#IdDireccion, Estado, CodigoPostal, Calle, IdCiudad

