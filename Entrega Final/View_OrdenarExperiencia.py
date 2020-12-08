from prettytable import PrettyTable
from Logic_ExperienciaResidenciaLogic import ExperienciaResidenciaLogic
from Logic_ExperienciasLogic import ExperienciaLogic
from Logic_TematicaLogic import TematicaLogic



class organizarExperienciaBE:
    def __init__(self):
        self.dbexperiencia = ExperienciaLogic()
        self.dbexperienciaresidencia = ExperienciaResidenciaLogic()
        self.dbtematica =TematicaLogic()
        

    #INGRESO DE DATOS
    def addOrganizarExperiencia(self):
        self.addExperiencia()

    def addExperiencia(self):
        print("\nAdding a new experiencia...")
        host = input("\nNombre del anfitrion: ")
        ExperienceTitle = input("\nTítulo experiencia: ")
        TypeExperience =input("\nTipo de experiencia (1.Online| 2.Presencial): ")

        if TypeExperience==1:
            TypeExperience= 1
            Location=input("\nTipo de experiencia (1.Meets|2.Zoom|3.Teams|4.Otro): ")
            Idiom=input("\nIdioma : ")
            PublicObject = input("Publico objetivo: ")
            Organization = input("Organizacion: ")
            hostExperience = input("Experiencia del anfitrion(Basico|Medio|Experto): ")
            NeedElements = input("Elementos faltantes: ")
            PrecioIndividual = round(float(input("Precio Individual($0.00): ")),2)
            strFecha = input("\nFecha (yyyy-mm-dd): ")
            strHora = input("\nHora (hh:mm:ss): ")
            ordenarTematica()
            idTematic = input("¿La tematica se encuentra en las opciones?(1.Sí|2.No): ")
            if idTematic==1:
                idTematic=input("Ingrese el id de la tematica: ")
                strFechaCompleta = strFecha+" "+strHora
            if idTematic==2:
                idTematic= self.dbtematica.insertTematica()
                strFechaCompleta = strFecha+" "+strHora
        
            else:
                idTematic==1
                strFechaCompleta = strFecha+" "+strHora
        if TypeExperience==2:

            TypeExperience= 2
            Location=input("\nTipo de experiencia (1.Meets|2.Zoom|3.Teams|4.Otro): ")
            Idiom=input("\nIdioma : ")
            PublicObject = input("Publico objetivo: ")
            Organization = input("Organizacion: ")
            hostExperience = input("Experiencia del anfitrion(Basico|Medio|Experto): ")
            NeedElements = input("Elementos faltantes: ")
            PrecioIndividual = round(float(input("Precio Individual($0.00): ")),2)
            strFecha = input("\nFecha (yyyy-mm-dd): ")
            strHora = input("\nHora (hh:mm:ss): ")
            ordenarTematica()
            idTematic = input("¿La tematica se encuentra en las opciones?(1.Sí|2.No): ")
            if idTematic==1:
                idTematic=input("Ingrese el id de la tematica: ")
                strFechaCompleta = strFecha+" "+strHora
            if idTematic==2:
                idTematic= self.dbtematica.insertTematica()
                strFechaCompleta = strFecha+" "+strHora
        
            else:
                idTematic==1
                strFechaCompleta = strFecha+" "+strHora
           
        else:
            TypeExperience= 1
            Location=input("\nTipo de experiencia (1.Meets|2.Zoom|3.Teams|4.Otro): ")
            Idiom=input("\nIdioma : ")
            PublicObject = input("Publico objetivo: ")
            Organization = input("Organizacion: ")
            hostExperience = input("Experiencia del anfitrion(Basico|Medio|Experto): ")
            NeedElements = input("Elementos faltantes: ")
            PrecioIndividual = round(float(input("Precio Individual($0.00): ")),2)
            strFecha = input("\nFecha (yyyy-mm-dd): ")
            strHora = input("\nHora (hh:mm:ss): ")
            ordenarTematica()
            idTematic = input("¿La tematica se encuentra en las opciones?(1.Sí|2.No): ")
            if idTematic==1:
                idTematic=input("Ingrese el id de la tematica: ")
                strFechaCompleta = strFecha+" "+strHora
            if idTematic==2:
                idTematic= self.dbtematica.insertTematica()
                strFechaCompleta = strFecha+" "+strHora
        
            else:
                idTematic==1
                strFechaCompleta = strFecha+" "+strHora
        self.dbexperiencia.insertExperiencia(host,ExperienceTitle,TypeExperience,Location,Idiom,PublicObject,Organization,hostExperience,NeedElements,PrecioIndividual,strFechaCompleta,idTematic)
        idexperiencia=self.dbexperiencia.traerIDExperiencia(host,ExperienceTitle,TypeExperience,Location,Idiom,PublicObject,Organization,hostExperience,NeedElements,PrecioIndividual,strFechaCompleta,idTematic)
        
        print("\nSu experiencia se ha creado con éxito.\n")
        print(f"Su código de experiencia único es {idexperiencia}.\n")
        self.addExperiencia()

   
    #UPDATES

    def updateOrdenarExperiencia(self):
        self.updateExperiencia()

    def updateExperiencia(self):
        print("\nUpdating an existing experiencia...")
        id = int(input("\nID de la experiencia a actualizar: "))

        experiencia = self.dbexperiencia.searchExperienciaById(id)

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
            print(f"id Antigüa temática: { experiencia.idTematic}")
            ordenarTematica()
            idTematic = input("Nueva temática: ")
        else:
            idTematic = experiencia.idTematic

        self.dbexperiencia.updateExperienciaBD(id, host, ExperienceTitle, TypeExperience,
        Location, Descrption, Idiom, PublicObject, Organization, hostExperience, 
        NeedElements, precio, strfechacompleta, idTematic)
        print("\nLos cambios se han efectuado con éxito.")
        self.getAllExperiencias()

    

    #DELETACION
    def deleteOrganizarExperiencia(self):
        self.deleteExperiencia()

    def deleteExperiencia(self):
        print("Borrando experiencia...")
        id = int(input("ID de la experiencia a eliminar: "))

        self.dbresidencia.deleteResidenciaDB(id)
        print("La residencia se ha removido con éxito.")

    #ORDENAR

    def ordenarTematica(self):
        result = self.dbtematica.getTematicas()

        table = PrettyTable()
        table.field_names = ["IdTematica", "NombreTematica", "Descripcion"]

        for tematica in result:
            table.add_row([
                tematica.id,
                tematica.tematicaname,
                tematica.description
                ])

        print(table)
        table.clear()