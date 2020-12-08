from prettytable import PrettyTable
from Logic_ExperienciaResidenciaLogic import ExperienciaResidenciaLogic
from Logic_ExperienciasLogic import ExperienciaLogic
from Logic_TematicaLogic import TematicaLogic
from View_Tematica import TematicaBE


class organizarExperienciaBE:
    def __init__(self):
        self.dbexperiencia = ExperienciaLogic()
        self.dbexperienciaresidencia = ExperienciaResidenciaLogic()
        self.dbtematica =TematicaLogic()
        self.viewtematica =TematicaBE()
    

    #INGRESO DE DATOS
    def addAlojamiento(self):
        self.addCountry()

    def addExperiencia(self):
        print("\nAdding a new experiencia...")
        anfitrionname = input("\nNombre del anfitrion: ")
        tituloexperiencia = input("\nTítulo experiencia: ")
        tipoexperiencia =input("\nTipo de experiencia: ")
        self.dbpais.insertCountry(countryname,code)
        idpais=self.dbpais.traerIDCountry(countryname,code)
        
        print("\nSu pais se ha creado con éxito.\n")
        print(f"Su código de país único es {idpais}.\n")
        self.addCity()

   
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

    #DELETACION
    def deleteAlojamiento(self):
        self.deleteResidencia()

    def deleteResidencia(self):
        print("Borrando residencia...")
        id = int(input("ID de residencia a eliminar: "))

        self.dbresidencia.deleteResidenciaDB(id)
        print("La residencia se ha removido con éxito.")

    #DISPLAY
    def displayTematicas(self):
       print(self.viewtematica.getAllTematicas)
        
    