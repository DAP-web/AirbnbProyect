from prettytable import PrettyTable
from Logic_ExperienciasLogic import ExperienciaLogic


class experienciasBE:
    def __init__(self):
        self.dbexperiencia = ExperienciaLogic()

    def getAllExperiencias(self):
        result = self.dbexperiencia.getExperiencia()

        table = PrettyTable()
        table.field_names = [
            "idExp",
            "NombreAnfitrion",
            "TituloExperiencia",
            "TipoDeExperiencia",
            "Ubicacion",
            "Descripcion",
            "Idioma",
            "PublicoObjetivo",
            "Organizacion",
            "AnfitrionExp",
            "ElementosANecesitar",
            "Precio",
            "Fecha",
            "IdTematica",
        ]

        for experiencia in result:
            table.add_row([
                experiencia.id,
                experiencia.host,
                experiencia.ExperienceTitle,
                experiencia.TypeExperience,
                experiencia.Location,
                experiencia.Descrption,
                experiencia.Idiom,
                experiencia.PublicObject,
                experiencia.Organization,
                experiencia.hostExperience,
                experiencia.NeedElements,
                experiencia.precio,
                experiencia.fecha,
                experiencia.idTematic
            ])
        print(table)
        table.clear()

    def addExperiencia(self):
        print("\nAñadiendo unua experiencia...")
        host = input("Nombre Anfrition: ")
        ExperienceTitle = input("Titulo de experiencia: ")
        TypeExperience = int(input("Tipo de experiencias (0-Online | 1-Presencial): "))
        Location = input("Direccion: ")
        Descrption = input("Descrpcion: ")
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

        print("\nLa experiencia se ha agregado con éxito")
        print(f"El codigo de la experiencia es {idExp}.\n")
        self.getAllExperiencias()

    def updateExperiencias(self):
        print("\nActualizando la experiencia...")
        id = int(input("\nID de la expereincia a actualizar: "))

        experiencia = self.dbexperiencia.searchExperienciaById(id)

        update = int(input("¿Actualizar el anfitrion? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Anfitrion antigÜo : {experiencia.host}")
            host = input("Nuevo anfitrion: ")
        else:
            host = experiencia.host

        update = int(input("¿Actualizar el titulo de la experiencia? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo titulo de la experiencia: {experiencia.ExperienceTitle}")
            ExperienceTitle = input("Nuevo titulo de experiencia: ")
        else:
            ExperienceTitle = experiencia.ExperienceTitle

        update = int(input("¿Actualizar el tipo de experiencia? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo tipo de experiencia: {experiencia.TypeExperience}")
            TypeExperience = input("Nuevo tipo de experiencia: ")
        else:
            TypeExperience = experiencia.TypeExperience

        update = int(input("¿Actualizar la ubicacion? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüa ubicacion: {experiencia.Location}")
            Location = input("Nueva ubicacion: ")
        else:
            Location = experiencia.Location

        update = int(input("¿Actualizar la descripción? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüa descripción: {experiencia.Descrption}")
            Descrption = input("Nueva descripción: ")
        else:
            Descrption = experiencia.Descrption

        update = int(input("¿Actualizar el idioma? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo idioma: {experiencia.Idiom}")
            Idiom = input("Nuevo idioma: ")
        else:
            Idiom = experiencia.Idiom

        update = int(input("¿Actualizar el publico objetivo? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo publico objetivo: {experiencia.PublicObject}")
            PublicObject = input("Nuevo publico objetivo: ")
        else:
            PublicObject = experiencia.PublicObject

        update = int(input("¿Actualizar la organización? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüa organización: {experiencia.Organization}")
            Organization = input("Nueva organización: ")
        else:
            Organization = experiencia.Organization

        update = int(input("¿Actualizar la experiencia del anfitrion? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüa experiencia del anfitrion: {experiencia.hostExperience}")
            hostExperience = input("Nueva experiencia del anfitrion: ")
        else:
            hostExperience = experiencia.hostExperience

        update = int(input("¿Actualizar los elementos a necesitar? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüos elementos a necesitar: {experiencia.NeedElements}")
            NeedElements = input("Nuevos elementos a necesitar: ")
        else:
            NeedElements = experiencia.NeedElements

        update = int(input("¿Actualizar el precio? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo precio: {experiencia.precio}")
            precio = round(float(input("Nuevo precio: ")),2)
        else:
            precio = experiencia.precio

        update = int(input("¿Actualizar fecha de la experiencia? 0-No - 1-Sí: "))
        if update == 1:
            print(f"Fecha de retirada Vieja: {experiencia.fecha}")
            strfecha = input("Nueva Fecha (yyyy-mm-dd): ")
            strhora = input("Nueva hora (hh:mm:ss): ")
            strfechacompleta = strfecha+' '+strhora
        else:
            strfechacompleta = experiencia.fecha

        update = int(input("¿Actualizar temática? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüa temática: { experiencia.idTematic}")
            idTematic = input("Nueva temática: ")
        else:
            idTematic = experiencia.idTematic

        self.dbexperiencia.updateExperienciaBD(id, host, ExperienceTitle, TypeExperience,
        Location, Descrption, Idiom, PublicObject, Organization, hostExperience, 
        NeedElements, precio, strfechacompleta, idTematic)
        print("\nLos cambios se han efectuado con éxito.")
        self.getAllExperiencias()

    def deleteExperiencia(self):
        print("Borrando experiencia...")
        id = int(input("ID de experiencia a eliminar: "))

        self.dbexperiencia.deleteExperienciaDB(id)
        print("La experiencia se ha removido con éxito.")
        self.getAllExperiencias()