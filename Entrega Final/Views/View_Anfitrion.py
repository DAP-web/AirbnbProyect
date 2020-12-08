from prettytable import PrettyTable
from Logic_ResidenciasLogic import ResidenciaLogic
from Logic_DireccionesLogic import DirectionLogic
from Logic_CiudadesLogic import CiudadesLogic
from Logic_PaisesLogic import PaisesLogic

class anfitrionBE:
    def __init__(self):
        self.dbresidencia = ResidenciaLogic()
        self.direcciones = DirectionLogic()
        self.dbciudad = CiudadesLogic()
        self.dbpais = PaisesLogic()

    #INGRESO DE DATOS
    def addAlojamiento(self):
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
        print("-"*100)
        print("¿Está el país que buscas en esta tabla? 0-No, 1-Si")
        option = int(input("Opción: "))
        if option == 0:
            self.addCountry()
        if option == 1:
            countryname = input("Nombre de pais (Escrito de la misma forma que está en la tabla): ")
            code = input("Codigo telefonico: ")
            idpais=self.dbpais.traerIDCountry(countryname,code)
            print(f"\nEl código de país elegido es {idpais}.\n")
            self.cityHub()

    def addCountry(self):
        print("Adding a new country...")
        countryname = input("Nombre de pais: ")
        code = input("Codigo telefonico: ")

        self.dbpais.insertCountry(countryname,code)
        idpais=self.dbpais.traerIDCountry(countryname,code)
        
        print("\nSu pais se ha creado con éxito.")
        print(f"\nSu código de país único es {idpais}.\n")
        self.cityHub()

    def cityHub(self):
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
        print("-"*100)
        print("¿Está la ciudad que buscas en esta tabla? 0-No, 1-Si")
        option = int(input("Opción: "))
        if option == 0:
            self.addCity()
        if option == 1:
            cityname = input("Nombre de ciudad: ")
            idcountry = input("Codigo de pais (Número recibido en el ingreso del país): ")
            idciudad=self.dbciudad.traerIDCity(cityname,idcountry)
            print(f"\nSu código de ciudad elegido es {idciudad}.\n")
            self.addDirection()

    def addCity(self):
        print("\nAdding a new city...")
        cityname = input("Nombre de ciudad: ")
        idcountry = input("Codigo de pais (Número recibido en el ingreso del país): ")

        self.dbciudad.insertCity(cityname,idcountry)
        idciudad=self.dbciudad.traerIDCity(cityname,idcountry)

        print("\nSu ciudad se ha creado con éxito.")
        print(f"\nSu código de ciudad único es {idciudad}.\n")
        self.addDirection()
    
    def addDirection(self):
        print("Adding a new direction...")
        state = input("Estado: ")
        postalcode = input("CodigoPostal: ")
        street = input("Calle: ")
        cityid = input("IdCiudad (Numero recibido en el ingreso de la ciudad): ")

        self.direcciones.insertDirection(state,postalcode,street,cityid)
        iddireccion=self.direcciones.traerIDDireccion(state,postalcode,street,cityid)

        print("\nSu direccion se ha registrado con éxito.")
        print(f"\nSu código de direccion única es {iddireccion}.\n")
        self.addResidencia()

    def addResidencia(self):
        print("Añadiendo una nueva residencia...")
        tipoAlojamiento = input("Tipo de alojamiento: ")
        habitaciones = input("Número de habitaciones: ")
        banhos = input("Número de baños: ")
        camas = input("Número de camas: ")
        idDireccion = input("id de la dirección (Código recibido en el ingreso de dirección): ")
        precio = input("Ingrese el precio de la residencia: ")
        FlexDeCancelacion = int(input("Flexibilidad de cancelación (0-No | 1-Sí): "))
        aPlus = int(input("Airbnb Plus (0-No | 1-Sí): "))
        pets = int(input("Mascotas (0-No | 1-Sí): "))
        smokers = int(input("Fumador (0-No | 1-Sí): "))

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
        print(f"\nEl código de la residencia es {idResidencia}. \n")
    
    
    #UPDATES

    def updateAlojamiento(self):
        self.updateResidencia()
        
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
        #self.getAllResidencias()

    #DELETACION
    def deleteAlojamiento(self):
        self.deleteResidencia()

    def deleteResidencia(self):
        print("Borrando residencia...")
        id = int(input("ID de residencia a eliminar: "))

        self.dbresidencia.deleteResidenciaDB(id)
        print("La residencia se ha removido con éxito.")
