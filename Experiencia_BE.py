from prettytable import PrettyTable
from DB_Experiencia_BE import ExperienciaDB


class experienciasBE:
    def __init__(self):
        self.experienciabd = ExperienciaDB()

    def getAllExperiencias(self):
        result = self.experienciabd.getExperiencia()

        table = PrettyTable()
        table.field_names = {
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
            "Estado",
            "IdTematica",
        }

        for experiencia in result:
            table.add_row(
                [
                    experiencia["idExp"],
                    experiencia["NombreAnfitrion"],
                    experiencia["TituloExperiencia"],
                    experiencia["TipoDeExperiencia"],
                    experiencia["Ubicacion"],
                    experiencia["Descripcion"],
                    experiencia["Idioma"],
                    experiencia["PublicoObjetivo"],
                    experiencia["Organizacion"],
                    experiencia["AnfitrionExp"],
                    experiencia["ElementosANecesitar"],
                    experiencia["Estado"],
                    experiencia["IdTematica"],
                ]
            )
        print(table)
        table.clear()

    def addExperiencia(self):
        print("\nAñadiendo unua experiencia...")
        host = input("Nombre Anfrition: ")
        ExperienceTitle = input("Titulo de experiencia: ")
        TypeExperience = int(input("Tipo de experiencias (0-No | 1-Sí): "))
        Location = input("Direccion: ")
        Descrption = input("Descrpcion: ")
        Idiom = input("Idioma: ")
        PublicObject = input("Publico objetivo: ")
        Organization = input("Organizacion: ")
        hostExperience = input("Experiencia del anfitrion: ")
        NeedElements = input("Elementos faltantes: ")
        State = int(input("Estado (0-No | 1-Sí): "))
        idTematic = int(input("Tematica ID: "))

        self.experienciabd.insertExperiencia(
            host,
            ExperienceTitle,
            TypeExperience,
            Location,
            Descrption,
            Idiom,
            PublicObject,
            Organization,
            hostExperience,
            NeedElements,
            State,
            idTematic,
        )
        idExp = self.experienciabd.traerIDExperiencia(
            host,
            ExperienceTitle,
            TypeExperience,
            Location,
            Descrption,
            Idiom,
            PublicObject,
            Organization,
            hostExperience,
            NeedElements,
            State,
            idTematic,
        )

        print("\nLa experiencia se ha agregado con éxito")
        print("\El codigo de la experiencia es {idExp}. \n")
        self.getAllExperiencias()

    def updateExperiencias(self):
        print("\nActualizando la experiencia...")
        id = int(input("\nID de la expereincia a actualizar: "))

        experiencia = self.experienciabd.searchExperienciasById(id)

        update = int(input("¿Actualizar el anfitrion? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Anfitrion antigÜo : {experiencia['NombreAnfitrion']}")
            host = input("Nuevo anfitrion: ")
        else:
            host = experiencia["NombreAnfitrion"]

        update = int(input("¿Actualizar el titulo de la experiencia? 0-No - 1-Yes: "))
        if update == 1:
            print(
                f"Antigüo titulo de la experiencia: {experiencia['TituloExperiencia']}"
            )
            ExperienceTitle = input("Nuevo titulo de experiencia: ")
        else:
            ExperienceTitle = experiencia["TituloExperiencia"]

        update = int(input("¿Actualizar el tipo de experiencia? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo tipo de experiencia: {experiencia['TipoDeExperiencia']}")
            TypeExperience = input("Nuevo tipo de experiencia: ")
        else:
            TypeExperience = experiencia["TipoDeExperiencia"]

        update = int(input("¿Actualizar la ubicacion? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüa ubicacion: {experiencia['Ubicacion']}")
            Location = input("Nueva ubicacion: ")
        else:
            Location = experiencia["Ubicacion"]

        update = int(input("¿Actualizar la descripción? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüa descripción: {experiencia['Descripcion']}")
            Descrption = input("Nueva descripción: ")
        else:
            Descrption = experiencia["Descripcion"]

        update = int(input("¿Actualizar el idioma? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo idioma: {experiencia['Idioma']}")
            Idiom = input("Nuevo idioma: ")
        else:
            Idiom = experiencia["Idioma"]

        update = int(input("¿Actualizar el publico objetivo? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüo publico objetivo: {experiencia['PublicoObjetivo']}")
            PublicObject = input("Nuevo publico objetivo: ")
        else:
            PublicObject = experiencia["PublicoObjetivo"]

        update = int(input("¿Actualizar la organización? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüa organización: {experiencia['Organizacion']}")
            Organization = input("Nueva organización: ")
        else:
            Organization = experiencia["Organizacion"]

        update = int(input("¿Actualizar la experiencia del anfitrion? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüa experiencia del anfitrion: {experiencia['AnfitrionExp']}")
            hostExperience = input("Nueva experiencia del anfitrion: ")
        else:
            hostExperience = experiencia["AnfitrionExp"]

        update = int(input("¿Actualizar los elementos a necesitar? 0-No - 1-Yes: "))
        if update == 1:
            print(
                f"Antigüos elementos a necesitar: {experiencia['ElementosANecesitar']}"
            )
            NeedElements = input("Nuevos elementos a necesitar: ")
        else:
            NeedElements = experiencia["ElementosANecesitar"]

        update = int(input("¿Actualizar el estado? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüos estado: { experiencia['Estado']}")
            State = input("Nuevo estado: ")
        else:
            State = experiencia["Estado"]

        update = int(input("¿Actualizar el estado? 0-No - 1-Yes: "))
        if update == 1:
            print(f"Antigüos estado: { experiencia['IdTematica']}")
            idTematic = input("Nuevo estado: ")
        else:
            idTematic = experiencia["IdTematica"]

        self.experienciabd.updateExperienciaBD(
            id,
            host,
            ExperienceTitle,
            TypeExperience,
            Location,
            Descrption,
            Idiom,
            PublicObject,
            Organization,
            hostExperience,
            NeedElements,
            State,
            idTematic,
        )
        print("\nLos cambios se han efectuado con éxito.")
        self.getAllExperiencias()

    def deleteExperiencia(self):
        print("Borrando experiencia...")
        id = int(input("ID de experiencia a eliminar: "))

        self.experienciabd.deleteExperienciaDB(id)
        print("La experiencia se ha removido con éxito.")
        self.getAllExperiencias()