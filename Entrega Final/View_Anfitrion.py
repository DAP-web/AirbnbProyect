from prettytable import PrettyTable
from Logic_ResidenciasLogic import ResidenciaLogic
from Logic_DireccionesLogic import DirectionLogic
from Logic_CiudadesLogic import CiudadesLogic
from Logic_PaisesLogic import PaisesLogic


class anfitrionBE:
    def __init__(self):
        self.dbresidencia = ResidenciaLogic()
        self.iddireccion = DirectionLogic()
        self.dbciudad = CiudadesLogic()
        self.dbpais = PaisesLogic()

    #INGRESO DE DATOS
    def addAlojamiento(self):
        self.addCountry()

    def addCountry(self):
        print("\nAdding a new country...")
        countryname = input("\nNombre de pais: ")
        code = input("\nCodigo telefonico: ")

        self.dbpais.insertCountry(countryname,code)
        idpais=self.dbpais.traerIDCountry(countryname,code)
        
        print("\nSu pais se ha creado con éxito.\n")
        print(f"Su código de país único es {idpais}.\n")
        self.addCity()

    def addCity(self):
        print("\nAdding a new city...")
        cityname = input("\nNombre de ciudad: ")
        idcountry = input("\nCodigo de pais (Número recibido en el ingreso del país): ")

        self.dbciudad.insertCity(cityname,idcountry)
        idciudad=self.dbciudad.traerIDCity(cityname,idcountry)

        print("\nSu ciudad se ha creado con éxito.\n")
        print(f"Su código de ciudad único es {idciudad}.\n")
        self.addDirection()
    
    def addDirection(self):
        print("\nAdding a new direction...")
        state = input("\nEstado: ")
        postalcode = input("\nCodigoPostal: ")
        street = input("\nCalle: ")
        cityid = input("\nIdCiudad (Numero recibido en el ingreso de la ciudad): ")

        self.direcciones.insertDirection(state,postalcode,street,cityid)
        iddireccion=self.direcciones.traerIDDireccion(state,postalcode,street,cityid)

        print("\nSu direccion se ha registrado con éxito.\n")
        print(f"Su código de direccion única es {iddireccion}.\n")
        self.addResidencia()

    def addResidencia(self):
        print("\nAñadiendo una nueva residencia...")
        tipoAlojamiento = input("\nTipo de alojamiento: ")
        habitaciones = input("\nNúmero de habitaciones: ")
        banhos = input("\nNúmero de baños: ")
        camas = input("\nNúmero de camas: ")
        idDireccion = input("\nid de la dirección (Código recibido en el ingreso de dirección): ")
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
    break
    
    #UPDATES

    def updateAlojamiento(self):
        self.updateCountry()

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
        self.updateCity()

    def updateCity(self):
        print("\nUpdating an existing city...")
        id = int(input("\nID de la ciudad a actualizar: "))

        ciudad = self.dbciudad.searchCityById(id)

        update = int(input("Update Name? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old Name: {ciudad['NombreCiudad']}")
            cityname = input("New Name: ")
        else:
            cityname = ciudad["NombreCiudad"]

        update = int(input("Update IdPais? 0-No - 1-Yes "))
        if update == 1:
            print(f"Old IdPais: {ciudad['IdPais']}")
            idcountry = input("New IdPais: ")
        else:
            idcountry = ciudad["IdPais"]

        self.dbciudad.updateCityBD(id,cityname,idcountry)
        print("\nLos cambios se han efectuado con éxito.")
        self.updateDirection()

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
    break

    #DELETACION
    def deleteAlojamiento
        self.deleteResidencia()

    def deleteResidencia(self):
        print("Borrando residencia...")
        id = int(input("ID de residencia a eliminar: "))

        self.dbresidencia.deleteResidenciaDB(id)
        print("La residencia se ha removido con éxito.")
    break
