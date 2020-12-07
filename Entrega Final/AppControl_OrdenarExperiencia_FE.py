from Core_databaseX import DatabaseX
from View_Experiencia import experienciasBE
from View_ExperienciaResidencia import ExperienciaResidenciasBE

experienciabe = calificionesBE()
expericniaresidenciabe= ExperienciaResidenciasBE()
organizarExperienciadb = DatabaseX()


def AppOrganizarExperiencia():
    print("Inicializando la app de Airbnb Organizar experiencia...")
    while True:
        Menu = """\nElija una de las siguientes opciones:
        0-Salir de la app
        1-Organizar experiencia
        2-Ingresar una nueva calificación\n"""
        print("-"*100)
        print(Menu)
        print("-"*100)
        option = int(input("Opción: "))

        if option == 0:
            print("\nDeteniendo la aplicación de Airbnb Clientes")
            calificaciondb.connection.close()
            break
        if option == 1:
            def addOExperiencia(self):
            print("\nOrganizar una nueva experiencia...")
                
                host = input("Nombre Anfrition: ")
                ExperienceTitle = input("Titulo de experiencia: ")
                TypeExperience = int(input("Tipo de experiencias (0-Online | 1-Presencial): "))
                Location = input("Direccion: ")
                Descrption = input("Descripcion: ")
                Idiom = input("Idioma: ")
                PublicObject = input("Publico objetivo: ")
                Organization = input("Organizacion: ")
                hostExperience = input("Experiencia del anfitrion: ")
                NeedElements = input("Elementos faltantes: ")
                PrecioIndividual = round(float(input("Precio Individual: ")),2)
                strFecha = input("\nFecha (yyyy-mm-dd): ")
                strHora = input("\nHora (hh:mm:ss): ")
                idTematic = input("Tematica ID: ")
                strFechaCompleta = strFecha+" "+strHora

        self.dbexperiencia.insertExperiencia(host, ExperienceTitle, TypeExperience, Location,
        Descrption, Idiom, PublicObject, Organization, hostExperience, NeedElements,
        PrecioIndividual,strFechaCompleta,idTematic)

        idExp = self.dbexperiencia.traerIDExperiencia(host, ExperienceTitle, TypeExperience, Location,
        Descrption, Idiom, PublicObject, Organization, hostExperience, NeedElements,
        PrecioIndividual,strFechaCompleta,idTematic)
        if option == 2:
            organizarExperienciadb.calificar()
        if option == 3:
            pass
        if option == 4:
            pass

AppOrganizarExperiencia()